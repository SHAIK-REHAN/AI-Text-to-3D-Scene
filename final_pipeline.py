from transformers import pipeline
import spacy

# -------- LOAD MODELS --------
nlp = spacy.load("en_core_web_sm")
generator = pipeline("text-generation", model="gpt2")

# -------- INPUT --------
user_input = input("Enter paragraph: ")

# -------- GPT-2 SIMPLE PROMPT --------
prompt = f"Describe this as a simple visual scene: {user_input}"

result = generator(
    prompt,
    max_new_tokens=30,
    do_sample=True,
    temperature=0.5,
    top_k=40,
    top_p=0.9
)

generated_text = result[0]['generated_text']
generated_text = generated_text.replace(prompt, "").strip()

# -------- SMART MERGE LOGIC --------
bad_words = ["rule", "text", "scene", "describe", "use"]

if len(generated_text.split()) < 3:
    final_text = user_input

elif any(word in generated_text.lower() for word in bad_words):
    final_text = user_input

elif "dog" in generated_text.lower() and "boy" in user_input.lower():
    # GPT changed meaning → reject
    final_text = user_input

else:
    # Merge both (best case)
    final_text = user_input + ". " + generated_text

print("\n--- FINAL TEXT USED ---")
print(final_text)

# -------- NLP PROCESS --------
doc = nlp(final_text)

sentences = [sent.text for sent in doc.sents]

all_scenes = []
all_mapped_scenes = []

# -------- MAPPING --------
object_map = {
    "boy": "human_model",
    "football": "ball_model",
    "dog": "dog_model"
}

environment_map = {
    "park": "park_scene",
    "road": "road_scene"
}

action_map = {
    "playing": "play_animation",
    "running": "run_animation",
    "walking": "walk_animation",
    "sitting": "sit_animation"
}

# -------- PROCESS EACH SENTENCE --------
for sent in sentences:
    doc = nlp(sent)

    objects = []
    actions = []
    environment = []

    for token in doc:
        if token.pos_ == "NOUN" and token.dep_ in ["nsubj", "dobj"]:
            objects.append(token.text.lower())

        if token.pos_ == "VERB":
            actions.append(token.lemma_.lower())
        if token.dep_ == "pobj" or token.text.lower() in ["park", "road", "street", "room"]:
            environment.append(token.text.lower())
    # -------- FILTER BAD WORDS --------
    invalid_words = ["idea", "something", "thing", "anything"]

    objects = [obj for obj in objects if obj not in invalid_words]
    environment = [env for env in environment if env not in invalid_words]

    # Keep only useful actions
    valid_actions = ["playing", "running", "walking", "sitting", "jumping"]

    actions = [act for act in actions if act in valid_actions]

    # Remove duplicates
    objects = list(dict.fromkeys(objects))
    actions = list(dict.fromkeys(actions))
    environment = list(dict.fromkeys(environment))

    # Remove environment words from objects
    objects = [obj for obj in objects if obj not in environment]

    scene = {
        "objects": objects,
        "actions": actions,
        "environment": environment
    }

    all_scenes.append(scene)

    mapped_scene = {
        "models": [object_map.get(obj, obj) for obj in scene["objects"]],
        "environment": [environment_map.get(env, env) for env in scene["environment"]],
        "actions": [action_map.get(act, act) for act in scene["actions"]]
    }

    all_mapped_scenes.append(mapped_scene)

# -------- OUTPUT --------
print("\n--- ALL NLP SCENES ---")
for i, scene in enumerate(all_scenes, 1):
    print(f"Scene {i}: {scene}")

print("\n--- ALL 3D MAPPED SCENES ---")
for i, mapped in enumerate(all_mapped_scenes, 1):
    print(f"Scene {i}: {mapped}")