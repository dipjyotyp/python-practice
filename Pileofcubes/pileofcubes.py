def find_nb(m):
    n = 0
    volume = 0
    while True:
        volume += n**3
        if volume == m:
            return n
        elif volume > m:
            return -1
        n += 1

print(find_nb(4183059834009))
print(find_nb(24723578342962))
print(find_nb(135440716410000))
print(find_nb(0))
print(find_nb(1))