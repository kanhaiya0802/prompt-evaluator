import json

def load_prompt():
    with open("prompts/evaluation_prompt.txt", "r", encoding="utf-8") as file:
        return file.read()

def parse_response(response):
    response = response.replace("```json", "")
    response = response.replace("```", "")
    return json.loads(response)