def change_case(char):
    return char.lower() if char.isupper() else char.upper()

def work_on_strings(a,b):
    counter = 1
    while counter < 3:
        for i in range(len(a)):
            txt = []
            for j in range(len(b)):
                if a[i].lower() == b[j].lower():
                    txt.append(change_case(b[j]))
                else:
                    txt.append(b[j])
            b = ''.join(txt)
        a,b = b,a
        counter += 1
    return a+b


print(work_on_strings("abc","cde"))
print(work_on_strings("abcdeFgtrzw", "defgGgfhjkwqe"))