import spacy

nlp = spacy.load("en_core_web_sm")

text = "A boy is playing football in a park"

doc = nlp(text)

objects = []
actions = []
environment = []

for token in doc:
    if token.pos_ == "NOUN":
        objects.append(token.text)

    if token.pos_ == "VERB":
        actions.append(token.text)

for token in doc:
    if token.dep_ == "pobj":
        environment.append(token.text)

# Remove environment from objects
objects = [obj for obj in objects if obj not in environment]

# Create structured output
scene = {
    "objects": objects,
    "actions": actions,
    "environment": environment
}

print(scene)