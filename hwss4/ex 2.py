prices = {
    'banana': 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for keys in prices:
    print(keys)
    print('price :', prices[keys])
    print('cost :', stock[keys])

total = 0
for keys in prices:
    total += (prices[keys]*stock[keys])

print(total)