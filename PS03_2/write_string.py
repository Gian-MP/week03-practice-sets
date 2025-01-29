with open('string.txt', 'w') as file:
    colors = ["black", "blue", "red", "green", "yellow", "white"]
    for x in colors:
       file.write(f"{x}  \n")
        