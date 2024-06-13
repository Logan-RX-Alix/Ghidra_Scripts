 #simple script to extract strings like potential output from analyzed binary to console and a .txt in home dirrectory.
#@Logan Alix
#@category String
#@keybinding
#@menupath
#@toolbar

from ghidra.program.model.listing import CodeUnit, Data
from ghidra.program.model.data import StringDataType
from ghidra.util import Msg
import os

# Create a list to hold strings
strings_list = []

# Function to process each string data
def process_string(string_data):
    try:
        # Get the string value
        string_value = string_data.value
        strings_list.append(string_value)
    except:
        pass

# Get the current program being analyzed
current_program = currentProgram

# Get the data manager for the current program
data_manager = current_program.getListing()

# Iterate through all data in the program
for data in data_manager.getDefinedData(True):
    # Check if the data type is a string
    if isinstance(data.getDataType(), StringDataType):
        process_string(data)

# Print the strings
for string in strings_list:
    print(string)

# Specify the output file path
output_file_path = "/path/to/your/desired/location/ghidra_extracted_strings.txt"

# Export the strings to the specified file
with open(output_file_path, "w") as output_file:
    for string in strings_list:
        output_file.write(string + "\n")

# Print completion message
Msg.info("Ghidra Script", "String printing and export completed. Exported to {}".format(output_file_path))
