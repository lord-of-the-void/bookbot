def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
    
    words = file_contents.split()
    word_count = len(words)
    
    char_count = count_characters(file_contents)
    
    print_report(path_to_file, word_count, char_count)

def count_characters(text):
    text = text.lower()
    char_dict = {}
    
    for char in text:
        if char.isalpha(): 
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    
    return char_dict

def print_report(file_path, word_count, char_count):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

if __name__ == "__main__":
    main()