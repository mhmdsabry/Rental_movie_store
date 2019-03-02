from movie_store import *

#test_data
movie1 = Movie('Black Panther',1)
movie2 = Movie('Thor',0)
movie3 = Movie('Secret life of pets',2)
rental = {movie1:5,movie2:4,movie3:3}
customer = Customer('Sabry',rental)

#self_checking
assert customer.statement() == 'Rental Record for '+'Sabry'+'\n'+'\t'+'Black Panther'+'\t'+'15.0'+'\n'+'\t'+'Thor'+'\t'+'5.0'+'\n'+'\t'+'Secret life of pets'+'\t'+'1.5'+'\n'+'Amount owed is '+'21.5'+'\n'+'You earned '+'4'+' frequent renter points' ,'Test is FAILED'

