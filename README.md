# CookLang Recipe Converter
This project converts plain text recipes into CookLang format using various language models. This is just repository for the paper project.

## Prerequisites

- Python 3.12

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install cooklang-in-c:
    ```
    git clone https://github.com/cooklang/cook-in-c.git

    python setup.py build
    ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root with the following variables:
   ```
   AZURE_OPENAI_KEY=your_azure_openai_key
   AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
   AZURE_OPENAI_DEPLOYMENT_4o_mini=your_deployment_name
   AZURE_OPENAI_DEPLOYMENT_4o=your_deployment_name
   AZURE_OPENAI_VERSION=your_api_version
   OLLAMA_URL=your_ollama_url
   ```

## Running the Script

1. The `pycooklang.ipynb` notebook will:
   - Parse the input dataset
   - Create examples for training
   - Train and optimize various models (Llama, Azure OpenAI)
   - Save the optimized programs in the `data/programs/` directory

2. The `predict.ipynb` notebook will:
   - Parse the input dataset
   - Create examples for training
   - Train and optimize various models (Llama, Azure OpenAI)
   - Save the optimized programs in the `data/programs/` directory

3. The `eval.ipynb` notebook will:
   - Parse the input dataset
   - Create examples for training
   - Train and optimize various models (Llama, Azure OpenAI)
   - Save the optimized programs in the `data/programs/` directory


# Results table 

|    | with_cooklang   | without_ings   | model        | prompt_techqnique   |       WER |   ROUGE-L |       TER |
|---:|:----------------|:---------------|:-------------|:--------------------|----------:|----------:|----------:|
| 13 | False           | True           | gpt-4o       | RandomFewShot       | 0.0476775 |  0.990331 |  0.125271 |
| 24 | True            | True           | gpt-4o       | MIPROv2             | 0.0517735 |  0.990195 |  0.1246   |
| 25 | True            | True           | gpt-4o       | RandomFewShot       | 0.0559931 |  0.984831 |  0.15703  |
| 12 | False           | True           | gpt-4o       | MIPROv2             | 0.058581  |  0.983952 |  0.1391   |
| 16 | False           | True           | gpt-4o-mini  | RandomFewShot       | 0.0606936 |  0.983308 |  0.175653 |
| 28 | True            | True           | gpt-4o-mini  | RandomFewShot       | 0.0697857 |  0.982162 |  0.19549  |
|  1 | False           | False          | gpt-4o       | RandomFewShot       | 0.115338  |  0.941359 |  0.34636  |
|  3 | False           | False          | gpt-4o-mini  | MIPROv2             | 0.135256  |  0.93586  |  0.397854 |
|  4 | False           | False          | gpt-4o-mini  | RandomFewShot       | 0.129098  |  0.928446 |  0.381446 |
| 26 | True            | True           | gpt-4o       | zeroshot            | 0.199238  |  0.907482 |  1.13835  |
| 15 | False           | True           | gpt-4o-mini  | MIPROv2             | 0.185536  |  0.903004 |  1.104    |
|  2 | False           | False          | gpt-4o       | zeroshot            | 0.339778  |  0.869209 |  1.26664  |
| 14 | False           | True           | gpt-4o       | zeroshot            | 0.372436  |  0.843238 |  1.7383   |
|  0 | False           | False          | gpt-4o       | MIPROv2             | 0.555943  |  0.841092 |  2.72135  |
| 27 | True            | True           | gpt-4o-mini  | MIPROv2             | 0.278445  |  0.837479 |  1.81314  |
| 29 | True            | True           | gpt-4o-mini  | zeroshot            | 0.274373  |  0.811401 |  2.32433  |
| 31 | True            | True           | llama3.1:70b | RandomFewShot       | 0.46743   |  0.731679 |  2.73804  |
| 32 | True            | True           | llama3.1:70b | zeroshot            | 0.46743   |  0.731679 |  2.73804  |
| 17 | False           | True           | gpt-4o-mini  | zeroshot            | 0.675318  |  0.730529 |  2.80864  |
|  5 | False           | False          | gpt-4o-mini  | zeroshot            | 0.912785  |  0.674131 |  3.78378  |
| 35 | True            | True           | llama3.1:8b  | zeroshot            | 0.692294  |  0.636374 |  4.05067  |
| 30 | True            | True           | llama3.1:70b | MIPROv2             | 0.854265  |  0.621998 |  4.0269   |
| 34 | True            | True           | llama3.1:8b  | RandomFewShot       | 0.635604  |  0.617826 |  3.4939   |
|  7 | False           | False          | llama3.1:70b | RandomFewShot       | 0.879641  |  0.586772 |  3.96347  |
| 22 | False           | True           | llama3.1:8b  | RandomFewShot       | 0.848772  |  0.583771 |  3.64784  |
| 23 | False           | True           | llama3.1:8b  | zeroshot            | 0.963108  |  0.565372 |  4.07367  |
|  8 | False           | False          | llama3.1:70b | zeroshot            | 1.08496   |  0.560791 |  4.69368  |
| 11 | False           | False          | llama3.1:8b  | zeroshot            | 1.10464   |  0.560307 |  5.1225   |
| 20 | False           | True           | llama3.1:70b | zeroshot            | 1.04453   |  0.534683 |  4.54761  |
| 19 | False           | True           | llama3.1:70b | RandomFewShot       | 1.26057   |  0.532556 |  6.50786  |
| 18 | False           | True           | llama3.1:70b | MIPROv2             | 1.30568   |  0.410476 |  6.35512  |
| 33 | True            | True           | llama3.1:8b  | MIPROv2             | 1.9784    |  0.321543 |  9.43973  |
| 21 | False           | True           | llama3.1:8b  | MIPROv2             | 1.99379   |  0.289787 |  9.4096   |
| 10 | False           | False          | llama3.1:8b  | RandomFewShot       | 2.06598   |  0.267919 | 10.2592   |
|  9 | False           | False          | llama3.1:8b  | MIPROv2             | 1.87905   |  0.230551 |  8.92181  |
|  6 | False           | False          | llama3.1:70b | MIPROv2             | 1.45797   |  0.197413 |  7.50252  |


# Results table domain

|    | with_cooklang   | without_ings   | model        | prompt_techqnique   |   find_all_ings |   num_bonus_ings |   num_missing_ings |   find_all_units |   find_all_amounts |
|---:|:----------------|:---------------|:-------------|:--------------------|----------------:|-----------------:|-------------------:|-----------------:|-------------------:|
| 27 | True            | True           | gpt-4o-mini  | MIPROv2             |         0.90625 |          4.375   |            0.15625 |          0.59375 |           0.65625  |
| 15 | False           | True           | gpt-4o-mini  | MIPROv2             |         0.84375 |          2.59375 |            0.28125 |          0.65625 |           0.671875 |
| 24 | True            | True           | gpt-4o       | MIPROv2             |         0.84375 |          0.28125 |            0.15625 |          0.6875  |           0.78125  |
| 13 | False           | True           | gpt-4o       | RandomFewShot       |         0.8125  |          0.46875 |            0.25    |          0.78125 |           0.78125  |
| 12 | False           | True           | gpt-4o       | MIPROv2             |         0.78125 |          0.84375 |            0.28125 |          0.75    |           0.75     |
| 26 | True            | True           | gpt-4o       | zeroshot            |         0.78125 |          0.78125 |            0.25    |          0.6875  |           0.71875  |
| 25 | True            | True           | gpt-4o       | RandomFewShot       |         0.75    |          0.375   |            0.28125 |          0.71875 |           0.71875  |
| 16 | False           | True           | gpt-4o-mini  | RandomFewShot       |         0.71875 |          0.53125 |            0.34375 |          0.59375 |           0.59375  |
| 28 | True            | True           | gpt-4o-mini  | RandomFewShot       |         0.6875  |          0.84375 |            0.5625  |          0.59375 |           0.5625   |
| 29 | True            | True           | gpt-4o-mini  | zeroshot            |         0.59375 |          1       |            0.78125 |          0.34375 |           0.46875  |
|  1 | False           | False          | gpt-4o       | RandomFewShot       |         0.53125 |          2.125   |            1.09375 |          0.21875 |           0.25     |
|  3 | False           | False          | gpt-4o-mini  | MIPROv2             |         0.53125 |          2.4375  |            0.96875 |          0.1875  |           0.1875   |
|  0 | False           | False          | gpt-4o       | MIPROv2             |         0.53125 |          2.28125 |            0.96875 |          0.15625 |           0.15625  |
| 30 | True            | True           | llama3.1:70b | MIPROv2             |         0.5     |          1.21875 |            4.09375 |          0.40625 |           0.375    |
| 31 | True            | True           | llama3.1:70b | RandomFewShot       |         0.5     |          1.375   |            2.28125 |          0.3125  |           0.34375  |
| 32 | True            | True           | llama3.1:70b | zeroshot            |         0.5     |          1.375   |            2.28125 |          0.3125  |           0.34375  |
|  4 | False           | False          | gpt-4o-mini  | RandomFewShot       |         0.46875 |          2.25    |            1.09375 |          0.21875 |           0.1875   |
| 35 | True            | True           | llama3.1:8b  | zeroshot            |         0.4375  |          0.3125  |            3.875   |          0.34375 |           0.375    |
| 34 | True            | True           | llama3.1:8b  | RandomFewShot       |         0.40625 |          0.5625  |            4.5     |          0.34375 |           0.34375  |
| 14 | False           | True           | gpt-4o       | zeroshot            |         0.28125 |          5.25    |            3.875   |          0       |           0        |
| 19 | False           | True           | llama3.1:70b | RandomFewShot       |         0.28125 |          1.53125 |            4.875   |          0.25    |           0.25     |
| 18 | False           | True           | llama3.1:70b | MIPROv2             |         0.25    |          1.625   |            6.46875 |          0.125   |           0.125    |
|  2 | False           | False          | gpt-4o       | zeroshot            |         0.21875 |          7.0625  |            3.53125 |          0       |           0        |
|  7 | False           | False          | llama3.1:70b | RandomFewShot       |         0.125   |          2.71875 |            5.65625 |          0.03125 |           0.03125  |
| 33 | True            | True           | llama3.1:8b  | MIPROv2             |         0.03125 |          0.5     |            8.78125 |          0.03125 |           0        |
|  8 | False           | False          | llama3.1:70b | zeroshot            |         0       |          0       |            9.03125 |          0       |           0        |
|  5 | False           | False          | gpt-4o-mini  | zeroshot            |         0       |          0.53125 |            8.90625 |          0       |           0        |
|  6 | False           | False          | llama3.1:70b | MIPROv2             |         0       |          0.09375 |            8.84375 |          0       |           0        |
| 17 | False           | True           | gpt-4o-mini  | zeroshot            |         0       |          0.71875 |            8.84375 |          0       |           0        |
| 10 | False           | False          | llama3.1:8b  | RandomFewShot       |         0       |          1.40625 |            8.96875 |          0       |           0        |
| 11 | False           | False          | llama3.1:8b  | zeroshot            |         0       |          0       |            9.03125 |          0       |           0        |
| 23 | False           | True           | llama3.1:8b  | zeroshot            |         0       |          0       |            9.03125 |          0       |           0        |
| 22 | False           | True           | llama3.1:8b  | RandomFewShot       |         0       |          0       |            9.03125 |          0       |           0        |
| 21 | False           | True           | llama3.1:8b  | MIPROv2             |         0       |          0.75    |            9       |          0       |           0        |
| 20 | False           | True           | llama3.1:70b | zeroshot            |         0       |          0       |            9.03125 |          0       |           0        |
|  9 | False           | False          | llama3.1:8b  | MIPROv2             |         0       |          0.15625 |            9       |          0       |           0        |


## MIPROv2 with cooklang with ings prompt example

```
**  
Transform the given plain text recipe and accompanying ingredients into a structured Cooklang format. Use the following specifications:

1. **Ingredients:**
   - Prefix each ingredient with `@`.
   - For multi-word ingredients, wrap the entire ingredient in `{}`.
   - Indicate the quantity directly after the ingredient name in `{}`, followed by a `%` for the unit.
   - Example: `@salt`, `@ground black pepper{}`, `@potato{2}`, `@bacon strips{1%kg}`, `@syrup{1/2%tbsp}`.

2. **Comments:**
   - Use `--` to denote single-line comments.
   - For multi-line comments, enclose them in `[- -]`.
   - Example: `-- Don't burn the roux!`.

3. **Cookware:**
   - Use `#` to specify the cookware required.
   - For multi-word items, enclose in `{}`.
   - Example: `#pot`, `#potato masher{}`.

4. **Timers:**
   - Use `~` to specify timing instructions.
   - Indicate the duration in `{}`.
   - You may include a name before the duration.
   - Example: `~{25%minutes}`, `~eggs{3%minutes}`.

Return only the Cooklang formatted recipe without any additional commentary or information. Ensure that the output is complete and captures all elements of the recipe succinctly.

---

Ingredients: 1 kg corn beef,3 medium potatoes,3 medium carrots,1 cup frozen peas,4 eggs,6 pickles,1 cup mayonnaise,1 tbsp dill
Recipe Text: Zero step is cook corn beef (1 kg). Put into a large pan and simmer for 2 hours. The first step is to cook your potatoes (3 medium) and carrots (3 medium). I used a steamer, but you can always go the traditional route and boil them. In either case, peel the carrots but not the potatoes. Steam the potatoes for 30 minutes to start with, and then add the peeled carrots. Continue steaming for 10-15 more minutes, or until the potatoes and carrots are firm but tender when poked. Meanwhile, cook your frozen peas (1 cup) according to package directions. I use the kind that can be steamed in the package in the microwave. When they are done, set them aside to cool. When the potatoes and carrots are done, allow them to cool to the point that you can handle them easily. Peel the potatoes. Using your fingers or the back of a knife, gently scrape the thin layer of skin off of the potatoes. Dice them into 1cm cube-ish shapes and put them into a medium serving bowl. Next, dice your carrots. I've heard it said that a Soviet housewife could be judged on her housekeeping skills by how finely she could dice vegetables for her soups and salads. I, however, won't judge you. In fact, if you chop your potatoes and carrots a little larger, I would probably even thank you. I happen to like chunky salads. Toss the carrots and a cup of steamed peas into the bowl with the potatoes. Peel and dice your hardboiled eggs (4). Again, I know some like to have their salads with finely diced ingredients, but I don't. So dice them however you like. Chop pickles (6) finely. I used small snacking dill pickles, so I needed to use six of them. If you have larger pickles, try using three and see if that is enough for you. Add the meat if using and mix everything together gently before you add the mayonnaise (1 cup). Stir in one cup of mayo to start with, and add more if you think that the salad needs more binding together. Cover the salad and chill for at least one hour or overnight to allow the flavors to come together. And of course, garnish with finely chopped dill (1 tbsp). This is a Russian salad, after all.
Cooklang: Zero step is cook @corn beef{1%kg}. Put into a large pan and simmer for ~{2%hours}. The first step is to cook your @potatoes{3%medium} and @carrots{3%medium}. I used a steamer, but you can always go the traditional route and boil them. In either case, peel the carrots but not the potatoes. Steam the potatoes for ~{30%minutes} to start with, and then add the peeled carrots. Continue steaming for 10-15 more minutes, or until the potatoes and carrots are firm but tender when poked. Meanwhile, cook your @frozen peas{1%cup} according to package directions. I use the kind that can be steamed in the package in the microwave. When they are done, set them aside to cool. When the potatoes and carrots are done, allow them to cool to the point that you can handle them easily. Peel the potatoes. Using your fingers or the back of a knife, gently scrape the thin layer of skin off of the potatoes. Dice them into 1cm cube-ish shapes and put them into a medium serving bowl. Next, dice your carrots. I've heard it said that a Soviet housewife could be judged on her housekeeping skills by how finely she could dice vegetables for her soups and salads. I, however, won't judge you. In fact, if you chop your potatoes and carrots a little larger, I would probably even thank you. I happen to like chunky salads. Toss the carrots and a cup of steamed peas into the bowl with the potatoes. Peel and dice your hardboiled @eggs{4}. Again, I know some like to have their salads with finely diced ingredients, but I don't. So dice them however you like. Chop @pickles{6} finely. I used small snacking dill pickles, so I needed to use six of them. If you have larger pickles, try using three and see if that is enough for you. Add the meat if using and mix everything together gently before you add the @mayonnaise{1%cup}. Stir in one cup of mayo to start with, and add more if you think that the salad needs more binding together. Cover the salad and chill for at least one hour or overnight to allow the flavors to come together. And of course, garnish with finelly chopped @dill{1%tbsp}. This is a Russian salad, after all.

Ingredients: 100 g aubergine,80 g potatoes,40 g onions,70 g carrots,100 g red bell pepper,some oil.,120 g tomatoes,0.333 tsp smoked paprika,0.333 tsp rosemary,0.333 tsp thyme,0.333 tsp caraway,75 g tomato paste,0.333 tsp garlic paste,0.500 tsp sugar,some salt,some pepper,30 ml water
Recipe Text: Dice the aubergine into neat cubes of the same size, peel and cube the potatoes, onions, carrots and red bell pepper into medium chunks. Heat a deep frying pan or wok over a high heat with a little vegetable oil. Add the carrots and onions and sauté for 2 minutes until the onions are soft and translucent. Add the aubergines, potatoes and bell peppers to the pan and fry, then dice the tomatoes and add them to the pan. Stir in smoked paprika, rosemary, thyme and caraway and sauté over a medium heat for 8 minutes to reduce the sauce. Fry on a medium heat for 8 minutes, stirring occasionally to prevent burning on the bottom. Add the tomato paste and garlic paste, sugar per serving, salt and pepper to taste at the end. Stir in a little water to add some more liquid. Cover and stew over a low heat for 30 minutes, stirring occasionally. Serve warm or completely cooled like a ratatouille with pasta or toasted ciabatta.
Cooklang: Dice the @aubergine{100%g} into neat cubes of the same size, peel and cube the @potatoes{80%g}, @onions{40%g}, @carrots{70%g} and @red bell pepper{100%g} into medium chunks. Heat a #deep frying pan{} or wok over a high heat with a little vegetable @oil. Add the carrots and onions and sauté for ~{2%minutes} until the onions are soft and translucent. Add the aubergines, potatoes and bell peppers to the pan and fry, then dice the @tomatoes{120%g} and add them to the pan. Stir in @smoked paprika{1/3%tsp}, @rosemary{1/3%tsp}, @thyme{1/3%tsp} and @caraway{1/3%tsp} and sauté over a medium heat for ~{8%minutes} to reduce the sauce. Fry on a medium heat for ~{8%minutes}, stirring occasionally to prevent burning on the bottom. Add the @tomato paste{75%g} and @garlic paste{1/3%tsp}, @sugar{1/2%tsp} per serving, @salt and @pepper to taste at the end. Stir in a little @water{30%ml} to add some more liquid. Cover and stew over a low heat for ~{30%minutes}, stirring occasionally. Serve warm or completely cooled like a ratatouille with pasta or toasted ciabatta.

---

Follow the following format.

Ingredients: Ingredients for the recipe. Comma separated list of ingredients.

Recipe Text: Recipe text to convert to Cooklang format.

Reasoning: Let's think step by step in order to ${produce the cooklang}. We ...

Cooklang: Cooklang formatted recipe.

---

Ingredients: 3 eggs,125 g flour,250 ml milk,1 pinch sea salt,some oil

Recipe Text: Crack the eggs into a blender, then add the flour, milk and sea salt, and blitz until smooth. Pour into a bowl and leave to stand for 15 minutes. Melt the butter (or a drizzle of oil if you want to be a bit healthier) in a large non-stick frying pan on a medium heat, then tilt the pan so the butter coats the surface. Pour in 1 ladle of batter and tilt again, so that the batter spreads all over the base, then cook for 1 to 2 minutes, or until it starts to come away from the sides. Once golden underneath, flip the pancake over and cook for 1 further minute, or until cooked through. Serve straightaway with your favourite topping.

Reasoning: Let's think step by step in order to ``` @eggs{3} @flour{125%g} @milk{250%ml} @sea salt{1%pinch} @oil{} Crack the @eggs{3} into a #blender{} then add the @flour{125%g}, @milk{250%ml} and @sea salt{1%pinch}, and blitz until smooth. Pour into a bowl and leave to stand for ~{15%minutes}. Melt the @oil{} in a large non-stick #frying pan{} on a medium heat, then tilt the pan so the @oil{} coats the surface. Pour in 1 ladle of batter and tilt again, so that the batter spreads all over the base, then cook for ~{1-2%minutes}, or until it starts to come away from the sides. Once golden underneath, flip the pancake over and cook for ~{1%minute}, or until cooked through. Serve straightaway with your favourite topping. ```

Cooklang: ``` @eggs{3} @flour{125%g} @milk{250%ml} @sea salt{1%pinch} @oil{} Crack the @eggs{3} into a #blender{} then add the @flour{125%g}, @milk{250%ml} and @sea salt{1%pinch}, and blitz until smooth. Pour into a bowl and leave to stand for ~{15%minutes}. Melt the @oil{} in a large non-stick #frying pan{} on a medium heat, then tilt the pan so the @oil{} coats the surface. Pour in 1 ladle of batter and tilt again, so that the batter spreads all over the base, then cook for ~{1-2%minutes}, or until it starts to come away from the sides. Once golden underneath, flip the pancake over and cook for ~{1%minute}, or until cooked through. Serve straightaway with your favourite topping. ```

---

Ingredients: 100 g potatoes,50 g onions,200 g mushrooms,some oil,4 g salt,0.250 tsp pepper,0.250 tsp rosemary,50 g double cream,some salt

Recipe Text: Peel and chop the potatoes, onions and mushrooms into chunks. The potatoes will need to be cut a bit smaller. Heat a frying pan over a medium heat with a little oil and sauté the vegetables until golden. Season with salt, pepper and chopped fresh rosemary. Put the sautéed vegetables into a saucepan and pour water over them until just covered. Bring to the boil over a medium heat, then lower the heat and leave at a low simmer until the potatoes are tender. Remove the soup from the heat and blend with a blender, add the double cream and salt to taste. Garnish with freshly cracked black pepper.

Reasoning: Let's think step by step in order to ``` @potatoes{100%g} @onions{50%g} @mushrooms{200%g} @oil{} @salt{4%g} @pepper{1/4%tsp} @rosemary{1/4%tsp} @double cream{50%g} @salt{} Peel and chop the @potatoes, @onions and @mushrooms into chunks. The @potatoes will need to be cut a bit smaller. Heat a #frying pan{} over a medium heat with a little @oil and sauté the vegetables until golden. Season with @salt, @pepper and chopped fresh @rosemary. Put the sautéed vegetables into a #saucepan{} and pour water over them until just covered. Bring to the boil over a medium heat, then lower the heat and leave at a low simmer until the @potatoes are tender. Remove the soup from the heat and blend with a #blender{}, add the @double cream and @salt to taste. Garnish with freshly cracked black @pepper. ```

Cooklang: ``` @potatoes{100%g} @onions{50%g} @mushrooms{200%g} @oil{} @salt{4%g} @pepper{1/4%tsp} @rosemary{1/4%tsp} @double cream{50%g} @salt{} Peel and chop the @potatoes, @onions and @mushrooms into chunks. The @potatoes will need to be cut a bit smaller. Heat a #frying pan{} over a medium heat with a little @oil and sauté the vegetables until golden. Season with @salt, @pepper and chopped fresh @rosemary. Put the sautéed vegetables into a #saucepan{} and pour water over them until just covered. Bring to the boil over a medium heat, then lower the heat and leave at a low simmer until the @potatoes are tender. Remove the soup from the heat and blend with a #blender{}, add the @double cream and @salt to taste. Garnish with freshly cracked black @pepper. ```

---

Ingredients: 50 g strawberries,1 banana,50 g blueberries,100 g milk,30 g oat flakes,10 g chia seeds,10 g granola,1 g salt,10 g fresh blueberries,10 g fresh raspberries

Recipe Text: Blend strawberries, banana, blueberries, milk, oat flakes, chia seeds, granola, salt with a blender, allow to settle for 10 minutes, pour into a bowl and garnish with fresh blueberries and fresh raspberries. You can use fresh or frozen fruit for this smoothie.

Reasoning: Let's think step by step in order to ``` @strawberries{50%g} @banana{1} @blueberries{50%g} @milk{100%g} @oat flakes{30%g} @chia seeds{10%g} @granola{10%g} @salt{1%g} @fresh blueberries{10%g} @fresh raspberries{10%g} Blend @strawberries{50%g}, @banana{1}, @blueberries{50%g}, @milk{100%g}, @oat flakes{30%g}, @chia seeds{10%g}, @granola{10%g}, @salt{1%g} with a #blender{}; allow to settle for ~{10%minutes}. Pour into a bowl and garnish with @fresh blueberries{10%g} and @fresh raspberries{10%g}. You can use fresh or frozen fruit for this smoothie. ```

Cooklang: ``` @strawberries{50%g} @banana{1} @blueberries{50%g} @milk{100%g} @oat flakes{30%g} @chia seeds{10%g} @granola{10%g} @salt{1%g} @fresh blueberries{10%g} @fresh raspberries{10%g} Blend @strawberries{50%g}, @banana{1}, @blueberries{50%g}, @milk{100%g}, @oat flakes{30%g}, @chia seeds{10%g}, @granola{10%g}, @salt{1%g} with a #blender{}; allow to settle for ~{10%minutes}. Pour into a bowl and garnish with @fresh blueberries{10%g} and @fresh raspberries{10%g}. You can use fresh or frozen fruit for this smoothie. ```

---

Ingredients: {ingredients}

Recipe Text: {recipe text}

Reasoning: Let's think step by step in order to 
```

## Few-shot example with cooklang with ingredients

```

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

---

Follow the following format.

Ingredients: Ingredients for the recipe. Comma separated list of ingredients.

Recipe Text: Recipe text to convert to Cooklang format.

Reasoning: Let's think step by step in order to ${produce the cooklang}. We ...

Cooklang: Cooklang formatted recipe.

---

Ingredients: 1 egg yoke,125 g condenced milk,3tsp instant coffee,1,1/2cups water,3tsp gelatine,1 eggwhite,60 g cashew
Recipe Text: Crack the egg yoke into a bowl, then add the condenced milk and instant coffee, and mix until a nice caramel is formed. Do not allow to bubble. Pour into a bowl and leave to cool down for 15 minutes. Heat water and gelatine then stir till gelatine is dissolved completely. Once gelatine is cooled down mix it with the caramel. Beat eggwhite until formy. Then mix the whites bit by bit to the the gelatine-caramel mixture. Pour into a pudding bowl and leave in fridge for 2 hours minimum. Add some cashew and enjoy!
Cooklang: Crack the @egg yoke{1} into a bowl, then add the @condenced milk{125%g} and @instant coffee{3tsp}, and mix until a nice caramel is formed. Do not allow to bubble. Pour into a #bowl and leave to cool down for ~{15%minutes}. heat @water{1,1/2cups} and @gelatine{3tsp} then stir till gelatine is dissolved completely.Once gelatine is colled down mix it with the caramel. Beat @eggwhite{1} until formy. Then mix the whites bit by bit to the the gelatinecaramel mixture. Pour into a #puddingbowl and leave in fridge for 2 hours minimum. Add some @cashew{60%g} and enjoy!

---

Ingredients: 30 g red bell pepper,30 g courgette,30 g tomatoes,30 g mozzarella cheese,2 eggs,30 g double cream,0.250 tsp salt,0.250 tsp pepper
Recipe Text: Preheat the oven to 180 degrees. Finely dice red bell pepper, courgette, tomatoes and grate the mozzarella cheese. Beat the eggs in a bowl and add the double cream, salt and pepper and whisk well with a fork. Add the vegetables to the egg mixture and pour it into the pan, sprinkle with cheese and place in the oven to bake for 7 minutes. Take an oven mitt and remove the pan from the oven, fold the omelette in half and place on a plate. Garnish with finely chopped fresh parsley and serve with a relish or chutney.
Cooklang: Preheat the oven to 180 degrees. Finely dice @red bell pepper{30%g}, @courgette{30%g}, @tomatoes{30%g} and grate the @mozzarella cheese{30%g}. Beat the @eggs{2} in a #bowl and add the @double cream{30%g}, @salt{1/4%tsp} and @pepper{1/4%tsp} and whisk well with a fork. Add the vegetables to the egg mixture and pour it into the #pan, sprinkle with cheese and place in the oven to bake for ~{7%minutes}. Take an #oven mitt{} and remove the pan from the oven, fold the omelette in half and place on a plate. Garnish with finely chopped fresh parsley and serve with a relish or chutney.

---

Ingredients: 1 eggs,40 g soba noodles,5 g green pepper,0.400 l chicken stock,50 g chicken fillets,some soy sauce
Recipe Text: Put a sauté pot on the stove and boil the eggs, then boil the soba noodles, following the instructions on the back of the package. The carrots for the broth can be cut into chunks and boiled till soft. Cut the green pepper into small rings. Put the casserole on the stove, pour chicken stock into the pot and bring to the boil, cut the chicken fillets into strips and boil in the stock for about 5 minutes, then add the chopped boiled carrots and boiled soba noodles to the stock. Pour the broth into a soup bowl, peel the boiled egg and slice in half, place into the soup, add the soy sauce to taste and garnish with green peppers.
Cooklang: Put a #sauté pot{} on the stove and boil the @eggs{1}, then boil the @soba noodles{40%g}, following the instructions on the back of the package. The carrots for the broth can be cut into chunks and boiled till soft. Cut the @green pepper{5%g} into small rings. Put the #casserole on the stove, pour @chicken stock{0.4%l} into the pot and bring to the boil, cut the @chicken fillets{50%g} into strips and boil in the stock for about ~{5%minutes}, then add the chopped boiled carrots and boiled soba noodles to the stock. Pour the broth into a soup bowl, peel the boiled egg and slice in half, place into the soup, add the @soy sauce{} to taste and garnish with green peppers.

---

Ingredients: 3 eggs,125 g flour,250 ml milk,1 pinch sea salt,some oil
Recipe Text: Crack the eggs into a blender, then add the flour, milk and sea salt, and blitz until smooth. Pour into a bowl and leave to stand for 15 minutes. Melt the butter (or a drizzle of oil if you want to be a bit healthier) in a large non-stick frying pan on a medium heat, then tilt the pan so the butter coats the surface. Pour in 1 ladle of batter and tilt again, so that the batter spreads all over the base, then cook for 1 to 2 minutes, or until it starts to come away from the sides. Once golden underneath, flip the pancake over and cook for 1 further minute, or until cooked through. Serve straightaway with your favourite topping.
Cooklang: Crack the @eggs{3} into a blender, then add the @flour{125%g}, @milk{250%ml} and @sea salt{1%pinch}, and blitz until smooth. Pour into a #bowl and leave to stand for ~{15%minutes}. Melt the butter (or a drizzle of @oil if you want to be a bit healthier) in a #large non-stick frying pan{} on a medium heat, then tilt the pan so the butter coats the surface. Pour in 1 ladle of batter and tilt again, so that the batter spreads all over the base, then cook for 1 to 2 minutes, or until it starts to come away from the sides. Once golden underneath, flip the pancake over and cook for 1 further minute, or until cooked through. Serve straightaway with your favourite topping.

---

Ingredients: {ingredients}

Recipe Text: {recipe text}

Reasoning: Let's think step by step in order to produce the cooklang. We need to identify and format each ingredient, cookware, and timer according to the Cooklang specification.

Cooklang: 
```

## Few-shot example without cooklang with ingredients

```

Convert plain recipe text with provided ingredients into Cooklang text format.
Return only Cooklang formatted recipe, dont return any other information. Return whole recipe in Cooklang format! Dont stop till you reach the end of the recipe.

---

Ingredients: 50 g ciabatta,some oil,,50 g cottage cheese,80 g smoked salmon,5 g capers,1 g dill,some lemon,some black pepper
Recipe Text: Slice the whole ciabatta loaf in half and then slice the halves lengthwise. Fry the ciabatta halves in a frying pan in a little oil, a griddle pan gives the best results and makes nice lines as the bread toasts. Spread the cottage cheese on the toasted ciabatta liberally, cut out the smoked salmon slices and place on the bread with a sprinkling of capers and finally chopped dill. Serve with a lemon wedge and freshly cracked black pepper.
Cooklang: Slice the whole @ciabatta{50%g} loaf in half and then slice the halves lengthwise. Fry the ciabatta halves in a #frying pan{} in a little @oil, a griddle pan gives the best results and makes nice lines as the bread toasts. Spread the @cottage cheese{50%g} on the toasted ciabatta liberally, cut out the @smoked salmon{80%g} slices and place on the bread with a sprinkling of @capers{5%g} and finally chopped @dill{1%g}. Serve with a @lemon wedge and freshly cracked @black pepper{}.

Ingredients: 0.500 avocado,100 g king prawns,some oil,some salt,,0.200 tsp thyme,0.200 tsp rosemary,1 glove garlic,20 g rocket salad leaves,30 g lime,some olive oil
Recipe Text: Cut the avocado in half, remove the stone and carefully peel off the skin. Cut the avocado into slices. A little lemon juice will prevent it going brown if necessary. Peel the king prawns, heat a frying pan over a medium heat with a little oil and sauté the prawns with the salt, thyme, rosemary and chopped garlic. Should you like chilli you can finely chop one chilli and add to the prawns. Arrange the avocado on a plate, top with the rocket salad leaves, place the prawns on the rocket salad and drizzle with lime juice and olive oil. This salad makes a lovely, light Summer lunch.
Cooklang: Cut the @avocado{1/2} in half, remove the stone and carefully peel off the skin. Cut the avocado into slices. A little lemon juice will prevent it going brown if necessary. Peel the @king prawns{100%g}, heat a #frying pan{} over a medium heat with a little @oil and sauté the prawns with the @salt, @thyme{1/5%tsp}, @rosemary{1/5%tsp} and chopped @garlic{1%glove}. Should you like chilli you can finely chop one chilli and add to the prawns. Arrange the avocado on a plate, top with the @rocket salad leaves{20%g}, place the prawns on the rocket salad and drizzle with @lime{30%g} juice and @olive oil{}. This salad makes a lovely, light Summer lunch.

Ingredients: 50 g courgette,0.333 tsp salt,some pepper,0.200 tsp thyme,200 g salmon steak,some salt.,50 g double cream,10 g horseradish,some salt,30 g cherry tomatoes,1 slice lemon
Recipe Text: Preheat the oven to 180 degrees. Cut a rectangular piece of parchment or baking paper. Wash the courgette and cut into 5 mm thick rounds. Place on the parchment, drizzle with olive oil and season with salt, pepper and chopped thyme. Place the salmon steak on top and season the fish with salt. Wrap the salmon and courgettes in the parchment to prevent drying out and place in the oven to bake for 15 minutes. While the fish is baking, make the sauce. Heat the double cream, horseradish and salt in a saucepan and simmer until thickened. Taste for further seasoning. Place the fish and courgettes on a plate, spoon the sauce over the top and garnish with the cherry tomatoes cut in half and a lemon wedge.
Cooklang: Preheat the oven to 180 degrees. Cut a rectangular piece of #parchment or baking paper. Wash the @courgette{50%g} and cut into 5 mm thick rounds. Place on the parchment, drizzle with olive oil and season with @salt{1/3%tsp} @pepper and chopped @thyme{1/5%tsp}. Place the @salmon steak{200%g} on top and season the fish with @salt. Wrap the salmon and courgettes in the parchment to prevent drying out and place in the oven to bake for ~{15%minutes}. While the fish is baking, make the sauce. Heat the @double cream{50%g}, @horseradish{10%g} and @salt in a #saucepan and simmer until thickened. Taste for further seasoning. Place the fish and courgettes on a plate, spoon the sauce over the top and garnish with the @cherry tomatoes{30%g} cut in half and a @lemon{1%slice} wedge.

---

Follow the following format.

Ingredients: Ingredients for the recipe. Comma separated list of ingredients.

Recipe Text: Recipe text to convert to Cooklang format.

Reasoning: Let's think step by step in order to ${produce the cooklang}. We ...

Cooklang: Cooklang formatted recipe.

---

Ingredients: 400 g water,60 g potatoes,30 g carrots,40 g salmon fillet,40 g hake fillet,30 g soy sauce,20 g fish sauce,20 g cherry tomatoes,5 g green peppers,50 g double cream

Recipe Text: Pour 400g of water into a saucepan and put on a medium heat. Peel and cut the potatoes (60g) into large pieces (if the potatoes are small with thin skin, you can simply rinse them and cut them in half without peeling), peel the carrots (30g) and cut them into smaller chunks. Place the vegetables into the pan and boil covered with a lid on until soft. Next, cut the salmon fillet (40g) and hake fillet (40g) into large pieces and add to the vegetables, add soy sauce (30g) and fish sauce (20g), halved cherry tomatoes (20g), chopped green peppers (5g) and double cream (50g). It is not necessary to cook for a long time, so as not to overcook the fish, it is enough to bring the soup gently to a boil.

Reasoning: Let's think step by step in order to Cooklang: Pour @water{400%g} into a #saucepan and put on a medium heat. Peel and cut the @potatoes{60%g} into large pieces (if the potatoes are small with thin skin, you can simply rinse them and cut them in half without peeling), peel the @carrots{30%g} and cut them into smaller chunks. Place the vegetables into the pan and boil covered with a lid on until soft. Next, cut the @salmon fillet{40%g} and @hake fillet{40%g} into large pieces and add to the vegetables, add @soy sauce{30%g} and @fish sauce{20%g}, halved @cherry tomatoes{20%g}, chopped @green peppers{5%g} and @double cream{50%g}. It is not necessary to cook for a long time, so as not to overcook the fish, it is enough to bring the soup gently to a boil.

Cooklang: Pour @water{400%g} into a #saucepan and put on a medium heat. Peel and cut the @potatoes{60%g} into large pieces (if the potatoes are small with thin skin, you can simply rinse them and cut them in half without peeling), peel the @carrots{30%g} and cut them into smaller chunks. Place the vegetables into the pan and boil covered with a lid on until soft. Next, cut the @salmon fillet{40%g} and @hake fillet{40%g} into large pieces and add to the vegetables, add @soy sauce{30%g} and @fish sauce{20%g}, halved @cherry tomatoes{20%g}, chopped @green peppers{5%g} and @double cream{50%g}. It is not necessary to cook for a long time, so as not to overcook the fish, it is enough to bring the soup gently to a boil.

---

Ingredients: {recipe text}

Recipe Text: {recipe text}

Reasoning: Let's think step by step in order to Cooklang: 

```