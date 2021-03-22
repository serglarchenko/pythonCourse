import re

initial_string = """ Из 35 футболистов, забивших как минимум 7 голов на чемпионатах мира, только у троих футболистов 
средний показатель превышает 2 гола за игру. Эти 35 игроков представляют 14 футбольных сборных"""


def my_func(text_, multiplier_=2):
    return print(re.sub(r'\d+', repl(multiplier_), text_))


def repl(mult):
    return lambda digit: str(int(digit.group(0)) * mult)


my_func(initial_string)
