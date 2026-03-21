mat1 = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
flat = [x for row in mat1 for x in row]
print(flat)