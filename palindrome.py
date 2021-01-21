#!/usr/bin/env python3

from sys import argv

"""
    Finds palindromes greater than X characters.
    It also prints:
    - the size of the longest palindrome
    - the size of the shortest palindrome
    - the list of the longest and the shortest
    palindromes of a given file.

    PEP8 compliant
    “Readability counts."
    “Beautiful is better than ugly.”
    — The Zen of Python
"""


counter = 0
all_palindromes = []
str_size = argv[1]

if len(argv) > 2:

    with open(argv[2], 'r') as file:
        for string in file.read().split():
            if string == string[::-1]:  # compares with reversed string
                all_palindromes.append(string)
            if len(string) >= int(str_size) and string == string[::-1]:
                counter += 1

    longest_str = max(all_palindromes, key=len)
    shortest_str = min(all_palindromes, key=len)

    print(f'There are {counter} {str_size}+char_palindromes and '
          f'{len(all_palindromes)} total in file {argv[2]}.\n')

    print(f'--- Longest palindrome has: '
          f'{len(longest_str)} characters.\n')

    print(f'--- Shortest palindrome has: '
          f'{len(shortest_str)} characters.\n')

    print(f'--- Longest palindrome(s): {longest_str}\n')

    print(f'--- Shortest palindrome(s): {shortest_str}')

else:
    print('Usage: palindrome.py numberofchars filename\n'
          'Example: ./palindrome.py 15 filewithstrings.txt')
