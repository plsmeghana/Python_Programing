def group_anagrams_no_dict(words):
    result = []
    keys = []

    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in keys:
            index = keys.index(sorted_word)
            result[index].append(word)
        else:
            keys.append(sorted_word)
            result.append([word])

    return result

# Test
words = ["listen", "silent", "enlist", "hello", "below", "elbow"]
print(group_anagrams_no_dict(words))
