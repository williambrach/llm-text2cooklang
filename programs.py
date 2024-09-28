import dspy


class CookLangSignature(dspy.Signature):
    """
    Convert plain recipe text with provided ingredients into Cooklang text format.
    Cooklang Recipe Specification:
        1. Ingredients
        - Use `@` to define ingredients
        - For multi-word ingredients, end with `{}`
        - Specify quantity in `{}` after the name
        - Use `%` to separate quantity and unit
        ```
        @salt
        @ground black pepper{}
        @potato{2}
        @bacon strips{1%kg}
        @syrup{1/2%tbsp}
        ```
        2. Comments
        - Single-line: Use `--` at the end of a line
        - Multi-line: Enclose in `[- -]`
        ```
        -- Don't burn the roux!
        Mash @potato{2%kg} until smooth -- alternatively, boil 'em first, then mash 'em, then stick 'em in a stew.
        ```
        3. Cookware
        - Define with `#`
        - Use `{}` for multi-word items
        ```
        #pot
        #potato masher{}
        ```
        4. Timers
        - Define with `~`
        - Specify duration in `{}`
        - Can include a name before the duration
        ```
        ~{25%minutes}
        ~eggs{3%minutes}
        ```
    Return only Cooklang formatted recipe, dont return any other information. Return whole recipe in Cooklang format! Dont stop till you reach the end of the recipe.
    """

    ingredients = dspy.InputField(
        desc="Ingredients for the recipe. Comma separated list of ingredients."
    )
    recipe_text = dspy.InputField(desc="Recipe text to convert to Cooklang format.")

    cooklang = dspy.OutputField(
        desc="Cooklang formatted recipe.",
    )


class CookLangFormatter(dspy.Module):
    def __init__(self):
        super().__init__()

        self.prog = dspy.ChainOfThought(CookLangSignature)

    def forward(self, recipe_text: str, ingredients: str) -> CookLangSignature:
        prediction = self.prog(recipe_text=recipe_text, ingredients=ingredients)
        return prediction


class CookLangSignatureNoSteps(dspy.Signature):
    """
    Convert plain recipe text with provided ingredients into Cooklang text format.
    Return only Cooklang formatted recipe, dont return any other information. Return whole recipe in Cooklang format! Dont stop till you reach the end of the recipe.
    """

    ingredients = dspy.InputField(
        desc="Ingredients for the recipe. Comma separated list of ingredients."
    )
    recipe_text = dspy.InputField(desc="Recipe text to convert to Cooklang format.")

    cooklang = dspy.OutputField(
        desc="Cooklang formatted recipe.",
    )


class CookLangFormatterNoSteps(dspy.Module):
    def __init__(self):
        super().__init__()

        self.prog = dspy.ChainOfThought(CookLangSignatureNoSteps)

    def forward(self, recipe_text: str, ingredients: str) -> CookLangSignatureNoSteps:
        prediction = self.prog(recipe_text=recipe_text, ingredients=ingredients)
        return prediction


class CookLangSignatureNoStepsNoIngredients(dspy.Signature):
    """
    Convert plain recipe text with provided ingredients into Cooklang text format.
    Return only Cooklang formatted recipe, dont return any other information. Return whole recipe in Cooklang format! Dont stop till you reach the end of the recipe.
    """

    recipe_text = dspy.InputField(desc="Recipe text to convert to Cooklang format.")

    cooklang = dspy.OutputField(
        desc="Cooklang formatted recipe.",
    )


class CookLangFormatterNoStepsNoIngredients(dspy.Module):
    def __init__(self):
        super().__init__()

        self.prog = dspy.ChainOfThought(CookLangSignatureNoStepsNoIngredients)

    def forward(self, recipe_text: str) -> CookLangSignatureNoStepsNoIngredients:
        prediction = self.prog(recipe_text=recipe_text)
        return prediction


SUPPORTED_MODEL_TYPES = [
    t.lower() for t in ["miprov2", "MIPROv2", "fewshot", "randomfewshot", "zeroshot"]
]

SUPPORTED_MODELS = [
    m.lower()
    for m in [
        "gpt-4o-mini",
        "gpt-4o",
        "llama3.1:8b",
        "llama3.1:70b",
        "llama3.1:70b+gpt-4o",
        "llama3.1:8b+gpt-4o",
    ]
]


def get_program_class(
    model_type: str, model_name: str, cooklang_spec: bool, ingredients: bool
):
    model_type = model_type.lower()
    model_name = model_name.lower()
    if model_type not in [t.lower() for t in SUPPORTED_MODEL_TYPES]:
        raise ValueError(f"Unsupported model type: {model_type}")

    if model_name not in [m.lower() for m in SUPPORTED_MODELS]:
        raise ValueError(f"Unsupported model: {model_name}")

    if cooklang_spec and ingredients:
        return CookLangFormatter()
    elif ingredients:
        return CookLangFormatterNoSteps()
    else:
        return CookLangFormatterNoStepsNoIngredients()


def get_program(
    model_type: str, model_name: str, cooklang_spec: bool, ingredients: bool
):
    program = get_program_class(model_type, model_name, cooklang_spec, ingredients)
    # RandomFewShot_llama3.1/70b_without_cooklang_spec
    if model_type.lower() == "miprov2":
        model_type = "MIPROv2"
    elif model_type.lower() == "zeroshot":
        model_type = "zeroshot"
    elif model_type.lower() == "fewshot" or model_type.lower() == "randomfewshot":
        model_type = "RandomFewShot"
    else:
        raise ValueError(f"Unexpected model type: {model_type}")

    cooklang_spec_str = (
        "_with_cooklang_spec" if cooklang_spec else "_without_cooklang_spec"
    )
    ingredients_str = "" if ingredients else "_without_ings"

    program_data_name = (
        f"{model_type}_{model_name}{cooklang_spec_str}{ingredients_str}.json"
    )
    print(f"Loading program data from: data/programs/{program_data_name}")
    program.load(path=f"data/programs/{program_data_name}")
    return program
