from example1.movie import Movie, MOVIE
from example1.rental import Rental 
from example1.customer import Customer 


def test_addRental_in_customer():
    customer = Customer('test')
    
    m = Movie('tmovie', 0)
    r1 = Rental(m, 1)
    r2 = Rental(m, 2)

    customer.addRental(r1)
    customer.addRental(r2)

    assert customer.getRentals() == [r1, r2]


def test_statement_with_no_rental():
    name = 'test'
    customer = Customer(name) 

    assert customer.statement() == {'name': name, 'amount': [], 
                                    'totalAmount': 0, 'renterPoint': 0}


def test_statement_with_one_rental():
    name = 'test'
    customer = Customer(name) 

    m1 = Movie('movie1', MOVIE['REGULAR'])
    r1 = Rental(m1, 1)
    customer.addRental(r1)

    assert customer.statement() == {'name': name, 'amount': [{'movie1': 2}], 
                                    'totalAmount': 2, 'renterPoint': 0}
    

def test_statement_with_two_rental():
    name = 'test'
    customer = Customer(name) 

    m1 = Movie('movie1', MOVIE['REGULAR'])
    r1 = Rental(m1, 1)
    m2 = Movie('movie2', MOVIE['REGULAR'])
    r2 = Rental(m2, 2)
    customer.addRental(r1)
    customer.addRental(r2)

    assert customer.statement() == {'name': name, 
                                    'amount': [{'movie1': 2}, {'movie2': 4}], 
                                    'totalAmount': 6, 'renterPoint': 0}


def test_statement_with_renterPoint():
    name = 'test'
    customer = Customer(name) 

    m1 = Movie('movie1', MOVIE['NEW_RELESE'])
    r1 = Rental(m1, 1)
    m2 = Movie('movie2', MOVIE['NEW_RELESE'])
    r2 = Rental(m2, 2)
    customer.addRental(r1)
    customer.addRental(r2)

    assert customer.statement() == {'name': name, 
                                    'amount': [{'movie1': 3}, {'movie2': 6}], 
                                    'totalAmount': 9, 'renterPoint': 1}


def test_statement_with_renterPoint():
    name = 'test'
    customer = Customer(name) 

    m1 = Movie('movie1', MOVIE['CHILDRENS'])
    r1 = Rental(m1, 1)
    m2 = Movie('movie2', MOVIE['REGULAR'])
    r2 = Rental(m2, 2)
    m3 = Movie('movie3', MOVIE['NEW_RELESE'])
    r3 = Rental(m3, 3)
    customer.addRental(r1)
    customer.addRental(r2)
    customer.addRental(r3)

    assert customer.statement() == {'name': name, 'amount': [{'movie1': 1}, {'movie2': 4}, {'movie3': 9}], 
                                    'totalAmount': 14, 'renterPoint': 1}

