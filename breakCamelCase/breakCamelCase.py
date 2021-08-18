def solution(s):
    new_string = ''
    j = 0
    for i in range(len(s)):
        if s[i].isupper():
            new_string += s[j:i]
            new_string += ' '
            j = i
        if i == len(s)-1:
            new_string += s[j:i+1]
    return new_string



print(solution("helloWorld"))
print(solution("camelCase"))
print(solution("breakCamelCase"))