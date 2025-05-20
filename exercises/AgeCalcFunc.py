from datetime import datetime
import Person

Name = str(input("Please enter your name: "))
Country = str(input("Please enter the name of the country you're residing in: "))
DateOfBirth = datetime.strptime(input("Please enter your date of birth (e.g. D M YYYY): "), '%d %m %Y')
Occupation = str(input("Please enter your occupation: "))
person1 = Person.Person(Name, Country, DateOfBirth, Occupation)
now = datetime.now()
print("Hi, " + str(person1.name) + ". You're " + str(person1.AgeCalc()) + " years old as of " + str(now.strftime("%d-%m-%Y")))