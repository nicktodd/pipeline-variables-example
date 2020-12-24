import os
import json
import datetime

# access a variable
input_variable = os.getenv('input_variable')
print("the input_variable has a value of " + input_variable)


# now set a variable
print("setting an output variable named environment to the value of DEV")
os.putenv("Environment", "DEV")

# create a file containing the timestamped parameter
today = datetime.datetime.now()
dateAsString = today.strftime('%Y%m%d%H%M') 

environment_param = "TEST-"+dateAsString

parameter_file_data = {
    
        "Parameters" : {
            "Environment" : environment_param
        }
    
}
with open('dynamic_parameters.json', 'w') as outfile:    
        json.dump(parameter_file_data, outfile)


