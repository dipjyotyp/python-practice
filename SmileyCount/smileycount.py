import re
def count_smileys(arr):
    count = 0
    smileyRegEx = re.compile(r'^[:;][-~]?[\)D]')
    for smiley in arr:
        mo = smileyRegEx.search(smiley)
        if mo != None:
            count += 1

    return count

print(count_smileys([';]', ':[', ';*', ':$', ';-D']))
print(count_smileys([':)', ';(', ';}', ':-D']))
print(count_smileys([';D', ':-(', ':-)', ';~)']))