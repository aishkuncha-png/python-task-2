# datatypes_demo.py
# This is the name of the Python script file

# Step 1: Variable declaration
# Declares an integer variable to store age
age = 21

# Declares a float variable to store height
height = 5.9

# Declares a string variable to store a name
name = "Alex"

# Declares a boolean variable to indicate student status
is_student = True


# Step 2: Print data types
# Prints the data type of the variable 'age'
print(type(age))

# Prints the data type of the variable 'height'
print(type(height))

# Prints the data type of the variable 'name'
print(type(name))

# Prints the data type of the variable 'is_student'
print(type(is_student))


# Step 3: Arithmetic operations
# Declares an integer variable with value 10
num1 = 10

# Declares another integer variable with value 3
num2 = 3

# Adds num1 and num2 and prints the result
print("Addition:", num1 + num2)

# Subtracts num2 from num1 and prints the result
print("Subtraction:", num1 - num2)

# Multiplies num1 and num2 and prints the result
print("Multiplication:", num1 * num2)

# Divides num1 by num2 and prints the result as a float
print("Division:", num1 / num2)


# Step 4: Type conversion
# Starts a try block to handle potential errors
try:
    # Takes input from the user (input is always a string)
    user_input = input("Enter a number: ")

    # Converts the string input into an integer
    number_int = int(user_input)

    # Converts the string input into a float
    number_float = float(user_input)

    # Prints the converted integer value
    print("Integer:", number_int)

    # Prints the converted float value
    print("Float:", number_float)

# Executes if the input cannot be converted to a number
except ValueError:
    # Prints an error message if conversion fails
    print("Invalid input! Please enter numbers only.")


# Step 5: String and number concatenation
# Prints string and integer together using comma (automatic conversion)
print("Age is", age)

# Converts integer to string and concatenates it with another string
print("Age is " + str(age))


# Step 6: Dynamic typing
# Assigns an integer value to variable 'value'
value = 10

# Prints the value and its data type
print(value, type(value))

# Reassigns the same variable with a string value
value = "Ten"

# Prints the new value and its new data type
print(value, type(value))

# Reassigns the same variable with a float value
value = 10.5

# Prints the updated value and its updated data type
print(value, type(value))
