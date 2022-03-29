bookings = [[1, 10], [5, 10], [11, 20]]


start_day = min([booking[0] for booking in bookings])
end_day = max([booking[1] for booking in bookings])


current_rented_cars = 0
rented_cars_history = [0]


for day in range(start_day, end_day+1):
    for booking in bookings:
        if day == booking[0]:
            current_rented_cars += 1
            rented_cars_history.append(current_rented_cars)
        elif day == booking[1]:
            current_rented_cars -= 1
            rented_cars_history.append(current_rented_cars)

print('Min number of cars required: ', max(rented_cars_history))
