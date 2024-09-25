# Advent of Code 2023
# Day 19-2: Aplenty

import re

ACCEPT = "A"
REJECT = "R"

MIN = 1
MAX = 4000


class Workflow:
    def __init__(self):
        self.rules = []

    def add_rule(self, success, key=None, span=None):
        self.rules.append(Workflow.Rule(success, key, span))

    def apply(self, spans):
        paths = []

        for rule in self.rules:
            success_spans, fail_spans = rule.apply(spans)

            if success_spans is not None:
                paths.append(Path(rule.success, success_spans))

            spans = fail_spans

        return paths

    class Rule:
        def __init__(self, success, key, span):
            self.success = success
            self.key = key
            self.span = span

        def apply(self, spans):
            if self.key is None:
                return spans, None

            span = spans[self.key]
            success_span = span.intersection(self.span)
            fail_span = span.difference(self.span)
            succes_spans = fail_spans = None

            if success_span is not None:
                succes_spans = spans.copy()
                succes_spans[self.key] = success_span
            if fail_span is not None:
                fail_spans = spans.copy()
                fail_spans[self.key] = fail_span

            return succes_spans, fail_spans


class Path:
    def __init__(self, name, spans):
        self.name = name
        self.spans = spans


class Span:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def intersection(self, other):
        if self.min > other.max or self.max < other.min:
            return None

        return Span(max(self.min, other.min), min(self.max, other.max))

    def difference(self, other):
        spanA = Span(self.min, other.min - 1)
        spanB = Span(other.max + 1, self.max)

        if spanA.max >= spanA.min:
            return spanA
        if spanB.max >= spanB.min:
            return spanB

        return None


def parse_input(path):
    with open(path) as file:
        lines = [line.strip() for line in file.readlines()]
        divider = lines.index("")
        workflow_lines = lines[:divider]

        workflows = {}

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
                    limit = int(re.search(r"\d+", rule).group())
                    span = Span(MIN, limit - 1) if operation == "<" else Span(limit + 1, MAX)

                    workflow.add_rule(success, key, span)
                else:
                    workflow.add_rule(rule)

            workflows[name] = workflow

        return workflows


workflows = parse_input("input.txt")
paths = [Path("in", {"x": Span(MIN, MAX), "m": Span(MIN, MAX), "a": Span(MIN, MAX), "s": Span(MIN, MAX)})]
accepted_spans = []

while len(paths) > 0:
    path = paths.pop(0)

    if path.name == REJECT:
        continue
    if path.name == ACCEPT:
        accepted_spans.append(path.spans)
    else:
        paths.extend(workflows[path.name].apply(path.spans))

total_accepted_combinations = 0
for spans in accepted_spans:
    accepted_combinations = 1

    for key in spans:
        accepted_combinations *= spans[key].max - spans[key].min + 1

    total_accepted_combinations += accepted_combinations

print(total_accepted_combinations)