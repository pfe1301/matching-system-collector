## Data Collection for Matching System

This README file outlines the data collection process for the matching system, which sources data from OpenAI and WriteSonic.

### OpenAI

OpenAI provides a variety of natural language processing models that can be used for various tasks. For this matching system, we utilized OpenAI's GPT-3 model to generate text based on user inputs. The data from OpenAI is collected via their API, which provides access to the GPT-3 model.

### WriteSonic

WriteSonic is a platform that can generate SEO-friendly content.
We interact with this paltform using their API.


### Repo organization

The codebase is structured as follows:

#### data

This folder contains the `entities.txt` file that we collect textual descriptions about.

#### src

This folder contains the scripts and CLI script to interact with the APIs

#### store

This folder contains the output file(s) of the scripts

#### tests

This folder contains the test cases for unit testing.

*Note*: The tests are under development