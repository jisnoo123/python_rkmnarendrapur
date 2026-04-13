# Rotate list
import math

# Input
print('List Input:')
inp_list = list()

while True:
    inp = input('Enter number:')

    if inp=='done':
        break

    inp = int(inp)
    inp_list.append(inp)

# Rotate
rotated = list()

k = int(input('Enter k:'))
times = int(math.ceil(len(inp_list)/k))

for i in range(1, times+1):
    prev = (k*i) - k -1
    for j in range((k*i)-1, prev, -1):
        if j<len(inp_list):
            rotated.append(inp_list[j])
    
# Display result
print(f'Input list {inp_list}')
print(f'Rotated list {rotated}')