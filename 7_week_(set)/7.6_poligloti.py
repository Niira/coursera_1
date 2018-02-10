n = int(input())
mySet = set()
mySet1 = set()
mySet2 = set()
if n != 0:
    pupil1 = int(input())
    if pupil1 != 0:
        for line in range(pupil1):
            lang = str(input())
            mySet.add(lang)
            mySet1.add(lang)
    if n - 1 != 0:
        for i in range(n - 1):
            pupil = int(input())
            if pupil != 0:
                for string in range(pupil):
                    lang = str(input())
                    mySet.add(lang)
                    mySet2.add(lang)
            else:
                continue
            mySet1 &= mySet2
            mySet2.clear()
print(len(mySet1))
for lang in sorted(mySet1):
    print(lang)
print(len(mySet))
for lang in sorted(mySet):
    print(lang)
