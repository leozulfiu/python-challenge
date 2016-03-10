
def get_next_number(number):
    quantity = 0
    value = 0
    for digit in range(len(str(number))):
        print "a"
    return number+1


get_next_number(3333221111)
startValue = 1

currentNumber = startValue
numbers = [startValue]

for i in range(30):
    currentNumber = get_next_number(currentNumber)
    numbers.append(currentNumber)
