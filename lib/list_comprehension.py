#!/usr/bin/env python3


# Function that returns even elements from a list using list comprehension
def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

# Function that appends an exclamation mark to each sentence in the list using list comprehension
def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]
