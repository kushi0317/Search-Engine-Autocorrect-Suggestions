# 🔍 Search Autocomplete & Spell Corrector

A Python-based CLI project that provides real-time autocomplete suggestions and autocorrect capabilities using:
- ✅ Trie Data Structure
- ✅ DFS + Heap for Top-K autocomplete
- ✅ Damerau-Levenshtein Distance for typo correction

---

## 📁 Project Structure
```
search-autocomplete/
│
├── trie.py                 # Trie and TrieNode implementation
├── suggestor.py           # Autocomplete logic with DFS + Min-Heap
├── corrector.py           # Damerau-Levenshtein distance-based autocorrect
├── main.py                # CLI interface to test autocomplete and correction
├── word_freq.csv          # Sample dictionary with word frequencies
└── README.md              # You're here!
```

---

## ⚙️ Setup Instructions

1. **Clone the Repository**
```bash
https://github.com/yourusername/search-autocomplete.git
cd search-autocomplete
```

2. **Prepare the Dictionary File**
Ensure `word_freq.csv` exists with the format:
```csv
word,frequency
hello,1000
help,950
hero,600
...
```

3. **Run the Application**
```bash
python main.py
```

---

## ✨ Features

### 🔡 Autocomplete:
- Based on Trie traversal and frequency-ranked DFS
- Returns top-5 suggestions sorted by popularity

### 🔁 Autocorrect:
- Uses Damerau-Levenshtein to catch common typing errors
- Suggests close matches within edit distance of 2

---

## 🧪 Example
```
Enter your search query (or 'exit'): her

🔍 Autocomplete Suggestions:
 1. hero
 2. herb
 3. herd

🛠 Spell Correction Suggestions:
 1. her
 2. here
 3. hers
```

---

## 🧠 Concepts Used
- Trie (prefix tree)
- DFS for prefix completion
- Min-Heap for top-K sorting
- Damerau-Levenshtein edit distance

---

## 📜 License
MIT License © Your Name
