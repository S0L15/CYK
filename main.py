def readInputFile(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())  # Number of cases
        cases = [] # create a list to store the different cases
        for _ in range(n):
            k, m = map(int, f.readline().split())  # Number of non-terminals and strings
            grammar = [] # create a list to store the grammar
            # Fill the grammar with non terminals and their respective productions
            for _ in range(k):
                prods= f.readline().split()
                nonTerminal = prods[0]
                prods.remove(prods[0])
                grammar.append((nonTerminal, prods))
            inputStrings = [] # create a list for the case strings
            # Fill the list of cases
            for _ in range(m):
                inputStrings.append(f.readline().split())
            cases.append((n, k, m, grammar, inputStrings))
        return cases

def cyk(grammar, string):
    if not string:
        return 'S' in [prod[0] for prod in grammar if not prod[1]]

    stringList = string[0] # change the string (list) to a stringList (string)
    length = len(stringList) # length of the string
    table = [[set() for _ in range(length)] for _ in range(length)] # set the table

    # Fill the table
    for j in range(0, length):
        # iterate over rules
        for lhs, rule in grammar:
            for rhs in rule:
                # if a terminal is found add the non terminal to the table
                if len(rhs) == 1 and rhs[0] == stringList[j]:
                    table[j][j].add(lhs)

        for i in range(j, -1, -1):
            # iterate over the range i to j + 1
            for k in range(i, j):
                # iterate over rules
                for lhs, rule in grammar:
                    for rhs in rule:
                        # if a terminal is found add the non terminal to the table
                        if len(rhs) == 2 and rhs[0] in table[i][k] and rhs[1] in table[k + 1][j]:
                            table[i][j].add(lhs)
    
    # if len(table[0][length-1]) id different from 0 means that the string is produced by the grammar
    if len(table[0][length-1]) != 0:
        return True
    else:
        return False

def processOutput(grammar, inputStrings, n):
    print(f"Caso {n + 1}")
    print('-' * 30)
    for string in inputStrings:
        if cyk(grammar, string):
            print('yes')
        else:
            print('no')

if __name__ == "__main__":
    filename = "test_cky.in"  # Replace with your actual file path
    casesData = readInputFile(filename)
    caseNumber = 0
    # iterates over different cases
    for n, k, m, grammar, inputStrings in casesData:
        processOutput(grammar, inputStrings, caseNumber)
        caseNumber += 1 