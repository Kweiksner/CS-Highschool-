class matrix:
    def __init__(self, arr):
        self.matrix = arr
        self.rows = int(len(arr))
        if arr:
            self.columns = int(len(arr[0]))
        else:
            self.columns = 0
    
    def comb_rows(self, scalar, mrow1, nrow2):
        for i in range(self.columns):
            self.matrix[nrow2-1][i]= self.matrix[nrow2-1][i] + (scalar *self.matrix[mrow1-1][i])
        self.display()
    
    def display(self):
        for i in range(self.rows):
            print("[ ", end='')
            for j in range(self.columns):
                print(self.matrix[i][j], end=' ')
            print("]")

def main():
    m_data = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    
    m = matrix(m_data)  # Create a matrix object
    m.comb_rows(3, 1, 2)

main()
