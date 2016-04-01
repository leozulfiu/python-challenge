
def get_next_number(number):
    quantity = 0
    output = ""
    number_string = str(number)
    current_number = number_string[0]
    index = 0

    while True:
        if index == len(number_string):
            output += str(quantity) + str(current_number)
            break
        digit = number_string[index]
        if digit == current_number or index == len(number_string):
            quantity += 1
        else:
            output += str(quantity) + str(current_number)
            quantity = 1
            current_number = digit
        index += 1
    return output

startValue = 1
currentNumber = startValue
numbers = [startValue]

for i in range(30):
    currentNumber = get_next_number(currentNumber)
    numbers.append(currentNumber)

print len(numbers[30])

#solution: 5808
#not final solution...