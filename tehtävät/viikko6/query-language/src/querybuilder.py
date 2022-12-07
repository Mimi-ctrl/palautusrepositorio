from matchers import All, PlaysIn, And, HasAtLeast, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, query=None):
        if not query:
            query = All()
        self.query = query
    
    def playsIn(self, i):
        return QueryBuilder(And(self.query, PlaysIn(i)))

    def hasAtLeast(self, i, y):
        return QueryBuilder(And(self.query, HasAtLeast(i, y)))

    def hasFewerThan(self, i, y):
        return QueryBuilder(And(self.query, HasFewerThan(i, y)))

    def oneOf(self, *matchers):
        return QueryBuilder(Or(*matchers))

    def build(self):
        return self.query
