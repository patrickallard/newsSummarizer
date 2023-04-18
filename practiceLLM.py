import torch
import os
from transformers import (pipeline, AutoModelForSeq2SeqLM, AutoTokenizer)

model_name = "philschmid/bart-large-cnn-samsum"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
# tokenizer maxes out at 1024 tokens. May need to find a way to truncate scrapped data or increase maximum number of tokens
tokenizer = AutoTokenizer.from_pretrained(model_name, model_max_length = 1024)
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

files = []
summary = []
abstract = []
for filename in os.listdir("."):
    if os.path.isfile(filename) and "politico_" in filename:
        files.append(filename)
# loop through all files and summarize each one
for file in files:
    f = open(file, "r", encoding="utf8")
    to_tokenize = f.read()
    # might be worth it to insert a read function that counts the number of tokens in file, that way, max_length is calculated dynamically
    summerized = summarizer(to_tokenize, min_length=75, max_length=300, do_sample=False)
    # extracts the value from the key:value pair that is stored in a list of a list
    summary.append(summerized[0].get('summary_text'))
    os.remove(file) 

# TODO: write an algo that generates an abstract of the list of summaries (i.e strings)
summerized = summarizer(summary,min_length=70, max_length=300, do_sample=False)
abstract.append(summerized)
print(abstract)