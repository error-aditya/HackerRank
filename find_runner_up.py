# # class sports_day:
# #     def running(self):
# #         n = int(input())
# #         list1 = set(map(int,input().split()))
# #         find = list(list1)
# #         find.sort(reverse = True)
# #         return print(find[1])

# # sports = sports_day()
# # sports.running()

# n = int(input())

# num = list(map(int,input().split()))

# print(num)
user_input = input("Enter a number: ")  # Take the initial input
first_digit = user_input[0]  # Get the first character

# Check if the first character is a digit
if first_digit.isdigit():
    first_digit = int(first_digit)  # Convert it to an integer

    # Take input based on the first digit
    inputs = []
    for i in range(first_digit):
        value =list(map(int,input(f"Enter input {i+1}: ").split())) # Take input
        inputs.append(value)

    # Display the collected inputs
    print("Collected Inputs:", inputs)

else:
    print("Invalid input! Please enter a valid number.")
