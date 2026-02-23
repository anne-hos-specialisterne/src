

filename = '../data/navneliste.txt'

file = open(filename)

names = file.readlines()[0]


file.close()

names1 = names.split(sep = ',')
#print(names1)

sorted_names_alpha = sorted(names1)
sorted_names_len = sorted(names1, key = len)


print(sorted_names_alpha)
print(sorted_names_len)

length_dictionary = {}

for name in sorted_names_len:
    n = list(name)
    length_dictionary[name] = len(n)


print(length_dictionary)