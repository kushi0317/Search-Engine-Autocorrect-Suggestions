
# File: main.py

import csv
from trie import Trie
from suggestor import autocomplete
from corrector import correct_query

# Load dictionary
trie = Trie()
dictionary = []

with open("word_freq.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        word = row["word"].strip().lower()
        freq = int(row["frequency"])  # Change to 'count' if your CSV uses that
        trie.insert(word, freq)
        dictionary.append(word)

def main():
    while True:
        query = input("\nEnter your search query (or 'exit'): ").strip().lower()
        if query == "exit":
            break

        print("\n🔍 Autocomplete Suggestions:")
        suggestions = autocomplete(trie, query, k=5)
        for i, word in enumerate(suggestions, 1):
            print(f" {i}. {word}")

        print("\n🛠 Spell Correction Suggestions:")
        corrections = correct_query(dictionary, query, threshold=2, max_results=5)
        for i, word in enumerate(corrections, 1):
            print(f" {i}. {word}")

if __name__ == "__main__":
    main()