from collections import defaultdict


def group_anagrams(words):
    dfdict = defaultdict(list)
    for word in words:
        sort_word = " ".join(sorted(word))
        dfdict[sort_word].append(word)
    return dfdict.values()


words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))
