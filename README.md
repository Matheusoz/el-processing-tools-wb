
# Text Processing Module

This module encompasses the entire implementation for an array of text preprocessing and cleaning pipelines. Flexibility in configuration is a key characteristic of the cleaning architecture, made possible through config files, for instance, [`configs/cleaning/default.yml`](configs/cleaning/default.yml).

## Submodules

### Preprocessing and Cleaning of Documents

We create purpose-driven modules for preprocessing and cleaning aimed at efficiently handling the raw data mainly composed of PDF and text documents. These modules' output becomes a refined and high-quality input for our models.

The pipeline largely consists of the following steps:
- Text extraction from pdf
- Sentence tokenization
- Lemmatization and stop words removal
- Purging all tokens that aren't alphabetical 
- Implementation of spell check to identify and correct misspelled words
- Token normalization via lowercase conversion

### Phrase Detection

Logical grouping of tokens into phrases to uphold their intrinsic meaning is a crucial part of preprocessing. We primarily use the [Gensim](https://radimrehurek.com/gensim/) NLP toolkit and Spacy for developing our phrase detection algorithms.

### Acronym Detection

Documentation in development organizations and multilateral development banks commonly contain acronyms. Hence, in this project, we have added an acronym detection and expansion subroutine to our pipeline. The subroutine is designed to spot acronyms within the document and replace them with their fully expanded counterparts. Each occurrence of the acronym is kept track of and prototypes encoding the acronym's information are generated.