class matrix:
    def __init__(self, arr):
        self.matrix = arr
        self.rows = int(len(arr))
        if arr:
            self.columns = int(len(arr[0]))
        else:
            self.columns = 0
    def switch_rows(self,r1,r2):
        self.matrix[r1-1], self.matrix[r2-1] = self.matrix[r2-1], self.matrix[r1-1]

def main():
    matrix1 = matrix([[1,2,3,4],  # <-- Added comma here
                      [4,5,6,7]])  # <-- Changed to create matrix object
    
    numb = 1
    num2 = 2
    matrix1.switch_rows(numb, num2)
    
    # Print the matrix to see the result
    print(matrix1.matrix)

main()