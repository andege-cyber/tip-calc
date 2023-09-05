print("\033[1mInput\033[0m") #\033[1m and \033[0m ere used to bolden the text
charge = float(input("Enter charge for food ="))
print("Charge for food = "+ str(charge))
print() #addes an empty new line in the output

print("\033[1mOutput\033[0m")
Tax= float(18/100 * charge)
print("Tax = " +"$"+str(Tax))
Salestax= float(7/100 * charge)
print("Sales tax = " +"$"+str(Salestax))
Grandtotal= float(charge + Tax + Salestax)
print("Grand total = " +"$"+str(Grandtotal))