print("Welcome to the Band Name Generator")
city = input("What's the name of the city you grew up in?\n")
petsName = input("What's your pet's name\n")
print(f"Your band name could be {city} {petsName}")

# I tried to make the code harder by using loops to check if the user's input was anything besides what I was asking,
# this is my version with loops that had a structure error because I did not include the inputs inside the while loop

# print("Welcome to the Band Name Generator")
# city = input("What's the name of the city you grew up in?\n")
# petsName = input("What's your pet's name\n")
#
# flag = True
#
# while flag == True and city != str and petsName != str:
#     print("Insert valid names")
#     flag = False
# if city == str and petsName == str:
#         print("Welcome to the Band Name Generator")
#         city = str(input("What's the name of the city you grew up in?\n"))
#         petsName = str(input("What's your pet's name\n"))
#         print(f"Your band name could be {city} {petsName}")


# Improved Version

# print("Welcome to the Band Name Generator")
# flag = True
#
# while flag:
#     city = input("What's the name of the city you grew up in?\n")
#     petsName = input("What's your pet's name\n")
#
#     if city != str or petsName != str:
#         print("Insert valid names")
#     else:
#         print(f"Your band name could be {city} {petsName}")
#         flag = False