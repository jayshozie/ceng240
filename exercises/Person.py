from datetime import date

class Person:
    def __init__(self, firstName, country, dateOfBirth, occupation, height, weight):
        self.firstName = firstName
        self.country = country
        self.dateOfBirth = dateOfBirth
        self.occupation = occupation
        self.height, self.weight = height, weight
        self.BMI = self.BodyMassIndex()
    def AgeCalc(self):
        today = date.today()
        age = today.year - self.dateOfBirth.year
        if today < date(today.year, self.dateOfBirth.month, self.dateOfBirth.day):
            age -= 1
        return age
    
    def BodyMassIndex(self):
        BMI = self.weight / (self.height**2)
        return BMI

# Emir = Person("Emir Baha Yildirim", "Turkiye", date(2005, 8, 1), "Student", 1.78, 75)
# print(Emir.AgeCalc())
# person = Person("Elizabeth II", "UK", date(1930, 1, 11), "The Queen", 1.56, 60)
# print(person.BMI)