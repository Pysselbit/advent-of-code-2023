# Advent of Code 2023
# Day 19-1: Aplenty

import re

ACCEPT = "A"
REJECT = "R"


class Workflow:
    def __init__(self):
        self.rules = []

    def add_rule(self, success, key=None, operation=None, value=None):
        self.rules.append(Workflow.Rule(success, key, operation, value))

    def get_result(self, part):
        for rule in self.rules:
            success = rule.get_result(part)

            if success:
                return success

    class Rule:
        def __init__(self, success, key=None, operation=None, value=None):
            self.success = success
            self.key = key
            self.operation = operation
            self.value = value

        def get_result(self, part):
            if self.operation is None:
                return self.success

            success = part[self.key] > self.value if self.operation == ">" else part[self.key] < self.value

            return self.success if success else None


def parse_input(path):
    with open(path) as file:
        lines = [line.strip() for line in file.readlines()]
        divider = lines.index("")
        workflow_lines = lines[:divider]
        rating_lines = lines[divider + 1:]

        workflows = {}
        parts = []

        for line in workflow_lines:
            workflow = Workflow()
            name = re.search("[a-z]+", line).group()
            rules = re.search("[a-z]+{(.+)}", line).groups()[0].split(",")

            for rule in rules:
                operation = re.search("[<>]", rule)
                if operation:
                    success = rule.split(":")[1]
                    key = re.split("[<>]", rule)[0]
                    operation = operation.group()
                    value = int(re.search(r"\d+", rule).group())

                    workflow.add_rule(success, key, operation, value)
                else:
                    workflow.add_rule(rule)

            workflows[name] = workflow

        for line in rating_lines:
            part = {}
            pairs = re.findall(r"[a-z]=\d+", line)

            for pair in pairs:
                part[re.search("[a-z]", pair).group()] = int(re.search(r"\d+", pair).group())

            parts.append(part)

        return workflows, parts


workflows, parts = parse_input("input.txt")

sum_accepted = 0
for part in parts:
    result = "in"

    while result not in ACCEPT + REJECT:
        result = workflows[result].get_result(part)

    if result == ACCEPT:
        sum_accepted += sum([part[key] for key in part])

print(sum_accepted)