def diamond(n):
    if n <= 0 or n%2 == 0:
        return None
    mid_pos = int(n/2) + 1
    star = '*'
    nl = '\n'
    gap = ' '
    step = 0
    output = []
    for i in range(1,n + 1,2):
        step += 1
        beads = gap*(mid_pos - step)
        beads += star*i
        beads += nl
        output.append(beads)
    if n > 1:
        index = len(output) -2
        output += output[index::-1]

    
    return(''.join(output))

print(diamond(19))