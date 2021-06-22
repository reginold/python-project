

from bill import Bill, Flatmate

from report import PdfReport





amount = input("hey user, enter the bill amount: ")
bill_date = input("what is the bill period? E.g. December 2020: ")
name_1 = input("what is your name: ")
day_1 = input(f"how many days did {name_1} stay in the house during the bill period: ")
name_2 = input("what is name of other flatmate: ")
day_2 = input(f"how many days did {name_2} stay in the house during the bill period: ")

the_bill = Bill(1000, "April 2020")
print(the_bill.amount)
person1 = Flatmate("Lu", 15)
person2 = Flatmate("yangg", 20)
print(person2.day_in_house)
person1_pay = person1.pays(the_bill, person2)
print(person1_pay)

pdf = PdfReport('output_file.pdf')
pdf.generate(person1, person2, the_bill)
# def main(amount, name1, name2, day1, day2):
# 	day_pay = int(amount) / (int(day1) + int(day2))
# 	person1_pay = day_pay * int(day1)
# 	person2_pay = day_pay * int(day2)
# 	result_1 = f"{name1} pays: " + str(person1_pay)
# 	result_2 = f"{name2} pays: " + str(person2_pay)
# 	print(result_1)
# 	print(result_2)
# 	return result_1, result_2


# if __name__ == "__main__":
# 	amount = input("hey user, enter the bill amount: ")
# 	bill_date = input("what is the bill period? E.g. December 2020: ")
# 	name_1 = input("what is your name: ")
# 	day_1 = input(f"how many days did {name_1} stay in the house during the bill period: ")
# 	name_2 = input("what is name of other flatmate: ")
# 	day_2 = input(f"how many days did {name_2} stay in the house during the bill period: ")
# 	main(amount, name_1, name_2, day_1, day_2)