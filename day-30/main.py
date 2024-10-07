## FileNotFound
# with open("a_file.txt") as file:
#     file.read()

## KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

## IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

## TypeError
# text = "abc"
# print(text + 5)

## -------------------------------------------------------------------------

# # File Not Found
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["non_existent_key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} doesn't exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error message I made up")
#     file.close()

## -------------------------------------------------------------------------

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height is not over 3 meters")
bmi = weight / height ** 2
print(bmi)
