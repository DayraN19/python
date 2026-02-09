def ft_count_harvest_recursive():

    def count(day, max_day):
        if day > max_day:
            print("Harvest time!")
            return
        print(f"Day {day}")
        count(day + 1, max_day)

    max_day = int(input("Days until harvest: "))
    count(1, max_day)


ft_count_harvest_recursive()
