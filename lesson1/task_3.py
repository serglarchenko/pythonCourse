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
python_str = 'python'
special_symbols = ['.', ',', '-', '!', '\'', ' ', '\n']


def get_frequency_word_in_text(text, word):
    return print(f'The word {word} occurs {text.lower().count(word)} times!!')


def get_frequency_char_in_text(text):
    char_dict = dict()
    for i in text.lower():
        if i not in special_symbols:
            if i not in char_dict:
                char_dict[i] = 1
                continue
            char_dict[i] += 1
    max_key = max(char_dict.__iter__(), key=lambda k: char_dict[k])
    return print(f'Frequent char in the text is {max_key}, occurs {char_dict.get(max_key)} times')


get_frequency_word_in_text(source_text, python_str)

get_frequency_char_in_text(source_text)