from re import escape


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_text(book_path)
    total = count(book_text)
    freq = get_character_frequency(book_text)
    report(book_path, total, freq)


def report(path, count, freq):
    print(f"--- Begin report of {path} ---")
    print(f"{count} words found in the document")

    for word in freq:
        escaped_word = word.encode("unicode_escape").decode("utf-8")
        total = freq[word]
        times = "times"
        if total == 1:
            times = "time"

        print(f"The '{escaped_word}' character was found {total} {times}")

    print("--- End report ---")


def get_character_frequency(text):
    frequency = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in frequency:
            frequency[lower_char] += 1
        else:
            frequency[lower_char] = 1

    return frequency


def get_text(path):
    with open(path) as f:
        return f.read()


def count(text):
    return len(text.split())


if __name__ == "__main__":
    main()
