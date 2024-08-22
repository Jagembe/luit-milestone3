# This list contains tuples, where each tuple represents a flight connection
# The structure of each tuple is (Starting City, Destination City, Flight Time in Minutes)
connections = [
    ('Amsterdam', 'Dublin', 100),  # Flight from Amsterdam to Dublin with a duration of 100 minutes
    ('Amsterdam', 'Rome', 140),    # Flight from Amsterdam to Rome with a duration of 140 minutes
    ('Rome', 'Warsaw', 130),       # Flight from Rome to Warsaw with a duration of 130 minutes
    ('Minsk', 'Prague', 95),       # Flight from Minsk to Prague with a duration of 95 minutes
    ('Stockholm', 'Rome', 190),    # Flight from Stockholm to Rome with a duration of 190 minutes
    ('Copenhagen', 'Paris', 120),  # Flight from Copenhagen to Paris with a duration of 120 minutes
    ('Madrid', 'Rome', 135),       # Flight from Madrid to Rome with a duration of 135 minutes
    ('Lisbon', 'Rome', 170),       # Flight from Lisbon to Rome with a duration of 170 minutes
    ('Dublin', 'Rome', 170)        # Flight from Dublin to Rome with a duration of 170 minutes
]

# Initialize a counter to track the number of flights that lead to Rome
counter = 0

# Initialize a variable to accumulate the total flight time for flights that lead to Rome
sum = 0.0

# Iterate over each flight connection in the 'connections' list
for con in connections:
    # Check if the destination city of the current flight is 'Rome'
    if con[1] == 'Rome':
        counter += 1       # Increment the counter by 1 for each flight that ends in Rome
        sum += con[2]      # Add the flight time of the current flight to the total sum

# After the loop, the counter holds the number of flights that lead to Rome,
# and 'sum' holds the total flight time of all those flights.

# Calculate the average flight time by dividing the total sum by the number of flights (counter)
# Print the results: the number of flights and the average flight time
print(counter, 'connections lead to Rome with an average flight time of', sum/counter, 'minutes')
