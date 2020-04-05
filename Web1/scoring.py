import dpath.util
import json
with open('scoring.json', 'r') as file:
    data = json.load(file)
required_tests = dpath.util.values(data, '**/required_tests')
points = dpath.util.values(data, '**/points')
c = 0
for i in range(len(required_tests)):
    if (points[i] % len(required_tests[i])) == 0:
        c += points[i] / len(required_tests[i])
    #     print('ok')
    # else:
    #     print('wa')

print(int(c))