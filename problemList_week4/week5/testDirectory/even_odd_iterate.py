# for loop to iterate between odd elements and even elements
n = 6
evenNumber = []
oddNumber = []

sampleAlphabet = 'ABCDEF'

# add even number less than 6 in list
for i in range(0, n, 2):
    evenNumber.append(i)

# add odd number less than 6 in list
for j in range(1, n, 2):
    oddNumber.append(j)

# for loop to iterate between odd and even number
for char, enum in zip(sampleAlphabet[0::2], evenNumber):
    print(f'{char}: {enum}')

for char, onum in zip(sampleAlphabet[1::2], oddNumber):
    print(f'{char}: {onum}')
