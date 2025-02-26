import csv
def main():
    fhand = open('student_data_cs2.txt', "r") 
    csvname = "data_sort.csv"
    with open(csvname, 'w', newline='') as file:                               #opens csv file

        for line in fhand: 
            ID = line[0:4].rstrip()
            first_name=line[5:19].rstrip()
            last_name=line[21:35].rstrip()
            grade = line[36:38].rstrip()
            GPA =line[42:46].rstrip()
            birth_date = line[47:58].rstrip()
            gender= line[60: 61].rstrip()
            class_rank = line[67:70].rstrip()
            attend_pct = line[76:86].rstrip()
            honors = line[86:87].rstrip()
            sport = line[93:102].rstrip()
            club_count=line[102:111].rstrip()
         # writing to csv file
            writer = csv.writer(file)
            writer.writerow([ID, first_name, last_name,grade,GPA, birth_date, gender,class_rank, attend_pct, honors, sport,club_count])
        
main()