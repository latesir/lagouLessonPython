import random

computer_number = random.randint(1, 10)
print(computer_number)

while True:
    input_number = int(input("请输入一个数字"))
    if computer_number > input_number:
        print("bigger")
    elif computer_number < input_number:
        print("smaller")
    else:
        print("right")
        break
