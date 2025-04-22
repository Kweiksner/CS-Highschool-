dictionary = dict()              
new_list = list()

fhand = open('M_box.txt', "r")  


for line in fhand:
    words = line.split()
    if len(words) < 5 or words[0] != 'From':
        continue

    column = words[5].find(':')
    hour = words[5][:column]
    if hour not in dictionary:
        dictionary[hour] = 1      
    else:
        dictionary[hour] += 1    

for key, val in list(dictionary.items()):
    new_list.append((key, val))              

new_list.sort()                              

for key, val in new_list:
    print(key, val)
