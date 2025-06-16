
def damerau_levenshtein(s1, s2):
    d = {}
    len1, len2 = len(s1), len(s2)

    for i in range(-1, len1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, len2 + 1):
        d[(-1, j)] = j + 1

    for i in range(len1):
        for j in range(len2):
            cost = 0 if s1[i] == s2[j] else 1
            d[(i, j)] = min(
                d[(i-1, j)] + 1,
                d[(i, j-1)] + 1,
                d[(i-1, j-1)] + cost
            )
            if i > 0 and j > 0 and s1[i] == s2[j-1] and s1[i-1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[(i-2, j-2)] + cost)

    return d[(len1-1, len2-1)]

def correct_query(dictionary_words, query, threshold=2, max_results=5):
    candidates = []
    for word in dictionary_words:
        distance = damerau_levenshtein(query, word)
        if distance <= threshold:
            candidates.append((distance, word))
    candidates.sort()
    return [word for _, word in candidates[:max_results]]