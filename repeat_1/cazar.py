alfavit = input()
sdvig = int(input())


lenalfavit = len(alfavit)

while abs(sdvig) > lenalfavit:
    if sdvig > 0:
        sdvig = sdvig - lenalfavit
    else:
        sdvig = lenalfavit + sdvig

left = alfavit[sdvig:lenalfavit + 1] + alfavit[:sdvig]
if sdvig > 0:
    srez = lenalfavit - sdvig
    right = alfavit[srez:] + alfavit[:srez]
else:
    right = alfavit[abs(sdvig):] + alfavit[:abs(sdvig)]


print(left)
print(alfavit)
print(right)