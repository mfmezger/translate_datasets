from pathlib import Path
from langchain_google_vertexai import ChatVertexAI
from langchain_core.prompts import PromptTemplate

save_json_file = "data/de/medical_meadow_mediqa.json"


gemini =  ChatVertexAI(
        model_name="gemini-flash-001",
        location="europe-west3",
        temperature=0,
        convert_system_message_to_human=True,
        streaming=False,
        max_output_tokens=3000,
    )

def main():

    # figure out what would be the best async approach for that.
    prompt_template = PromptTemplate("""Nachfolgend erhältst du einen englischen Text. Deine Aufgabe ist es, diesen Text auf Deutsch zu übersetzen. Bei deiner Übersetzung legst du größten Wert auf hohe Sprachqualität. Du achtest auf semantische Richtigkeit, korrekte Grammatik, Rechtschreibung und Tonalität. Sprachen abweichend von Englisch, Eigenwörter, mathematische Formeln und Code belässt du im Original.
    
    Originaler Text: {original_text}. Übersetzung:""")

    chain = prompt_template | gemini

    json_file_path = Path("data/input/medical_meadow_mediqa.json")

    # load the json dataset
    with json_file_path.open() as f:
            data = json.load(f)

    messages = [{"original_text": i["instruction"]} for i in data]

    instruction_responses = batch_chain.batch(messages)

    messages = [{"original_text": i["input"]} for i in data]

    input_responses = batch_chain.batch(messages)

    messages = [{"original_text": i["output"]} for i in data]

    output_responses = batch_chain.batch(messages)

    final = [{
            "instruction": instruction_responses[i],
            "input": input_responses[i],
            "output": output_responses[i],} for i in range(len(data))]


    # create and save json
    with save_json_file.open("w") as file:
        json.dump(final, file, indent=4)







if __name__ == "__main__":
    main()