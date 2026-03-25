from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "give a story on for each style of for loop so that 7th standard kids can understand the concept of for loop in programming"

result = generator(
    prompt,
    max_new_tokens=100,
    do_sample=True,
    temperature=0.7,
    top_k=50,
    top_p=0.9,
    repetition_penalty=1.2
)

# Extract only generated part (remove prompt)
generated_text = result[0]['generated_text'].replace(prompt, "")

print("Scene:", generated_text.strip())