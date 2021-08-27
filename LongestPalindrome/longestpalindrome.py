def longest_palindrome (s):
    if s == s[::-1]:
        return len(s)
    text = s
    reverse_text = ''
    subtext = ''
    count = []
    for i in range((len(s)), 0, -1):
        for j in range(len(s)):
            subtext = text[j:i]
            reverse_text = subtext[::-1]
            if len(reverse_text) == 1:
                continue
            if subtext == reverse_text:
                count.append(subtext)
    if len(max(count, key = len)) == 0:
        return 1
    else:
        return len(max(count, key = len))


print(longest_palindrome("abklmomlke"))
print(longest_palindrome("abcdefghba"))
print(longest_palindrome("baablkj12345432133d"))
