def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    x = y = 0
    for dir in walk:
        if dir == 'n':
            y += 1
        if dir == 's':
            y -= 1
        if dir == 'e':
            x += 1
        if dir == 'w':
            x -= 1
    
    if x == y and x == 0:
        return True
    else:
        return False

print(is_valid_walk(['s','n','w','e']))
print(is_valid_walk(['e','w','w','e']))
print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))