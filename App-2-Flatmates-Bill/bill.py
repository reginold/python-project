class Bill:
	"""[summary]

	Returns:
	    [type]: [description]
	"""
	def __init__(self, amount, period) -> None:
	    self.amount = amount
	    self.period = period

	    
class Flatmate:
	"""[summary]
	"""
	def __init__(self, name, days_in_house) -> None:
	    self.name = name
	    self.day_in_house = days_in_house

	def pays(self, bill, flatemate2):
		weight = bill.amount / (self.day_in_house + flatemate2.day_in_house)
		return self.day_in_house * weight