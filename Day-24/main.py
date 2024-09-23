# file = open("my_file.txt")
# with open("C:/Users/seanh/Desktop/my_file.txt") as file:
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# with open("new_file.txt", mode="w") as file:
#     file.write("New Text.")
