with open('source.txt', 'w') as file:
    file.write(f"Hello World\n")
    file.write(f"This is appended text")
with open('source.txt', 'r') as file:
    source_file = file.read()
with open('destination.txt', 'w') as destined_file:
    destined_file.write(source_file)
    