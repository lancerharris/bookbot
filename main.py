def sort_on(dict):
    return dict["count"]

def unique_characters(text_string):
    if len(text_string) == 0:
        return
    unique_characters = {}
    for char in text_string:
        char = char.lower()
        if char not in unique_characters.keys():
            unique_characters[char] = 1
        else:
            unique_characters[char] += 1
    return unique_characters

def get_file_contents(file_path):
    with open(file_path) as f:
        return f.read()

def get_char_count(text):
    return len(text.split())

def char_dict_to_sorted_list(char_dict, sort_func):
    dict_list = []
    for key in char_dict.keys():
        if key.isalpha():
            dict_list.append({"char": key, "count": char_dict[key]})
    dict_list.sort(reverse=True, key=sort_func)
    return dict_list


def main():
    file_contents = get_file_contents("./books/frankenstein.txt")

    print("--- Begin Report of books/frankenstein.txt")
    print(f"{len(file_contents.split())} words were found in the document.")
    print("\n")

    unique_chars = unique_characters(file_contents)
    character_dict_list = char_dict_to_sorted_list(unique_chars, sort_on)

    for char_dict in character_dict_list:
            print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")

    print("\n")
    print("--- End of Report ---")

main()
