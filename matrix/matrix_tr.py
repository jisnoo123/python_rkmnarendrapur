#Transpose of a matrix

m = int(input('Enter no. of rows:'))
n = int(input('Enter no. of cols:'))

matrix = list()

# Matrix element input
for i in range(m):
    row = list()
    for j in range(n):
        print('Enter a[',i,'][',j,']:')
        row.append(int(input()))
    matrix.append(row)

print('Original matrix:', matrix)

# Matrix transpose

mat_tr = list()

for i in range(n):
    col = list()
    for j in range(m):
        col.append(matrix[j][i])
    mat_tr.append(col)

print('Matrix transpose', mat_tr)