#!/usr/bin/env python3

from sys import argv

"""
    Version 3: as fast as version 2
    (it now uses list comprehensions to store
    all palindromes in a tuple and count occurrences).
    Finds palindromes greater than X characters.
    It also prints:
    - the size of the longest palindrome
    - the size of the shortest palindrome

    PEP8 compliant
    “Readability counts."
    “Beautiful is better than ugly.”
    — The Zen of Python
"""

if len(argv) > 2:

    all_palindromes = ()  # tuple stores all palindromes
    str_size = argv[1]  # number of required characters
    filename = argv[2]  # file to parse
    counter_plus = 0  # counts palindromes with str_size or more
    counter_exact = 0  # counts palindromes with exact str_size

    with open(filename, 'r') as file:
        lines = file.read().split()
        all_palindromes = list(filter(lambda str: str == str[::-1], lines))

    #  extracts the longest and the shortest palindromes (string)
    longest_str = max(all_palindromes, key=len)
    shortest_str = min(all_palindromes, key=len)

    #  compares initial str_size with the shortest and longest palindromes
    #  and forces counters to zero, since there are no palindromes with
    #  those sizes (shorter than shortest_str - longer than longest_str)
    if int(str_size) < len(shortest_str) or int(str_size) > len(longest_str):
        counter_plus = counter_exact = 0
    else:
        #  walrus := taking place here :)
        [counter_plus := counter_plus + 1 for pp in all_palindromes
         if len(pp) >= int(str_size)]
        [counter_exact := counter_exact + 1 for pp in all_palindromes
         if len(pp) == int(str_size)]

    print(f'There are:\n'
          f'{counter_plus} palindromes with {str_size} or more characters\n'
          f'{counter_exact} palindromes with exact {str_size} characters\n'
          f'{len(all_palindromes)} palindromes total in file {filename}\n')

    print(f'---> Longest palindrome: "{longest_str}" > '
          f'{len(longest_str)} characters.\n')

    print(f'---> Shortest palindrome: "{shortest_str}" > '
          f'{len(shortest_str)} characters.\n')

else:
    print('Usage: palindrome.py numberofchars filename\n'
          'Example: ./palindrome.py 15 filewithstrings.txt')
