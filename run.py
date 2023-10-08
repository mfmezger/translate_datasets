import pandas as pd 

# load json file
df = pd.read_json("final/deu-medical_meadow_mmmlu.json")

# convert to csv
df.to_csv("mmlu.csv", index=False)