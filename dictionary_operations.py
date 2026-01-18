# Dictionary Operations Program

# Creating a dictionary
student = {
    "name": "Rahul",
    "roll_no": 101,
    "marks": 85
}

print("Original Dictionary:", student)

# Adding a new key-value pair
student["branch"] = "ECE"
print("After adding branch:", student)

# Updating an existing value
student["marks"] = 90
print("After updating marks:", student)

# Removing an item
student.pop("roll_no")
print("After removing roll number:", student)

# Printing all keys
print("Keys:", student.keys())

# Printing all values
print("Values:", student.values())
