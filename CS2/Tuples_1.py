dicts = dict()           # Initialize variables
new_list = list()

fhand = open('M_box_shor.txt')


for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in dicts:
            dicts[words[1]] = 1       
        else:
            dicts[words[1]] += 1     

for key, val in list(dicts.items()):
    new_list.append((val, key))              

new_list.sort(reverse=True)                  

for count, email in new_list[:1]:         
    print(email, count)