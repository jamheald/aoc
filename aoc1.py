input = open("/Users/james.heald/Documents/aoc/aoc1input.txt","r")

expenses = input.read().split('\n')

expenses = [int(string) for string in expenses]

eLen = len(expenses)

for i in range(eLen):
    for j in range(i+1,eLen):
        if expenses[i] + expenses[j] == 2020:
            output1 = expenses[i] * expenses[j]
        for k in range(j+1,eLen):
            if expenses[i] + expenses[j] + expenses[k] == 2020:
                output2 = expenses[i] * expenses[j] * expenses[k]
                break

print(output1)
print(output2)