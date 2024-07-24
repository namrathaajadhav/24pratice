#membership operator
list = "hello how are you"
print('h' in list)
print('b' in list)
print('b' not in list)

valid_username = ["admin", "user1","user2"]
username = input("eneter your username:")
if username in valid_username:
     print("welcome back", username)
else:
    print("invalid username. please try again.")

 #clear
    numbers = [3,5,6,8,9,11,14]
print(numbers)
numbers.clear()
print(numbers)

#delete 
my_list = [1,2,3]
del my_list[0]
print(my_list)


#nested list

numbers = [[3,5,6],[8,9,11],[14,15,16]]
print(numbers[1][2])
for i in numbers:
    print(i)

    for i in range(len([numbers])):
          for j in  range(len(numbers[i])):
            print(numbers[i][j],end= " ")
            print()

# list comprehension
numbers = [1,2,3,4,5,6]
square = [number*number for number in numbers]
print(square)

#creating list

numbers_of_list = int(input("enter a numbers:"))
zero = []
for numbers in range(numbers_of_list):
    my_numbers = input("enter my_numbers:")
    zero.append(my_numbers)
    print(zero)




