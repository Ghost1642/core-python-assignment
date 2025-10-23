def book_seat(booked, seat, total):
    if seat in booked or seat > total or seat < 1:
        return booked
    booked.append(seat)
    return booked
def cancel_seat(booked, seat):
    if seat in booked:
        booked.remove(seat)
    return booked
total_seats = 10
booked_seats = [2, 5, 7]
book_seat_num = 3
cancel_seat_num = 5
booked_seats = book_seat(booked_seats, book_seat_num, total_seats)
booked_seats = cancel_seat(booked_seats, cancel_seat_num)
available_seats = [i for i in range(1, total_seats+1) if i not in booked_seats]
print("Available seats:", available_seats)
