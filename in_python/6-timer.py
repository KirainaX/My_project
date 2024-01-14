import time

# Loop through hours (0 to 23)
for i in range(24):
    # Loop through minutes (0 to 59)
    for j in range(60):
        # Loop through seconds (0 to 59)
        for k in range(60):
            # Check the current time and print in the specified format
            if i == 0 and j == 0 and k == 0:
                print("00:00:00")
            elif i == 0 and j == 0 and 10 > k > 0:
                print("00:00:0{}".format(k))
            elif i == 0 and j == 0 and k >= 10:
                print("00:00:{}".format(k))
            elif i == 0 and 10 > j > 0 and 10 > k > 0:
                print("00:0{}:0{}".format(j, k))
            elif i == 0 and j >= 10 and k >= 10:
                print("00:{}:{}".format(j, k))
            elif 10 > i > 0 and 10 > j > 0 and 10 > k > 0:
                print("0{}:0{}:0{}".format(i, j, k))
            elif i >= 0 and j >= 10 and k >= 10:
                print("{}:{}:{}".format(i, j, k))

            # Add a one-second delay between each iteration
            time.sleep(1)
