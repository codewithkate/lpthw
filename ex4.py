# input value for the variable cars / # of cars
cars = 100
# input value for the variable space_in_a_car / # of spaces in each car
space_in_a_car = 4.0
# input value for the variable drivers / # of drivers
drivers = 30
# input value for the variable passengers / # of passengers
passengers = 90
# calculates the number of cars that will not be driven: 100 - 30
cars_not_driven = cars - drivers
# the # of cars that are driven is the same as the # of drivers
cars_driven = drivers
# total number of people who can ride in the carpool
carpool_capacity = cars_driven * space_in_a_car
# total number of passengers in each car
average_passengers_per_car = passengers / cars_driven

# prints how many cars are available based on line 2
print("There are", cars, "cars available.")
# prints how many drivers are available based on line 6
print("There are only", drivers, "drivers available.")
# prints how many cars are not going to be driven based on line 12
print("There will be", cars_not_driven, "empty cars today.")
# prints how many people can carpool based on line 14
print("We can transport", carpool_capacity, "people today.")
# prints the number of passengers based on line 8
print("We have", passengers, "to carpool today.")
# prints the number of passengers in each car based on line 16
print("We need to put about", average_passengers_per_car,
"in each car.")

# File "ex4.py", line 8, in <module>
#    average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined
## This is wrong because there is an _ between car and pool. There is not a value called car_pool to call on for the function.
