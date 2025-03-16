def main():
    from stats import word_count, letter_count, report
    import sys

    def get_book_text(path):
        with open(path) as f:
            return f.read()

    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    else:

        book_path = sys.argv[1]
        text = get_book_text(book_path)
    
        num_words = word_count(text)
        num_letters = letter_count(text)
        sorted_letters = report(num_letters)
        
        # Now print the formatted report according to the instructions
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        
        # Print each letter and its count, but only for alphabetical characters
        for char_dict in sorted_letters:
            char = char_dict["letter"]
            if char.isalpha():  # Only print alphabetical characters
                print(f"{char}: {char_dict['num']}")
        
        print("============= END ===============")


main()