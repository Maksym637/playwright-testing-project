from difflib import SequenceMatcher


# TODO
def are_strings_similar(string_1, string_2, threshold=0.5) -> bool:
    return SequenceMatcher(a=string_1, b=string_2).ratio() >= threshold
