# Duy Tran
# 1002190361
# 4/14/2025
# unbuntu 24.04.2 , python 3.12.4

"""
extra credit B
"""


def numberBlockDepth(fileName):

    with open(fileName, "r") as file:
        lines = file.readlines()

    depth = 0
    isBlockComment = False

    for line in lines:

        # inital depth count for this line
        startDepth = depth
        printDepth = startDepth
        firstBrace = False

        # Keeping leading space and removing trailing space to keep the indentation
        printLine = line.rstrip('\n\r')

        i = 0
        while i < len(line):

            char = line[i]
            # To get next character with bounds check
            nextChar = line[i + 1] if i + 1 < len(line) else None

            # Check if flag for block comment
            if isBlockComment:
                # reset flag then skip these characters
                if char == '*' and nextChar == '/':
                    isBlockComment = False
                    i += 2
                    continue
                else:
                    i += 1
                    continue

            # set flag then skip these characters
            if char == '/' and nextChar == '*':
                isBlockComment = True
                i += 2
                continue

            # if comment then skip the rest of the line
            if char == '/' and nextChar == '/':
                break

            # string literal, skip this character
            if char == '"':
                i += 1

                while i < len(line):
                    if line[i] == '\\' and i + 1 < len(line):
                        # Skip the escape character and the escaped character
                        i += 2
                    elif line[i] == '"':
                        break

                    else:
                        i += 1

                if i < len(line):
                    i += 1
                continue

            # process depth after comments
            if char == '{':
                # If first brace on this line, show depth after this opening brace
                if not firstBrace:
                    printDepth = startDepth + 1
                    firstBrace = True
                # always increase depth for {
                depth += 1
            elif char == '}':
                # If first brace on this line, show depth before this closing brace
                if not firstBrace:
                    printDepth = startDepth
                    firstBrace = True
                # decrease the depth counter when } is found
                if depth > 0:
                    depth -= 1

            i += 1

        print(f"{printDepth} {printLine}")

    # Check for unmatched braces when EOF
    if depth > 0:
        print(f"\nError: unmatched braces (expected ‘}}’ but found EOF) at depth {depth}.")


if __name__ == "__main__":
    numberBlockDepth("input_EC.txt")
