print("------------")
print("Calculator")
print("")

Operation= str(input("Insert a math operation (+, -, x, :)= "))
# pilih operasi

#Jumlah
if Operation == "+":
    firstnumber= int(input('Insert first number: '))
    secondnumber= int(input('Insert second number: '))
    Result= firstnumber+secondnumber

#Kurang
elif Operation == "-":
    firstnumber= int(input('Insert first number: '))
    secondnumber= int(input('Insert second number: '))
    Result= firstnumber-secondnumber

#Kali
elif (Operation == "x" or Operation == "X"):
    firstnumber= int(input('Insert first number: '))
    secondnumber= int(input('Insert second number: '))
    Result= firstnumber*secondnumber

#Bagi
if Operation == ":":
    firstnumber= int(input('Insert first number: '))
    secondnumber= int(input('Insert second number: '))
    Result= firstnumber/secondnumber

#Hasil
print("")
print ("The result of", str(firstnumber)+(Operation)+str(secondnumber), "is", str(Result))
print("------------")

# james dan rayya
