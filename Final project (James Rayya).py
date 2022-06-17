print("------------")
print("Calculator")
print("")

Operation= input("Insert a math operation (+, -, :, x)= ")
# pilih operasi yg mana


#Jumlah
if Operation == "+":
    firstnumber= int(input('Insert first number: '))
    secondnumber= int(input('Insert second number: '))
    Result= firstnumber+secondnumber


#Kali
if Operation == "x":
    firstnumber= int(input('Insert first number: '))
    secondnumber= int(input('Insert second number: '))
    Result= firstnumber*secondnumber
if Operation == "X":
    firstnumber= int(input('Insert first number: '))
    secondnumber= int(input('Insert second number: '))
    Result= firstnumber*secondnumber


#hasil
print("")
print ("The result of", (f"{firstnumber}{Operation}{secondnumber}"), "is", Result)
print("------------")

# james dan rayya