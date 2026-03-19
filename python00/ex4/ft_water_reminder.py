def ft_water_reminder():
    dsw = int(input("Days since last watering:"))
    if dsw > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
