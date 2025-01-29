file_path = "C:\\Users\\Admin\\Documents\\PS03_3\\random_words.txt"
counted_path =  "C:\\Users\\Admin\\Documents\\PS03_3\\word_frequencies.txt"
target_word = "apple"

with open(file_path, 'r') as file:
    content = file.read().lower()

word_count = content.split().count(target_word.lower())

with open(counted_path, 'w') as new_file:
    new_file.write(f"The word {target_word} appears {word_count} times in the file.\n")


print("The file is created succesfully!")