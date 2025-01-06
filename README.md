# Project
Evaluating Large Language Models for Recipe Conversion. Code repository for the project.

![flow](./plots/flow.png)

## Results

### Results by model

![Model comparison](./plots/standard_model_comparison.png)

### Results by prompt technique

![Model comparison](./plots/standard_prompt_technique_analysis.png)

## Prompt examples


- **[Few-shot example with cooklang with ingredients](./examples/few-shot-no-cooklang-with-ings.txt)** (default and best performing prompt)
- [Few-shot example without cooklang with ingredients](./examples/few-shot-no-cooklang-with-ings.txt) (example without cooklang specification)
- [MIPROv2 with cooklang with ings prompt example](./examples/miprov2-with-cooklang-with-ings.txt) (example of MIPROv2 prompt)


## Results table (WER, ROUGUE-L, TER)

(TODO)

### Results table (Ingredient Identification, Amount Identification, Unit Identification)

[Table](./examples/specific-metrics-results.md)

## Setup

### Prerequisites

- Python 3.12

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/williambrach/llm-text2cooklang.git
   cd llm-text2cooklang
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

0. The `program.py` contains:
   - Dspy classes for all programs and signatures
   - Util functions for loading programs 

1. The `pycooklang.ipynb` notebook will:
   - Parse the input dataset
   - Create examples for training
   - Train and optimize various models (Llama, Azure OpenAI)
   - Save the optimized programs in the `data/programs/` directory

2. The `predict.ipynb` notebook will:
   - Load and parse the input dataset from a TSV file
   - Set up language models (Azure OpenAI or Ollama) based on environment variables
   - Load optimized programs from JSON files in the `data/programs/` directory
   - Prepare to generate CookLang predictions for each recipe using the loaded programs
   - Cooklang prediction into CSV output

3. The `eval.ipynb` notebook will:
   - Load and process evaluation data from TSV files
   - Calculate various metrics (WER, ROUGE-L, TER) on the predictions
   - Evaluate ingredient, unit, and amount accuracy
   - Generate visualizations comparing model performance across different metrics
   - Save the resulting plots in the `plots/` directory



## Citation

```shell
```
