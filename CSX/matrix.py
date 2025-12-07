#question:How to make sure that my decimals are not so long
#how do i make my matrix lines line up


import sys
class matrix:
    def __init__(self, arr):
            self.matrix = arr
            self.rows = int(len(arr))
            if arr:
                self.columns = int(len(arr[0]))
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
        
    def floats(number):
        try:
            number = float(number)
            return number
        except ValueError:
            answer = "False"
            return answer
        
    def decimal(numb):
        try:
            if '/' in numb:
                split_nu = numb.split('/')                                  #splits number into 2 before and after the devided by symbol
                if len(split_nu) == 2:
                    numer = float(split_nu[0])
                    denom= float(split_nu[1])
                    if denom != 0:
                        return numer / denom
                    else:
                        return "False"
            return int(numb)                                                # if there is not divide by sign, then return a integer
        except:
            try:
                return float(numb)                                          # returns a float if number is not an integer
            except:
                return "False"
            
    def mat():
        mat=0
        while mat ==0:
            numb_mat = input("How many matrics would you like to make")
            numb_mat= matrix.integer(numb_mat)
            if numb_mat == "False" or numb_mat<1 :
                print("Please enter an integer larger than one")
            else:
                return numb_mat
    
    def create_matrix(self,row,col):
        new_answer = self.empty_matrix(row,col)
        for i in range(row):
            for j in range(col):
                while True:
                    number = input(f" Enter number row{i+1} and column{j+1}: ")                        
                    number = matrix.decimal(number)
                    if number != "False":
                        new_answer.matrix[i][j] = number
                        break
                    else:
                        print("You did not enter a number or fraction!")
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
    
    def display(self):
        for i in range(self.rows):
            print("[ ", end='')
            for j in range(self.columns):
                print(self.matrix[i][j] , end=' ')
            print("]")

    def available_matrix(mlist):
        print("Available matrices:")
        for name, mat in mlist.items():
            print()
            print(f"{name} ({mat.rows}x{mat.columns}):")
            mat.display()
            print()

    def add(self, m2):
        answer = self.empty_matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                answer.matrix[i][j] = (self.matrix[i][j]) + (m2.matrix[i][j])#why is this just adding the two numbers like 1+2 becomes 12   
        return answer
    
    def subtract(self, m2):
        answer = self.empty_matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                answer.matrix[i][j] = int(self.matrix[i][j]) - int(m2.matrix[i][j])
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
    
    def switch_rows(self,r1,r2):
        self.matrix[r1-1], self.matrix[r2-1] = self.matrix[r2-1], self.matrix[r1-1]

def main():
    thing = 0
    matrices = {}  # Dictionary to store all matrices by name
    
    while True:
        print("MATRIX CALCULATOR")
        print()
        print("1. Create new matrix")
        print("2. View all matrices")
        print("3. Add two matrices")
        print("4. Subtract two matrices")
        print("5. Multiply two matrices")
        print("6. Scalar multiplication")
        print("7. Switch Rows")
        print("8. Combine Rows")
        print("9. Reduce matrix")
        print("10. Invert Matrix")
        print("11. Delete a matrix")
        print("12. Exit")
        print()

        thing = 0 
        while thing ==0:
            choice = input("Enter your choice (1-12): ")
            if choice != "2" and choice != "1" and choice != "3" and choice != "4" and  choice != "5" and  choice != "6" and  choice != "7" and  choice != "8":
                print("Please enter a number 1-8")
            else:
                thing =1

        if choice == "1":
            name = input("Enter a name for this matrix: ")
            
            while True:
                rows = input("Enter number of rows: ")
                rows = matrix.integer(rows)
                if rows != "False" and rows > 0:
                    break
                print("Please enter a valid positive integer")
            
            while True:
                cols = input("Enter number of columns: ")
                cols = matrix.integer(cols)
                if cols != "False" and cols > 0:
                    break
                print("Please enter a valid positive integer")
            
            temp = matrix([])
            mat = temp.create_matrix(rows, cols)
            matrices[name] = mat
            print(f" Matrix '{name}' created successfully!")
            mat.display()
        
        elif choice == "2":
            if not matrices:
                print("No matrices created yet")
            else:
                matrix.available_matrix(matrices)
        
        elif choice == "3" or choice == "4":
            if len(matrices) < 2:
                print("You need at least 2 matrices to perform addition or subtraction!")
                names = 1
                dem = 1
            else:
                names = 0 
                dem = 0
            
            while names == 0:
                matrix.available_matrix(matrices)
                m1_name = input("Enter first matrix name: ")
                m2_name = input("Enter second matrix name: ")
                
                if m1_name not in matrices or m2_name not in matrices:
                    print("One or both matrix names not found!")
                else:
                    names =1 
            
            while dem == 0:
                m1 = matrices[m1_name]
                m2 = matrices[m2_name]
                if m1.correct_size(m2.rows, m2.columns, "1") == "False":
                    print("Matrices must have the same dimensions for addition or subtractions!")
                    dem = 1
                else:
                    dem = 1
            
            if choice =="3":
                result = m1.add(m2)
                result_name = input("Enter name for result matrix: ")
                matrices[result_name] = result
                print(f"Result of {m1_name} + {m2_name}:")
                result.display()
            
            else:
                result = m1.subtract(m2)
                result_name = input("Enter name for result matrix: ")
                matrices[result_name] = result
                print(f"Result of {m1_name} - {m2_name}:")
                result.display()
        
        elif choice == "5":
            if len(matrices) < 2:
                print("You need at least 2 matrices to perform multiplication!")
                names = 1
            else:
                names =0
            
            while names == 0:
                matrix.available_matrix(matrices)
                m1_name = input("Enter first matrix name: ")
                m2_name = input("Enter second matrix name: ")
                
                if m1_name not in matrices or m2_name not in matrices:
                    print("One or both matrix names not found!")
                else: 
                    names = 1 
                    
            m1 = matrices[m1_name]
            m2 = matrices[m2_name]
            
            if m1.correct_size(m2.rows, m2.columns, "3") == "False":
                print(f"Cannot multiply: columns of first matrix ({m1.columns}) must equal rows of second matrix ({m2.rows})!")
            else:
                result = m1.multiply(m2)
                result_name = input("Enter name for result matrix: ")
                matrices[result_name] = result
                print(f"Result of {m1_name} × {m2_name}:")
                result.display()
        
        elif choice == "6":
            if not matrices:
                print("You need at least 1 matrix for Scalar Multiplication!")
                scal_right = 1
                name_right = 1
            else:
                name_right = 0
            
            while name_right ==0:
                matrix.available_matrix(matrices)
                mat_name = input("Enter matrix name: ")
                if mat_name not in matrices:
                    print("Matrix not found! Enter a matrix you have already created")
                else:
                    name_right = 1
                    scal_right = 0 
            
            while scal_right == 0:
                scalar = input("Enter multiplication value: ")
                scalar = matrix.floats(scalar)
                if scalar != "False":
                    break
                print("Please enter a valid number")
            
            result = matrices[mat_name].scalar_times(scalar)
            rname = input("Enter name for result matrix: ")
            matrices[rname] = result
            print(f"Result of {scalar} × {mat_name}:")
            result.display()
       
        elif choice == "7":
            if not matrices:
                print("No matrices to switch rows!")
                name_right = 1
                correct_row =1 
            else:
                name_right = 0 

            while name_right == 0:
                matrix.available_matrix(matrices)
                name = input("Enter matrix name to switch to rows: ")

                if name in matrices:
                    m1 = matrices[name]
                    correct_row = 0
                    name_right= 1
                else:
                    print("Matrix not found, pick another one!")
                    
            while correct_row == 0:
                r1 = input("Enter first row: ")
                r2 = input("Enter second row: ")
                r1 = matrix.integer(r1)
                r2 = matrix.integer(r2)

                if r1 != "False" and r2!= "Flalse" and r1 > 0 and r2 >0 and r1!= r2:
                    if r1 <= m1.rows and r2 <= m1.rows:
                        m1.switch_rows(r1,r2)
                        print(f"{r1} and {r2} switched succsessfully ")
                        m1.display()
                        correct_row = 1
                    else:
                        print(f"Enter a number between 1 and {m1.rows}")
                else:
                    print("Please enter a 2 different positive integers")
    
        elif choice == "11":
            if not matrices:
                print("No matrices to delete!")
                name_right = 1
            else:
                name_right = 0 
            
            while name_right ==0:
                matrix.available_matrix(matrices)
                name = input("Enter matrix name to delete: ")
                
                if name in matrices:
                    del matrices[name]
                    print(f"Matrix '{name}' deleted successfully!")
                    name_right = 1
                else:
                    print("Matrix not found, pick another one!")
        
        elif choice == "12":
            print("Thank you for using Matrix Calculator!")
            sys.exit()

        else:
            print("Invalid choice! Please enter a number between 1 and 8.")

main()