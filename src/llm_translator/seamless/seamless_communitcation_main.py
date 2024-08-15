import os
import json
from tqdm import tqdm
import torch
from seamless_communication.models.inference import Translator


# Initialize a Translator object with a multitask model, vocoder on the GPU.
translator = Translator("seamlessM4T_medium", "vocoder_36langs", torch.device("cuda:0"), torch.float16)



def translate(text):
    # try:
    translated_text, _, _ = translator.predict(text, "t2tt", "deu", src_lang="eng")
    return str(translated_text)




# @task()
def start_conversion(folder: str, file: str):
    tmp_dict = []
    # open the json file
    with open(f"{folder}/{file}", "r") as json_file:
        data = json.load(json_file)

        # i = 0
        for d in tqdm(data):
            instuction = translate(d["instruction"])
            input = translate(d["input"])
            output = translate(d["output"])

            # create new line in the tmp_dict
            tmp_dict.append( {
                "instruction": instuction,
                "input": input,
                "output": output,
                "instuction_org": d["instruction"],
                "input_org": d["input"],
                "output_org": d["output"]
            })

            # i += 1

            # only try 30 instructions
            # if i > 5:
                # break


    # save the translated json file format utf-8
    with open(f"de/deu-{file}", "w", encoding="utf-8") as json_file:
        json.dump(tmp_dict, json_file, ensure_ascii=False, indent=4)



# @flow(name="llm_translate")
def dataset_preprocessing(folder):
    i = 0
    for file in os.listdir(folder):
        print(f"start conversion of {file}")
        i += 1
        if i < 4:
            continue
        start_conversion(folder=folder, file=file)    

# run the flow!
dataset_preprocessing(folder="data/input")