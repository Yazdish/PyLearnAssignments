import random

def non_repeating_random_2D_array(rows,cols):
  
    random_numbers = []
    cells = rows * cols                      
    while (len(random_numbers)) < cells:
        
        x = random.randint(1, cells)

        if x in random_numbers:
            random_numbers.remove(x)
            random_numbers.append(x)
        else:
            random_numbers.append(x)


    l= random_numbers
    
    return [l[i:i + cols] for i in range(0, len(l), cols)]