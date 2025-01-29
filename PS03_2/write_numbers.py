with open('numbers.txt', 'w') as file:
    nums = [1,2,3,4,5]
    for x in nums:
       file.write(f"{x}  \n")
        