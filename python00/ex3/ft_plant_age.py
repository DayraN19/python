def ft_plant_age():
    PLANT_AGE = int(input("Enter the age of the plant in days: "))
    if PLANT_AGE < 60:
        print("Plant needs more time to grow.")
    elif PLANT_AGE >= 60:
        print("Plant is ready to harvest!")


ft_plant_age()
