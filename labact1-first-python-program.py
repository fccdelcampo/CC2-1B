#   PROGRAMMED BY: Francis Carlo C. Del Campo (CC2 CITCS 1B)
#   PROGRAM DATE: September 9, 2023
#   PROGRAM TITLE: FirstPythonProgram.py


lbs = input("Enter weight in pounds (lbs): ")

if float(lbs) == 1:
    textweight = " pound in kilograms "
else:
    textweight = " pounds in kilograms "

kilograms = 0.45359237
kg = (kilograms * float(lbs))
print(lbs + textweight + str(kg) + " kilograms")
print("=================================")

miles = input("Enter distance in miles (mi): ")

if float(miles) == 1:
    textdist = " mile in kilometers "
else:
    textdist = " miles in kilometers "

kilometers = 1.60934
km = (kilometers * float(miles))
print(miles + textdist + str(km) + " kilometers")
print("==================================")

Fahrenheit = input("Enter temperature in Fahrenheit: ")
Celsius = ((float(Fahrenheit) - int(32)) / 1.8)
print(Fahrenheit + "° Fahrenheit in Celsius: " + str(Celsius) + "°")
print("==================================")

counter = 0
sum = 0
string = "Age of Student "
while counter < 10: 
    counter = counter + 1
    age = int(input(string + str(counter) + ": "))
    sum = sum + age
average = sum / 10
print("The average age of the students is ", average)
print("==================================")

mainCharacter = "~Stephen~"
deity = "<God>"
newCharacter = "~Buddha~"
sonOfGod = "<Jesus>"
fuhrer = "~Hitler~"

print('One day, a man who died of cardiac arrest gets transported into the afterlife. ')
print(deity + ' greets him, "' + mainCharacter + ', welcome to the afterlife! Forget everything for now."')
print('"Is this heaven?" Stephen asks. "Sort of. This is where all life of all time gather ')
print('when they die.", God replies. "Why am I the only human here?" Stephen asks. "Because')
print('you are the only human to ever exist. All people on Earth had once been you, before ')
print('you were reincarnated as Stephen. You were once ' + sonOfGod + ', and even ' + fuhrer + '. The man ')
print('confusingly exclaimed, “WHA—." But God reveals, "There is only one representative of ')
print('each species. You’re reincarnated every time you die." Stephen asks more, to which ')
print('God says, “Soon, you’ll learn. Time to go back to Earth, son. You’ll be reincarnated ')
print('as ' + newCharacter + '." Stephen returns, and Buddha is born thereafter."')
