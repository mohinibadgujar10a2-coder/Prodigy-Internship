import random
from collections import defaultdict

# Step 1: Read input text
with open(r"C:\Users\Dell\Desktop\TE\PRODIGY INFOTECH\TASK1\input.txt", "r") as file:
    text = file.read().lower()

# Step 2: Split text into words
words = text.split()

# Step 3: Build Markov Chain model
markov_chain = defaultdict(list)

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    markov_chain[current_word].append(next_word)

# Step 4: Generate text
def generate_text(start_word, length=15):
    current_word = start_word
    generated_text = [current_word]

    for _ in range(length - 1):
        next_words = markov_chain.get(current_word)
        if not next_words:
            break
        current_word = random.choice(next_words)
        generated_text.append(current_word)

    return " ".join(generated_text)

# Step 5: Run the generator
start = random.choice(words)
output = generate_text(start)

print("Generated Text:")
print(output)
