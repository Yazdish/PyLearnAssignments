height = int(input("height: "))
width = int(input("width: "))
Table = []
for i in range(1,height+1):
    Table.append([])
    for j in range(1,width+1):
        Table[i-1].append([i*j])

for row in Table:
    print(row)
