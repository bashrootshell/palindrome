#!/usr/bin/env python3

from sys import argv

"""
    Finds palindromes greater than X characters.
    It also prints:
    - the size of the longest palindrome
    - the size of the shortest palindrome
    - the longest and the shortest palindromes
        of a given file.

    PEP8 compliant
    “Readability counts."
    “Beautiful is better than ugly.”
    — The Zen of Python
"""

all_palindromes = []  # stores all palindromes
str_size = argv[1]  # number of required characters
filename = argv[2]  # file to parse
counter_plus = 0  # counts palindromes with str_size or more
counter_exact = 0  # counts palindromes with exact str_size

if len(argv) > 2:

    with open(filename, 'r') as file:
        for string in file.read().split():
            if string == string[::-1]:
                all_palindromes.append(string)
            if string == string[::-1] and len(string) >= int(str_size):
                counter_plus += 1
            if string == string[::-1] and len(string) == int(str_size):
                counter_exact += 1

    longest_str = max(all_palindromes, key=len)
    shortest_str = min(all_palindromes, key=len)

    print(f'There are:\n'
          f'{counter_plus} palindromes with {str_size} characters or more\n'
          f'{counter_exact} palindromes with exact {str_size} characters\n'
          f'{len(all_palindromes)} palindromes total in file {filename}.\n')

    print(f'---> Longest palindrome: "{longest_str}" > '
          f'{len(longest_str)} characters.\n')

    print(f'---> Shortest palindrome: "{shortest_str}" > '
          f'{len(shortest_str)} characters.\n')

else:
    print('Usage: palindrome.py numberofchars filename\n'
          'Example: ./palindrome.py 15 filewithstrings.txt')
