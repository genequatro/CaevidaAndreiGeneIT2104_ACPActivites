character = input("Enter two spaced-seperated characters: ").split()

print("-----------------------------")
print("The character with the greater value is: " + max(character))
print("-----------------------------")

print("Showing ASCII Values: ")
print(str(character[0]) +" : " + str(ord(character[0]))) 
print(str(character[1]) +" : " + str(ord(character[1]))) 

