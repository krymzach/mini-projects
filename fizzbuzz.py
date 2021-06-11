def fizzbuzz(in_num):
    output = ""
    if in_num % 3 == 0:
        output = output + "fizz"
    if in_num % 5 == 0:
        output = output + "buzz"
    if output == "":
        print(in_num)
    else:
        print(output)

for i in range(1, 101):
    fizzbuzz(i)