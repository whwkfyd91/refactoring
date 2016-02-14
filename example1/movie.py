
class Movie:

    def __init__(self, title, priceCode):
        self._title = title
        self._priceCode = priceCode

    def setPriceCode(self, priceCode):
        self._priceCode = priceCode

    def getPriceCode(self):
        return self._priceCode

    def getTitle(self):
        return self._title

MOVIE = {'CHILDRENS': 1, 'REGULAR': 2, 'NEW_RELESE': 3}

