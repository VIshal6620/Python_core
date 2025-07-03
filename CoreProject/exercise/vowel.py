str = 'vishal'

for vowel in 'aeiou':
    count = 0
    for ch in str:
        if ch == vowel:
            count += 1
    if count != 0:
        print(vowel, "count =", count)