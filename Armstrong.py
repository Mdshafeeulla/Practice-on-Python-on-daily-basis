def armstrong(number):
    power = len(number)
    sum = 0
    fixed_num = int(number)
    for i in number:
        sum += int(i) ** power
    if sum == fixed_num:
        print("It is armstrong")
    else:
        print("Not an armstrong")
armstrong("123")
