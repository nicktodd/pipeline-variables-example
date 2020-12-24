import os


# access a variable
input_variable = os.getenv('input_variable')
print("the input_variable has a value of " + input_variable)

# access GIT commit ID
# to be added later

# now set a variable
print("setting an output variable named environment to the value of DEV")
os.putenv("environment", "DEV")


    