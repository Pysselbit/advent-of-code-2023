# Advent of Code 2023
# Day 15-1: Lens Library

def hash(string):
    hash = 0

    for char in string:
        hash += ord(char)
        hash *= 17
        hash %= 256

    return hash

with open("input.txt") as file:
    sum = 0

    for command in file.read().strip().split(","):
        sum += hash(command)

    print(sum)