import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_md", disable=[
                 "lemmatizer", "attribute_ruler", "textcat"])
