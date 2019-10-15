import sys

def f_len(x):
    if len(x)==len(word):
        if x == word:
            return x
        else:
            pass


word = 'далеки'
words = list(map(f_len, input().split()))
print(words)
for line in words:
    print(line[0:6:])




# words = sys.stdin
# # words = list(map(str.strip, sys.stdin))
# print(words)
# s = 0
# f = 0
# for i in words:
#     i = i.lower()[:-1]
#     for j in i.split():
#         if 'далек' in j[:4]:
#             s += 1
#     if s >= 1:
#         f += 1
#         s = 0
# print(f)