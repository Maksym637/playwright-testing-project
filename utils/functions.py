"""Module representing some helper functions"""

from difflib import SequenceMatcher


def are_strings_similar(string_1: str, string_2: str, threshold: float = 0.9) -> bool:
    """
    Determines whether two strings are similar based on a similarity ratio

    Args:
        string_1 (str): The first string to compare
        string_2 (str): The second string to compare

    Returns:
        bool: True if the similarity ratio is greater than or equal to the threshold,
              otherwise False
    """
    return SequenceMatcher(a=string_1, b=string_2).ratio() >= threshold
