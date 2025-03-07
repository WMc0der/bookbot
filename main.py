import sys
from stats import text_to_word_count, characters_in_a_string, sorted_character_frequencies

def get_book_text(path):
    """Reads and returns the content of the book file."""
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        sys.exit(1)

def main():
    # Ensure correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the book path from command-line arguments
    book_path = sys.argv[1]

    # Display header
    print("=" * 28)
    print("           BOOKBOT           ")
    print("=" * 28)
    print(f"Analyzing book found at {book_path}...")

    # Read the book text
    book_text = get_book_text(book_path)

    # Count words
    word_count = text_to_word_count(book_text)

    # Count characters
    char_count = characters_in_a_string(book_text)

    # Get sorted character frequencies
    sorted_chars = sorted_character_frequencies(char_count)

    # Print word count section
    print("-" * 28)
    print("        Word Count         ")
    print("-" * 28)
    print(f"Found {word_count} total words")

    # Print character count section
    print("-" * 28)
    print("      Character Count      ")
    print("-" * 28)
    for entry in sorted_chars:
        print(f"{entry['character']}: {entry['count']}")

    # Display footer
    print("=" * 28)
    print("            END            ")
    print("=" * 28)

# Run the script
if __name__ == "__main__":
    main()

