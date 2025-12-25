

def convert_tobase10(number):
    new_numb = int(number,16)
    return new_numb

def convert_tobase16(number):
    new_numb = hex(number)[2: ].upper()
    return new_numb
    
    
def findCreature(input1, input2, input3):
    locations = []
    distaway =[]
    columns = []
    rows = []
    option1 = []
    option2 = []

    input1_possiblites = []
    input2_possiblites = []
    input3_possiblites = []
    
    input1s = input1.split()
    input2s = input2.split()
    input3s = input3.split()
    locations.append(input1s[0])
    distaway.append(input1s[1])
    locations.append(input2s[0])
    distaway.append(input2s[1])
    locations.append(input3s[0])
    distaway.append(input3s[1])
    
    for i in range(len(locations)):
        row_column = locations[i]
        row = row_column[:2]
        rows.append(row)
        column = row_column[-2:]
        columns.append(column)
    
    for i in range(len(distaway)):
        row_column = distaway[i]
        row = row_column[:2]
        option1.append(row)
        column = row_column[-2:]
        option2.append(column)
    
    input_1_row = rows[0]
    i1r = convert_tobase10(input_1_row)
    input_1_col = columns[0]
    i1c = convert_tobase10(input_1_col)
    input_1_opt_1 = option1[0]
    i101 = convert_tobase10(input_1_opt_1)
    input_1_opt_2 = option2[0]
    i102 = convert_tobase10(input_1_opt_2)

    R11 = str(i1r + i102)
    R12 = str(i1r + i101)
    R13 = str(i1r - i102)
    R14 = str(i1r - i101)
    C11 = str(i1c + i102)
    C12 = str(i1c + i101)
    C13 = str(i1c - i102)
    C14 = str(i1c - i101)

    input1_possiblites.append((R11, C14))
    input1_possiblites.append((R11, C12))
    input1_possiblites.append((R13, C14))
    input1_possiblites.append((R13, C12))
    input1_possiblites.append((R12, C11))
    input1_possiblites.append((R12, C13))
    input1_possiblites.append((R14, C11))
    input1_possiblites.append((R14, C13))
    
    input_2_row = rows[1]
    i2r = convert_tobase10(input_2_row)
    input_2_col = columns[1]
    i2c = convert_tobase10(input_2_col)
    input_2_opt_1 = option1[1]
    i201 = convert_tobase10(input_2_opt_1)
    input_2_opt_2 = option2[1]
    i202 = convert_tobase10(input_2_opt_2)

    R21 = str(i2r + i202)
    R22 = str(i2r + i201)
    R23 = str(i2r - i202)
    R24 = str(i2r - i201)
    C21 = str(i2c + i202)
    C22 = str(i2c + i201)
    C23 = str(i2c - i202)
    C24 = str(i2c - i201)

    input2_possiblites.append((R21, C24))
    input2_possiblites.append((R21, C22))
    input2_possiblites.append((R23, C24))
    input2_possiblites.append((R23, C22))
    input2_possiblites.append((R22, C21))
    input2_possiblites.append((R22, C23))
    input2_possiblites.append((R24, C21))
    input2_possiblites.append((R24, C23))

    input_3_row = rows[2]
    i3r = convert_tobase10(input_3_row)
    input_3_col = columns[2]
    i3c = convert_tobase10(input_3_col)
    input_3_opt_1 = option1[2]
    i301 = convert_tobase10(input_3_opt_1)
    input_3_opt_2 = option2[2]
    i302 = convert_tobase10(input_3_opt_2)

    
    R31 = str(i3r + i302)
    R32 = str(i3r + i301)
    R33 = str(i3r - i302)
    R34 = str(i3r - i301)
    C31 = str(i3c + i302)
    C32 = str(i3c + i301)
    C33 = str(i3c - i302)
    C34 = str(i3c - i301)

    input3_possiblites.append((R31, C34))
    input3_possiblites.append((R31, C32))
    input3_possiblites.append((R33, C34))
    input3_possiblites.append((R33, C32))
    input3_possiblites.append((R32, C31))
    input3_possiblites.append((R32, C33))
    input3_possiblites.append((R34, C31))
    input3_possiblites.append((R34, C33))


    for i in range(len(input1_possiblites)):
        for j in range(len(input2_possiblites)):
            if input1_possiblites[i] == input2_possiblites[j]:
                for k in range(len(input3_possiblites)):
                    if input3_possiblites[k] == input1_possiblites[i] and input2_possiblites[j] == input3_possiblites[k]:
                        arow, acol = input1_possiblites[i]
                        hrow = convert_tobase16(int(arow))
                        hcol = convert_tobase16(int(acol))

                        if len(hrow) == 1:
                            hrow = "0" + hrow
                        if len(hcol) == 1:
                            hcol = "0" + hcol
                        

                        result = (f"({hrow}, {hcol})")
                        return result             

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    input1 = ("4D93 414D")

    input2 = ("A566 997A")

    input3 = ("F633 EAAD")

    result = findCreature(input1, input2, input3)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()