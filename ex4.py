cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available"
print "There are only",drivers,"drivers available"
print "There will be", cars_not_driven,"empty cars today."
print "We can transport", carpool_capacity,"people today"
print "We have", passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car"

# Study Drills
# 1. error 'car_pool_capacity' is not defined is because such a variable name doesnt exist. the variable is carpool_capacity
# 2. using 4.0 is not necessary, it is better not to use it, as the carpool_capacity then shows only whole numbers, which is more meaningful when we relate to people
# 3. Not writing comments for now

