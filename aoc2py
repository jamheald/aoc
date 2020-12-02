input = open("/Users/james.heald/Documents/aoc/aoc2input.txt","r")

passwords = input.read().split('\n')

n = 0
m = 0

for i in range(len(passwords)):
    passArray = passwords[i].split(' ')
    numberString = passArray[0].split('-')
    numbers = [int(string) for string in numberString]
    char = passArray[1][0]
    password = passArray[2]

    occur = len(password.split(char))-1

    n = n + (numbers[0]<=occur and numbers[1]>=occur)

    char1 = password[numbers[0]-1]
    char2 = password[numbers[1]-1]

    kosh1 = char == char1
    kosh2 = char == char2

    m = m + (kosh1 * (not kosh2) + (not kosh1) * kosh2)

print(n,m)