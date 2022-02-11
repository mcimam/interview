for i in range(1,51):
    if(i % 3 == 0):
        print("Frontend", end="")
    
    if (i % 3 == 0 and i % 5 == 0):
        print(" ", end="")

    if (i % 5 == 0):
        print("Backend", end="")
    
    if (i % 3 != 0 and i % 5 != 0):
        print(i, end="")

    if (i != 50):
        print(",", end="")
    