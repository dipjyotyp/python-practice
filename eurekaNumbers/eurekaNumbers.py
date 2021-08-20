def sum_dig_pow(a, b):
    eureka_numbers = []
    for i in range(a,b+1):
        num = str(i)
        sum = 0
        for j in range(len(num)):
            sum += int(num[j])**(j+1)
        if sum == i:
            eureka_numbers.append(sum)
    return eureka_numbers


print(sum_dig_pow(1, 10))
print(sum_dig_pow(1, 100))
print(sum_dig_pow(89, 135))