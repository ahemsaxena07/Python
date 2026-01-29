

class Matrix:
    def __init__(self, data):
        self.data = data
        self.row = 3 
        self.cols = 3

    def display(self):
        print('Matrix: ')
        for row in self.data:
            print(row)

    def add(self, other):
        result = [[0,0,0], [0,0,0], [0,0,0]]
        for i in range(3):
            for j in range(3):
                result[i][j] = self.data[i][j] + other.data[i][j]
        return Matrix(result)
    
    def sub(self, other):
        result = [[0,0,0], [0,0,0], [0,0,0]]
        for i in range(3):
            for j in range(3):
                result[i][j] = self.data[i][j] - other.data[i][j]
        return Matrix(result)
    
    def mul(self, other):
        result = [[0,0,0], [0,0,0], [0,0,0]]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                     result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)
            
    def trans(self, other):
        result = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(3):
            for j in range(3):
                result[j][i] = self.data[i][j]
        return Matrix(result)

if __name__ == '__main__':
    m1 = Matrix([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
    m2 = Matrix([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
    
    print("Matrix A:")
    m1.display()
    print("Matrix B:")
    m2.display()
    
    print("Addition result:")
    result_add = m1.add(m2)
    result_add.display()

    print("Subtraction result:")
    result_sub = m1.sub(m2)
    result_sub.display()

    print("Multiplication result:")
    result_mul = m1.mul(m2)
    result_mul.display()

    print("Transpose result:")
    result_trans = m1.trans(m2)
    result_trans.display()