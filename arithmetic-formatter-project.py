def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_operands = []
    operators = []
    second_operands = []
    results = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        a, op, b = parts

        if op not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not a.isdigit() or not b.isdigit():
            return "Error: Numbers must only contain digits."

        if len(a) > 4 or len(b) > 4:
            return "Error: Numbers cannot be more than four digits."

        first_operands.append(a)
        operators.append(op)
        second_operands.append(b)

        if op == '+':
            results.append(str(int(a) + int(b)))
        else:
            results.append(str(int(a) - int(b)))

    line1 = []
    line2 = []
    line3 = []
    line4 = []

    for i in range(len(problems)):
        width = max(len(first_operands[i]), len(second_operands[i])) + 2
        line1.append(first_operands[i].rjust(width))
        line2.append(operators[i] + second_operands[i].rjust(width - 1))
        line3.append('-' * width)
        line4.append(results[i].rjust(width) if show_answers else '')

    arranged_problems = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(line3)
    if show_answers:
        arranged_problems += "\n" + "    ".join(line4)

    return arranged_problems
