def generate_Khayyam_triangle(rows):
    if rows == 1: return [[1]]

    triangle = [[1], [1, 1]] 

    row = [1, 1] 

    for i in range(2, rows):
        row = [1] + [sum(column) for column in zip(row[1:], row)] + [1]
        triangle.append(row)

    return triangle

for row in generate_Khayyam_triangle(int(input("n: "))):
    print (row)