from movie import Movie, MOVIE
from rental import Rental 


class Customer:

    def __init__(self, name):
        self._rentals = []
        self._name = name

    def getName(self):
        return self._name

    def addRental(self, rental):
        self._rentals.append(rental)

    def getRentals(self):
        return self._rentals
        
    def statement(self):
        totalAmount = 0
        renterPoint = 0
        amountList = []

        for rental in self._rentals:
            movie = rental.getMovie()
            amount = movie.getPriceCode() * rental.getDaysRented()
            amountList.append({movie.getTitle(): amount}) 
            totalAmount += amount

            if movie.getPriceCode() == MOVIE['NEW_RELESE']:
                if rental.getDaysRented() >= 2:
                    renterPoint += 1

        return {'name': self._name, 'amount': amountList,
                'totalAmount': totalAmount, 'renterPoint': renterPoint}

