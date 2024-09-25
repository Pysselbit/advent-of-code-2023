# Advent of Code 2023
# Day 20-2: Pulse Propagation

import math

TYPE_BROADCASTER = "broadcaster"
TYPE_FLIP_FLOP = "%"
TYPE_CONJUNCTION = "&"


class Pulse:
    def __init__(self, sender, receivers, high):
        self.sender = sender
        self.receivers = receivers
        self.high = high


class Module:
    def __init__(self, id):
        self.id = id
        self.inputs = []
        self.outputs = []

    def add_input(self, input):
        self.inputs.append(input)

    def add_output(self, output):
        self.outputs.append(output)

    def pulse(self, high, _):
        pass


class Broadcaster(Module):
    def pulse(self, high, _):
        return Pulse(self, self.outputs, high)


class FlipFlop(Module):
    def __init__(self, id):
        super().__init__(id)
        self.state = False

    def pulse(self, high, _):
        if high:
            return None

        self.state = not self.state
        return Pulse(self, self.outputs, self.state)


class Conjunction(Module):
    def __init__(self, id):
        super().__init__(id)
        self.input_values = {}

    def add_input(self, input):
        super().add_input(input)
        self.input_values[input] = False

    def pulse(self, high, sender):
        self.input_values[sender] = high
        return Pulse(self, self.outputs, False in self.input_values.values())


def parse_input(path):
    with open(path) as file:
        lines = [line.strip() for line in file.readlines()]
        modules = {}
        connections = {}
        output_module = None

        for line in lines:
            if line.startswith(TYPE_BROADCASTER):
                id = TYPE_BROADCASTER
                modules[id] = Broadcaster(id)
            else:
                id = line.split(" ")[0][1:]
                modules[id] = FlipFlop(id) if line[0] == TYPE_FLIP_FLOP else Conjunction(id)

            connections[id] = line.split(" -> ")[1].split(", ")

        for sender_id in connections:
            for receiver_id in connections[sender_id]:
                if receiver_id not in modules:
                    output_module = Module(receiver_id)
                    modules[receiver_id] = output_module

                sender = modules[sender_id]
                receiver = modules[receiver_id]

                sender.add_output(receiver)
                receiver.add_input(sender)

    return modules, output_module


modules, output_module = parse_input("input.txt")
broadcaster = modules[TYPE_BROADCASTER]

output_parent = output_module.inputs[0]
output_periods = {}

button_press_count = 0
while len(output_periods) < len(output_parent.inputs):
    button_press_count += 1

    queue = [Pulse(None, [broadcaster], False)]

    while len(queue) > 0:
        pulse = queue.pop(0)

        if pulse is None:
            continue

        for receiver in pulse.receivers:
            queue.append(receiver.pulse(pulse.high, pulse.sender))

        # Find periods for the inputs into the output module:
        if output_parent in pulse.receivers and output_parent.input_values[pulse.sender]:
            if pulse.sender not in output_periods:
                output_periods[pulse.sender] = button_press_count

print(math.lcm(*[output_periods[key] for key in output_periods]))