file_path1 = "C:\\Users\\Admin\\Documents\\PS03_3\\file1.txt"
file_path2 = "C:\\Users\\Admin\\Documents\\PS03_3\\file2.txt"
merged_path = "C:\\Users\\Admin\\Documents\\PS03_3\\merged_file.txt"

with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
    content1 = file1.read()
    content2 = file2.read()

with open(merged_path, 'w') as merged_file:
    merged_file.write(content1 + "\n" +content2) 

print("The file is created succesfully!")