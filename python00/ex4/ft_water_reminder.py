def ft_water_reminder():
    DSW = int(input("The number of days since the plant was last watered:"))
    if DSW > 2:
        print("Water the plants!")
    else:
        print("The plants are fine.")


ft_water_reminder()
