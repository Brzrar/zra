data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
codes = []
designations = []
for i in data:
    if i.isdigit():
        codes.append(i)
    else:
        designations.append(i)
operators = {}
x = 0
while len(operators) != len(designations):
    operators[designations[x]] = set()
    operators[designations[x]].add((codes[x]))
    x += 1
del operators['Katel']
del operators['Fonex']
operators['O!'].add('0700')
operators['O!'].add('0500')
operators['Megacom'].add('0999')
operators['Megacom'].add('0755')
operators['Beeline'].add('0777')
operators['Beeline'].add('0222')

for k, v in operators.items():
    print(k, ':', v)