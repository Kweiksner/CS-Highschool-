#next: do the second creating of matrix 
#make sure that the matrix are able to be add, subtracted or multiplied

class matrix:
    def __init__(self, arr):
            self.matrix = arr
            self.rows = len(arr)
            self.columns = len(arr[0]) if arr else 0 

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
        except ValueError:
            return False
        return number
    
    def create_matrix(self,row,col):
        new_answer = self.empty_matrix(row,col)
        for i in range(row):
            for j in range(col):
                while True:
                    number = input(f" Enter number row{i+1} and column{j+1}: ")
                    number = matrix.integer(number)
                    if number != False:
                        new_answer.matrix[i][j] = number
                        break
                    else:
                        print("You did not enter a number")
        return new_answer
                    

    
    def matrix_size(self,m2,opp):
        if opp == 1 or opp == 2:
             if self.rows != m2.rows:
                return False
        elif opp == 3:
             if self.rows != m2.columns and self.columns != m2.rows:
                return False
        else:
            return False
         
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

operations = input("Would you like to add, subtract, multiply, or scalar multiply(Enter 1,2,3 or 4)")
rows = input("How many rows do you want your matrix to be")
columms = input("How many comlumns do you want your matrix to be")
rows = matrix.integer(rows)
columns = matrix.integer(columms)

print("Create your matrix")
tem_matrix = matrix([[]])
matrix_1 = tem_matrix.create_matrix(rows,columns)
print(matrix_1.matrix)
if operations == "1" or operations== "2" or operations =="3":
    print("Create your 2nd matrix")
    #matrix.create_matrix()

#matrix_1=matrix([[1,2,3],
          #[4,5,6],
          #[7,8,9]])
#matrix_2=matrix([[4,5,7],
         # [0,3,4],
          #[5,5,2]])

#add_solution = matrix_1.add(matrix_2)
#print(add_solution.matrix)
#sub_solution = matrix_1.subtract(matrix_2)
#print(sub_solution.matrix)
#mul_solution = matrix_1.multiply(matrix_2)
#print(mul_solution.matrix)
#scl = matrix_1.scalar_times(3)
#print(scl.matrix)


#matrix
#size of the matrix
#values = []

#matrix fns
#add, subtract, multiply
#self.add(other_matrix)