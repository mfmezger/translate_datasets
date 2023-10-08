import os
import json
from tqdm import tqdm
from prefect import flow, task



def translate():
    # call the ollama rest service with the instruction
    pass




# @task()
def start_conversion(folder: str, file: str):+
    tmp_dict = {}
    # open the json file
    with open(f"{folder}/{file}", "r") as json_file:
        data = json.load(json_file)

        for d in data:
            pass




# @flow(name="llm_translate")
def dataset_preprocessing(folder):
    for file in tqdm(os.listdir(folder)):
        start_conversion(folder=folder, file=file)    

# run the flow!
dataset_preprocessing(folder="data/input")