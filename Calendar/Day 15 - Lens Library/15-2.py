# Advent of Code 2023
# Day 15-2: Lens Library

import re

OPERATION_ADD = "="
OPERATION_REMOVE = "-"


class Command:
    def __init__(self, input):
        self.label = re.match("[a-z]+", input).group()

        if OPERATION_ADD in input:
            self.operation = OPERATION_ADD
            self.focal_length = int(re.findall(r"\d+", input)[0])
        else:
            self.operation = OPERATION_REMOVE


class Lens:
    def __init__(self, label, focal_length):
        self.label = label
        self.focal_length = focal_length


class Box:
    def __init__(self):
        self.lenses = []

    def lens_index(self, label):
        for i in range(len(self.lenses)):
            if self.lenses[i].label == label:
                return i

        return -1

    def has_lens(self, label):
        return self.lens_index(label) >= 0


def hash(string):
    hash = 0

    for char in string:
        hash += ord(char)
        hash *= 17
        hash %= 256

    return hash


def parse_input(path):
    commands = []

    with open(path) as file:
        command_strings = file.read().strip().split(",")

        for command_string in command_strings:
            commands.append(Command(command_string))

    return commands


commands = parse_input("input.txt")
boxes = [Box() for _ in range(256)]

# Execute commands:
for command in commands:
    box = boxes[hash(command.label)]

    if command.operation == OPERATION_ADD:
        lens = Lens(command.label, command.focal_length)

        if box.has_lens(command.label):
            box.lenses[box.lens_index(command.label)] = lens
        else:
            box.lenses.append(lens)
    else:
        if box.has_lens(command.label):
            box.lenses.pop(box.lens_index(command.label))

# Calculate focusing power:
focusing_power = 0
for i in range(len(boxes)):
    for j in range(len(boxes[i].lenses)):
        focusing_power += (i + 1) * (j + 1) * boxes[i].lenses[j].focal_length

print(focusing_power)