from example1.movie import Movie, MOVIE
from example1.rental import Rental 
from example1.customer import Customer 


def test_create_movie():
    title = 'test'
    priceCode = 1
    movie = Movie(title, priceCode)

    assert movie.getPriceCode() == priceCode
    assert movie.getTitle() == title
    
    priceCode = 2
    movie.setPriceCode(priceCode)
    assert movie.getPriceCode() == priceCode

    assert MOVIE == {'CHILDRENS': 1, 'REGULAR': 2, 'NEW_RELESE': 3}


def test_create_rental():
    movie = Movie('test', 1)
    daysRented = 1 
    rental = Rental(movie, daysRented)

    assert rental.getDaysRented() == daysRented
    assert rental.getMovie() == movie


def test_create_customer():
    name = 'test' 
    customer = Customer(name)
    
    assert customer.getName() == name

