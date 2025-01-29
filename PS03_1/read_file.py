file_path = "C:\\Users\\Admin\\Documents\\codes\\example.txt"

file = open(file_path, 'r')

count_line = 0
count_word = 0
count_cha = 0


for line in file:
    print(line.strip())
 
    count_line += 1
    count_word += sum(1 for word in line.split())
    count_cha += sum(1 for char in line)

file.close()

print("Lines: ", count_line)
print("Words: ", count_word)
print("Characters: ", count_cha)




