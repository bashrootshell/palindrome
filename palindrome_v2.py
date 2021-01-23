#!/usr/bin/env python3

from sys import argv
import string

"""
    Version 2: faster than version 1 (it now uses a list to
    store all palindromes and to count ocurrences)
    The program will remove all punctuation from file.
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

    all_palindromes = []  # stores all palindromes
    str_size = argv[1]  # number of required characters
    filename = argv[2]  # file to parse
    counter_plus = 0  # counts palindromes with str_size or more
    counter_exact = 0  # counts palindromes with exact str_size
    rm_punct = str.maketrans('', '', string.punctuation)  # faster than join

    with open(filename, 'r') as file:
        for line in file.read().split():
            string = line.translate(rm_punct)
            if string == string[::-1]:
                all_palindromes.append(string)

    #  extracts the longest and the shortest palindromes (string)
    longest_str = max(all_palindromes, key=len)
    shortest_str = min(all_palindromes, key=len)

    #  compares initial str_size with the shortest and longest palindromes
    #  and forces counters to zero since there are no palindromes with
    #  those sizes (shorter than shortest_str / longer than longest_str)
    if int(str_size) < len(shortest_str) or int(str_size) > len(longest_str):
        counter_plus = counter_exact = 0
    else:
        for palindrome in all_palindromes:
            if len(palindrome) >= int(str_size):
                counter_plus += 1
            if len(palindrome) == int(str_size):
                counter_exact += 1

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
