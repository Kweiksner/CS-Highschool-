import string

counts = 0                          # Initialize variables
dict_counts = dict()
new_list = list()

fhand = open('M_box_shor.txt', 'r')

for line in fhand:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()

    words = line.split()
    for word in words:
        for letter in word:
            counts += 1
            if letter not in dict_counts:
                dict_counts[letter] = 1
            else:
                dict_counts[letter] += 1

for key, val in list(dict_counts.items()):
    new_list.append((val / counts, key))  # Computes the relative frequency

new_list.sort(reverse=True)         # Sorts from highest rel freq

for key, val in new_list:
    print(key, val)