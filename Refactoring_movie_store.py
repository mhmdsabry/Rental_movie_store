class Movie:
	CHILDREN = 2
	REGULAR = 0
	NEW_RELEASE = 1
	def __init__(self,title,priceCode):
		self.title = title
		self.priceCode = priceCode
	def get_priceCode(self):
		return self.priceCode
	def set_priceCode(self,priceCode):
	    self.priceCode = priceCode
	def get_title(self):
		return self.title


class Rental:
	def __init__(self,Movie_instance,daysRented):
		self.movie = Movie_instance
		self.daysRented = daysRented
	def get_daysRented(self):
		return self.daysRented
	def get_movie(self):
		return self.movie
	def get_charge(self):
		this_amount = 0
		if self.get_movie().get_priceCode()== Movie.REGULAR:
				this_amount+=2
				if(self.get_daysRented()>2):
					this_amount+=(self.get_daysRented() - 2)*1.5
				
		elif self.get_movie().get_priceCode()== Movie.NEW_RELEASE:
				this_amount+= self.get_daysRented() * 3.0
				
		elif self.get_movie().get_priceCode()== Movie.CHILDREN:
				this_amount+=1.5
				if(self.get_daysRented()>3):
					this_amount+=(self.get_daysRented() - 3)*1.5
		return this_amount
	def frequent_renter_points(self):
		if self.get_movie().get_priceCode() == Movie.NEW_RELEASE and self.get_daysRented()>1:
			return 2
		else:
			return 1



class Customer:
	def __init__(self,name,rental):
		self.name = name
		self.rental = rental
	def addRental(self,rental):
		self.rental.append(rental)
	def get_name(self):
		return self.name
		
	def statement(self):
		total_amount = 0
		frequent_renter_points = 0
		result = 'Rental Record for '+ self.get_name()+"\n"
		for movie,daysRented in self.rental.items():
			aRental = Rental(movie,daysRented)
			frequent_renter_points+=aRental.frequent_renter_points()
			result += "\t"+ aRental.get_movie().get_title() + "\t" + str(aRental.get_charge()) + "\n"
			total_amount+=aRental.get_charge()
		result += "Amount owed is "+str(total_amount)+"\n"
		result += "You earned "+str(frequent_renter_points)+" frequent renter points"
		return result
	