def text_to_word_count(book_text):
    """Returns the number of words in the given book text."""
    words = book_text.split()
    return len(words)

def characters_in_a_string(book_text):
    """Returns a dictionary with the frequency of each character in the given text."""
    book_text = book_text.lower()  # Convert text to lowercase
    char_count = {}  # Initialize dictionary

    for char in book_text:  
        if char in char_count:
            char_count[char] += 1  # Increment count if exists
        else:
            char_count[char] = 1  # Initialize count
    
    return char_count

def sorted_character_frequencies(char_count):
    """
    Takes a dictionary of character counts and returns a sorted list of dictionaries.
    Each dictionary contains a character and its count, sorted from greatest to least.
    Non-alphabetical characters are ignored.
    """
    sorted_list = [
        {"character": char, "count": count}
        for char, count in char_count.items() if char.isalpha()  # Only include letters
    ]
    
    # Sort list by count in descending order
    sorted_list.sort(key=lambda x: x["count"], reverse=True)
    
    return sorted_list

