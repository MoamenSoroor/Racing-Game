

l = [[1,2,3,4], [5,6,7,8] ,[9,10,11,12],  [13,14,15,16]]
l2 = []
for i in range(len(l)):
    row = []
    for j in range(len(l[0])):
        print(i,j)
        row.append(l[j][i])
    l2.append(row)


print(l2)