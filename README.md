# PubMed Paper Fetcher

## Overview
This project is a Python program to fetch research papers from PubMed based on a user-specified query. The program identifies papers with at least one author affiliated with a pharmaceutical or biotech company and returns the results as a CSV file.

## Project Structure
```
takehome_problem/
├── src/
│   ├── __init__.py
│   ├── pubmed_fetcher.py
│   └── cli.py
├── tests/
│   └── test_pubmed_fetcher.py
├── poetry.lock
├── pyproject.toml
├── README.md
└── .gitignore
```

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/ADKWDHQWQHDQI/takehome_problem.git
    cd takehome_problem
    ```

2. Install dependencies using Poetry:
    ```
    poetry install
    ```

## Usage
To fetch papers and output the results to the console:
```
poetry run get-papers-list "your_query"
```

To fetch papers and save the results to a CSV file:
```
poetry run get-papers-list "your_query" -f results.csv
```

To display usage instructions:
```
poetry run get-papers-list -h
```

To print debug information during execution:
```
poetry run get-papers-list "your_query" -d
```

## Testing
Run the unit tests using the following command:
```
poetry run pytest
```

## Tools Used
- [PubMed API](https://www.ncbi.nlm.nih.gov/home/develop/api/)
- [Poetry](https://python-poetry.org/)
