def print_upper_words(words,must_start_with):
    """Capitilizes words that must_start_with said letters"""
    for word in words:
        for letter in must_start_with: 
            if word.startswith(letter):
                print(word.upper())
                break

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})