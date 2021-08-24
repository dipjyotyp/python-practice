def tickets(people):
    sorted_list = sorted(people)
    bill_25, bill_50 = people.count(25), people.count(50)
    count = 0
    while count < len(people):
        popped = sorted_list.pop(0)
        if popped == 50:
            bill_25 -= 1
        if bill_25 < 0:
            return 'NO'
        if popped == 100:
            if bill_25 >= 1 and bill_50 >= 1:
                bill_25 -= 1
                bill_50 -= 1
            elif bill_25 >= 3:
                bill_25 -= 3
            else:
                return 'NO'
        count += 1
    return 'YES'


print(tickets([25, 25, 50]))
print(tickets([50, 50, 50]))
print(tickets([25, 25, 50, 50, 100]))
print(tickets([25, 100]))