# Travis Goode
# 10/6/2024
# Assignment Name: P2LAB2
# Calculates gallons of gas needed per mile driven

# Dictionary
my_dict = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# calls
keys = my_dict.keys()

# Why would I have this printed and like this rather than just call them from the dict to print
print("dict_keys(['Camaro', 'Prius', 'Model S', 'Silverado'])")
print()

# Vehicle
selected_vehicle = input("Enter a vehicle to see it's mpg: ")
print()


#miles
mpg = my_dict[selected_vehicle]
print(f"The {selected_vehicle} gets: {mpg} mpg.")
print()

#distance
miles = float(input(f"How many miles will you drive the {selected_vehicle}?: "))
print()


gallons_needed = miles / mpg


print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {selected_vehicle} {miles} miles.")
print()
