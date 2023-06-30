# Resume Parser using SpaCy and Streamlit

## Overview

This project is a resume parser built using SpaCy, a popular Natural Language Processing (NLP) library, and Streamlit, a Python web application framework. The goal of the project is to extract relevant information from resumes, such as personal information, skills, experience, and education details. The project utilizes a custom dataset consisting of 1014 resumes and leverages SpaCy's named entity recognition (NER) model, along with the RoBERTa base transformer model.

Deployed NLP(spacy) model link: https://huggingface.co/Yash-1124/en_resume_pipeline
## Features

- Extraction of personal information: The parser extracts personal information from the resumes, including names, contact details, and addresses.
- Skills extraction: The parser identifies skills mentioned in the resumes, providing insights into the applicant's technical abilities.
- Experience and education details: The parser extracts information about the applicant's work experience and educational background.

## Folder Structure

The project repository has the following structure:

- `main.py`: The main Python script that contains the Streamlit application code.
- `notebooks`: This directory contains a Jupyter notebook with the code used to train the SpaCy NER model on the custom dataset.
- `model`: This directory contains the trained SpaCy model.
- `requirements.txt`: A text file listing all the required dependencies for the project.
- `uploads/`: A folder to store the uploaded resumes for processing.
- `utils.py`: A utility module containing helper functions for text extraction and processing.
- `config`: A folder to store all configuration file for spacy models.
- `data` : A folder contains dataset containing 1014 resumes with annotations.

## Getting Started

To run the project locally, follow these steps:

1. clone the repository

```sh
git clone https://github.com/Yash-1511/Resume_Parser
```

2. Create virtual environment and active it

```sh
cd resume-parser
python -m venv env
source env/bin/activate  # For Unix/Linux
env\Scripts\activate  # For Windows
```
3. Install the project dependencies:

```sh
pip install -r requirements.txt
```

4. Run the Streamlit application:

```sh
streamlit run main.py
```

## Usage

Once the Streamlit application is running, you can use the following steps to parse resumes:

Choose the option for single or multiple PDFs in the sidebar.

- For a single PDF, click the "Choose your resume" button and select the desired resume file.
- For multiple PDFs, click the "Choose your resumes" button and select multiple resume files.

The parser will process the uploaded resumes and extract the relevant information.

For single PDF parsing, the extracted information will be displayed on the main page.

For multiple PDF parsing, the extracted information for each resume will be displayed on separate pages. Use the navigation buttons at the top to switch between resumes.

## References
- [Spacy](https://spacy.io/)
- [Streamlit](https://streamlit.io/)
- [OmkarPathak/pyresparser](https://github.com/OmkarPathak/pyresparser)

Note: The repository [OmkarPathak/pyresparser](https://github.com/OmkarPathak/pyresparser) was referenced for inspiration and general guidance in building this resume parser project.