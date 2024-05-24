class Film:
    def __init__(self, title, duration):
        self.title: str = title
        self.duration: str = duration
    
class CinemaRoom:
    def __init__(self, number, film, total_seats):
        self.number: int = number
        self.film: str = film
        self.total_seats: int = total_seats
        self.booked_seats = 0

    def book_seats(self, num_posti):
        avaliable_seats = self.total_seats - self.booked_seats
        if num_posti <= avaliable_seats:
            self.booked_seats += num_posti
            return "I confirm the avaliability of seats!"
        else:
            return "Seats are not avaliable, sorry!"
    
    def avaliable_seats(self):
        return self.total_seats - self.booked_seats
    
class Cinema:
    def __init__(self):
        self.cinema_rooms = []

    def add_cinema_room(self, cinema_room):
        self.cinema_rooms.append(cinema_room)
             
    def book_film(self, film_title, num_posti):
        for cinema_room in self.cinema_rooms:
            if cinema_room.film.title == film_title:
                return cinema_room.book_seats(num_posti)
        return "Sorry, the film isn't avaliable"
    
cinema = Cinema()

cinema_room_orion = CinemaRoom(1, Film("Barbie", 114), 100)
cinema_room_ares = CinemaRoom(2, Film("Oppenheimer", 180), 70)
cinema.add_cinema_room(cinema_room_orion)
cinema.add_cinema_room(cinema_room_ares)

print(cinema.book_film("Barbie", 20))
print(cinema.book_film("Oppenheimer", 12))
print(cinema.book_film("The Creator", 4))