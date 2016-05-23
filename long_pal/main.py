"""
Find the longest palindrome in the string
"""

from argparse import ArgumentParser


def longest_subpalindrome_slice(text):
    """
    Return (i, j) such that text[i:j] is the longest palindrome in text.
    """
    max_length = 0
    longest = (0, 0)
    text = text.lower()

    for i, _ in enumerate(text):
        current_length = 0
        j = 1

        try:
            while text[i - j] == text[i + j] and i - j >= 0:
                j += 1
                current_length += 1
            if text[i] == text[i + 1] and not current_length:
                current_length = 1
                longest = (i, i + 2)
            elif text[i] == text[i - 1] and not current_length:
                current_length = 1
                longest = (i - 1, i + 1)
        except IndexError:
            pass

        if current_length > max_length:
            max_length = current_length
            longest = (i - max_length, i + max_length + 1)
    return longest


def arg_parse():  # pragma: no cover
    """
    Parse console arguments
    """
    parser = ArgumentParser(description="Finds the longest palindrome")
    parser.add_argument("text", action="store")
    args = parser.parse_args()
    text = args.text
    return text


def main():  # pragma: no cover
    """
    Prints the result to a console
    """
    text = arg_parse()
    result = longest_subpalindrome_slice(text)
    print(result)

if __name__ == '__main__':  # pragma: no cover
    main()
