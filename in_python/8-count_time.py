import time

# Initialize minute and hour counters
count_min = 0
count_hour = 0

# Display a starting message
print("Let's get started :)")

# Infinite loop to simulate time passing
while True:
    # Check if the minute counter is at the start
    if count_min == 0:
        print("We have started the calculation")
    # Check if the minute counter is less than 60
    elif count_min < 60:
        # Determine the appropriate text for singular or plural form of "minute"
        minute_text = "minute" if count_min == 1 else "minutes"
        # Display the time that has passed in minutes
        print("{} {} have passed".format(count_min, minute_text))
    # Check if the minute counter has reached 60
    elif count_min == 60:
        # Reset minute counter and increment hour counter
        count_min = 0
        count_hour += 1
        # Determine the appropriate text for singular or plural form of "hour"
        hour_text = "hour" if count_hour == 1 else "hours"
        # Display the time that has passed in hours
        print("{} {} have passed".format(count_hour, hour_text))
    
    # Increment the minute counter
    count_min += 1
    
    # Pause the program for 60 seconds (1 minute)
    time.sleep(60)
