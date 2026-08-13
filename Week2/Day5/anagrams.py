from anagram_checker import AnagramChecker

def main():
    checker = AnagramChecker("sowpods.txt")

    while True:
        word = input("Enter a word (or 'quit' to exit): ").strip()

        if word.lower() == 'quit':
            break

        if checker.is_valid_word(word):
            anagrams = checker.get_anagrams(word)
            print(f"Anagrams found: {anagrams}")
        else:
            print("Invalid word!")


if __name__ == "__main__":
    main()