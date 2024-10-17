def count_words(string):
    words = string.split()
    return len(words)

    
def count_chars(string):
    chars_dict = {}
    for char in string:
       char = char.lower()
       if char in chars_dict:
            chars_dict[char] += 1
       else:
            chars_dict[char] = 1
    return chars_dict 


def main():
    file = "books/frankenstein.txt"
    content = None
    with open(file) as f:
        content = f.read()
    
    print(f"--- Begin report of {file} ---")
    print(f"{count_words(content)} words found in the document")
    print()

    for char, count in count_chars(content).items():
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")
    
    
    
main()
    