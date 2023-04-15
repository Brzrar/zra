
data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for i in data_tuple:
     if type(i) == str:
          letters.append(i)
     else:
          numbers.append(i)
numbers.remove(6.13)
numbers.remove(True)
letters.append(True)
numbers.insert(len(numbers) // 2, 2)
list.sort(numbers)
letters.reverse()
letters[letters.index('C')] = 'c'
letters[letters.index('g')] = 'G'
numbers[-2] = 4
numbers[-1] = 9
tuple1 = tuple(letters)
tuple2 = tuple(numbers)
print(tuple1)
print(tuple2)
