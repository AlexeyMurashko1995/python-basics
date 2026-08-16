# ---------- Task 1 ----------


def get_word_lengths(words: list[str]) -> dict[str, int]:
    clean_dict = {}
    for word in words:
        if len(word) > 0:
            clean_dict[word] = len(word)
    return clean_dict


our_list = ["python", "fastapi", "", "sql", "python"]

print(get_word_lengths(our_list))