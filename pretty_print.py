
# Import required libraries
import json
  
# Read JSON data from file and pretty print it
with open("dr_d1.json", "r", encoding="utf-8-sig") as read_file:
    # Convert JSON file to Python Types
    obj = json.load(read_file)
  
with open("dr_d1_formatted.json", "w") as write_file:
    json.dump(obj, write_file, indent=4)