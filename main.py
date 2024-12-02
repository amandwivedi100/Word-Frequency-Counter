from collections import Counter
import re

def get_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text: str = text.lower()
    words: list[str] = re.findall(r'\b\w+\b', lowered_text)
    words_counts: Counter = Counter(words)
    return words_counts.most_common()

def read_file(file_path: str)  -> str:
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("file not found")
        return ""

def main() -> None:
    choice: str = input("Enter 'file' if you want to input from a file or 'text' to enter the words manually:  ").strip().lower()

    if choice == 'file':
        file_path = input("Enter the file path: ").strip()
        text = read_file(file_path)
        if not text:
            return
    else:
        text = input("Enter text: ").strip()
    word_frequencies: list[tuple[str, int]] = get_frequency(text)
    for word, count in word_frequencies:
        print(f'{word}: {count}')

if __name__ == '__main__':
    main()
