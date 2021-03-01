source_text = """Python is an interpreted high-level programming language for general-purpose programming. Created by
 Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability,
  notably using significant whitespace. It provides constructs that enable clear programming on both small and large 
  scales. In July 2018, the creator Guido Rossum stepped down as the leader in the language community after 30 years.
Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms,
 including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.
Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open 
source software and has a community-based development model, as do nearly all of Python's other implementations. Python
 and CPython are managed by the non-profit Python Software Foundation. Привет из Харькова!
"""
python_str = 'Python'


def char_to_list(str):
    return [char for char in str.casefold() if char.isalnum()]


def get_frequency_char(list_of_characters):
    freq_key = ''
    freq_value = 0
    for key, value in list_of_characters.items():
        if value > freq_value:
            freq_value = value
            freq_key = key
    return print(f'Frequency char is {freq_key} : {freq_value}')


def count_char_in_list(char_list):
    char_dict = {}
    for i in char_list:
        keys = char_dict.keys()
        if i in keys:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict


def get_frequency_word(initial_str, word_for_count):
    count_word = 0
    list_of_words = initial_str.split()
    for i in list_of_words:
        if i.__contains__(word_for_count):
            count_word += 1
    return print(f"The word {word_for_count} occurs {count_word} times")


list_char = char_to_list(source_text)
count_char = count_char_in_list(list_char)
get_frequency_char(count_char)

get_frequency_word(source_text, python_str)
