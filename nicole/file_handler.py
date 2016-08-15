import re

def get_tokens(text):
    stripped_text = text.rstrip('\n')
    return re.findall(r"[\w']+|[.,!?;]", stripped_text)

lines = [get_tokens(line) for line in open('training_data.txt')]