def count_words(text):
    split_words = text.split()
    return len(split_words)

def count_chars(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_on(item):
    return item["num"]

def sort_character(char_dict):
    result = []
    for char, count in char_dict.items():
        if char.isalpha():
            result.append({"char": char, "num": count})
    result.sort(reverse=True, key=sort_on)
    return result
