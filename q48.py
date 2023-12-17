def ziarat(string):
    if string == 'NNN':
        return 'Agha'
    if string[0] == 'Y':
        return 'Haji'
    if string[1] == 'Y':
        return 'Karbalaee'
    return 'Mashti'
string = input()
print(ziarat(string))