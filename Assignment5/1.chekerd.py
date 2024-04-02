a = []
def chesss(n,m):
    for j in range(m):
        a.append([])
        for i in range(n):
            if i % 2 != 0:
                a[j].append("#")
            else:
                a[j].append("*")
chesss(int(input("n: ")), int(input("m: ")))
for row in a:
     print(row)
     
