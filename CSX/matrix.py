#next: try to make another class for the second matrix
#document

class matrix:
    def __init__(self, arr):
            self.matrix = arr
            self.rows = len(arr)
            if arr:
                self.columns = len(arr[0])
            else:
                self.columns = 0

    def empty_matrix(self, row, col):
         empt_matrix = []
         for i in range(row):
            cur_row=[]
            for j in range(col):
                cur_row.append(0)
            empt_matrix.append(cur_row)
         return matrix(empt_matrix)
    
    def integer(number):
        try:
            number = int(number)
            return number
        except ValueError:
            answer = "False"
            return answer
    def float(number):
        try:
            number = float(number)
            return number
        except ValueError:
            answer = "False"
            return answer
    
    def create_matrix(self,row,col):
        new_answer = self.empty_matrix(row,col)
        for i in range(row):
            for j in range(col):
                while True:
                    number = input(f" Enter number row{i+1} and column{j+1}: ")                        
                    number = matrix.float(number)
                    if number != "False":
                        new_answer.matrix[i][j] = number
                        break
                    else:
                        print("You did not enter a number")
        return new_answer
                    
    def correct_size(self,rows2,col2,opp):
        if opp == "1" or opp == "2":
             if self.rows != rows2 or self.columns != col2:
                return "False"
             else:
                return True
        elif opp == "3":
             if self.rows != col2 and self.columns != rows2:
                return "False"
             else:
                 return True 
        else:
            return "False"
         
    def add(self, m2):
        answer = self.empty_matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                answer.matrix[i][j] = self.matrix[i][j] + m2.matrix[i][j]   
        return answer
    
    def subtract(self, m2):
        answer = self.empty_matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                answer.matrix[i][j] = self.matrix[i][j] - m2.matrix[i][j]
        return answer
    
    def multiply(self,m2):
        answer = self.empty_matrix(self.rows, self.columns)
        for i in range(self.rows):  
            for j in range(m2.columns): 
                for k in range(self.columns):
                    answer.matrix[i][j] = answer.matrix[i][j] + self.matrix[i][k] * m2.matrix[k][j]
        return answer
    
    def scalar_times(self,number):
        answer = self.empty_matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                answer.matrix[i][j] = number *self.matrix[i][j]
        return answer

def main():
    thing=0
    opper =0
    while thing == 0:
        while opper == 0:
            operations = input("Would you like to add, subtract, multiply, or scalar multiply(Enter 1,2,3 or 4): ")
            if operations != "1" and operations != "2" and operations != "3" and operations != "4":
                print("Please enter a number(1-4)")
            else:
                rc=0
                while rc == 0:
                    rows = input("How many rows are in your matrix?: ")
                    columms = input("How many comlumns are in your matrix: ")
                    rows = matrix.integer(rows)
                    columns = matrix.integer(columms)
                    if rows != "False" and columns != "False":
                        rc=1
                    else:
                        print("Enter numbers for your rows and columns")
                        
                print("Create your matrix")
                tem_matrix = matrix([[]])
                matrix_1 = tem_matrix.create_matrix(rows,columns)
                print(matrix_1.matrix)

                if operations == "1" or operations== "2" or operations =="3":
                    size=0
                    while size == 0:
                        rc2=0
                        print("Create your 2nd matrix")
                        while rc2== 0:
                            rows2 = input("How many rows are in your matrix?: ")
                            columms2 = input("How many comlumns are in your matrix: ")
                            rows2 = matrix.integer(rows2)
                            columns2 = matrix.integer(columms2)
                            if rows2 != "False" and columns2 != "False":
                                rc2=1
                            else:
                                print("Enter numbers for your rows and columns")
                        
                        sizing = matrix_1.correct_size(rows2,columns2,operations)
                        if sizing == "False":
                            print("Please enter correct sizing for the operation you are trying to preform")
                        else:
                            tem_matrix2 = matrix([[]])
                            matrix_2 = tem_matrix2.create_matrix(rows,columns)
                            print(matrix_2.matrix)
                            size =1
                opper = 1
            if operations =="1": 
                add_solution = matrix_1.add(matrix_2)
                print(add_solution.matrix)
            elif operations =="2":
                sub_solution = matrix_1.subtract(matrix_2)
                print(sub_solution.matrix)
            elif operations =="3": 
                mul_solution = matrix_1.multiply(matrix_2)
                print(mul_solution.matrix)
            elif operations =="4": 
                while True:
                    times = input("How many times would you like to multiply you matrix by: ")
                    times = matrix.integer(times)
                    if times != "False":
                        scl = matrix_1.scalar_times(times)
                        print(scl.matrix)
                        break
                    else: 
                        print("Please enter a number")
        thing =1

main()