import json
import os
from string import Template

PROMPT_DIR = os.path.join(os.path.dirname(__file__), "prompts")

def load_prompt(name):
    filepath = os.path.join(PROMPT_DIR, f"{name}.json")
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Prompt '{name}' không tồn tại.")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["template"]

def fill_prompt(template_str, variables: dict):
    template = Template(template_str)
    return template.safe_substitute(variables)
