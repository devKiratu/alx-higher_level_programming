#!/usr/bin/python3
"""contains function that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """prints text with two lines added after ., ? and :
        Args:
            text: string to print
        Raises:
            TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    found = False
    for c in text:
        if found and c == ' ':
            continue
        if c == '.' or c == '?' or c == ':':
            print("{}".format(c))
            print()
            found = True
        else:
            print("{}".format(c), end="")
            found = False
