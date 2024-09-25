# Advent of Code 2023
# Day 20-1: Pulse Propagation

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
        self.outputs = []

    def add_input(self, input):
        pass

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
        self.inputs = {}

    def add_input(self, input):
        self.inputs[input] = False

    def pulse(self, high, sender):
        self.inputs[sender] = high
        return Pulse(self, self.outputs, False in self.inputs.values())


def parse_input(path):
    with open(path) as file:
        lines = [line.strip() for line in file.readlines()]
        modules = {}
        connections = {}

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
                    modules[receiver_id] = Module(receiver_id)

                sender = modules[sender_id]
                receiver = modules[receiver_id]

                sender.add_output(receiver)
                receiver.add_input(sender)

    return modules


modules = parse_input("input.txt")
broadcaster = modules[TYPE_BROADCASTER]
high_pulse_count = low_pulse_count = 0

for _ in range(1000):
    queue = [Pulse(None, [broadcaster], False)]

    while len(queue) > 0:
        pulse = queue.pop(0)

        if pulse is None:
            continue

        if pulse.high:
            high_pulse_count += len(pulse.receivers)
        else:
            low_pulse_count += len(pulse.receivers)

        for receiver in pulse.receivers:
            queue.append(receiver.pulse(pulse.high, pulse.sender))

print(high_pulse_count * low_pulse_count)