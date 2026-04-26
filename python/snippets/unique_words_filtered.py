# get unique words in from input
import argparse


def sanitize(words):
    # TODO
    return True

def main(words: str):
    # Return the unique words sorted in a string
    split_words = words.split(",")
    split_words.sort()
    unique_words = []
    for word in split_words:
        word = word.strip()
        if word not in unique_words:
            unique_words.append(word)
    return ", ".join(unique_words)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Get Unique Sorted Words",
        description="""
        Return a string of the unique words in a sorted order.
        Assumes input is a single string of comma seperated words
        """)
    parser.add_argument('-i', '--input_string')
    args = parser.parse_args()
    # import pdb;pdb.set_trace()
    print('=' * 20)
    print(main(args.input_string))
