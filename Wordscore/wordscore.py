def high(x):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    sentence = x.split()
    weights = []
    for word in sentence:
        weight = 0
        for char in word:
            index = 1 + alpha.index(char)
            weight += index
        weights.append(weight)
    return(sentence[weights.index(max(weights))])

print(high('man i need a taxi up to zzzz'))