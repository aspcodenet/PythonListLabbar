texter = ['abc', 'xyz', 'aba', '1221']

antal = 0
for s in texter:
    if len(s) >=2 and s[0] == s[len(s)-1]:
        antal = antal + 1

print(antal)