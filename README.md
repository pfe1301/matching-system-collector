# Data Collection for Matching System

This Python script collects and stores descriptions for a list of entities using different data sources/strategies.
This README file outlines the data collection process for the matching system.

## Available strategies

### OpenAI

OpenAI provides a variety of natural language processing models that can be used for various tasks. For this matching system, we utilized OpenAI's GPT-3 model to generate text based on user inputs. The data from OpenAI is collected via their API, which provides access to the GPT-3 model.

### WriteSonic

WriteSonic is a platform that can generate SEO-friendly content.
We interact with this paltform using their API.

### DBPedia

DBpedia is a large-scale, multilingual knowledge graph that extracts structured information from Wikipedia and makes it available in a machine-readable format.
We obtain the URI of the entity from the DBpedia Lookup API. If a URI is found, we query the DBpedia SPARQL endpoint for the entity's description in the specified language.

## Get Started
### Installation
1. Clone the repository:

```bash
git clone https://github.com/pfe1301/matching-system-collector.git
```
2. Navigate to the cloned repository:

```bash
cd matching-system-collector
```

3. Install the required dependencies using `pip`:
```bash
pip install -r requirements.txt
```

### Usage
To run the script, you need to provide the following arguments:

+ `file`: File that contains entities to get the descriptions for.
+ `output`: Location of the output (without extension). Default is "../store/output"
+ `lang`: Specify the language. Default is "en". "fr" is also supported.
+ `type`: Entities types. Default is "job".
+ `strategy`: The strategy of data collection (data source). Default is "writesonic".
+ `chunk`: The number of entities to store in a single file. Default is 100.
+ `startindex`: The index of the entity to start from. Default is 0.
+ `endindex`: The index of the entity to end at. Default is -1 (in this case ```endindex==len(entities)```).

Example:
```bash
python src/main.py data/job_titles.txt -o store/jobs_output -l fr -t job -s openai --chunk 100 --startindex 0 --endindex 200
```
This will collect the descriptions for the 200 first job titles from `data/job_titles.txt` and stores it in 2 chunks in `store/job_output0.json` and `store/job_output1.json` .


## Repo organization

The codebase is structured as follows:

### data

This folder contains the `entities.txt` file that we collect textual descriptions about.

### src

This folder contains the scripts and CLI script to interact with the APIs

### store

This folder contains the output file(s) of the scripts

### tests

This folder contains the test cases for unit testing.

*Note*: The tests are under development