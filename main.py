# Author: Jacob Noethiger jln5438@psu.print
temp=input("Enter temperature: ")
temp=float(temp)
unit=input("Enter unit in F/f or C/c: ")
if(unit=='f' or unit=='F'):
  ctemp=(temp-32)*5/9
  print(str(temp)+"° in Fahrenheit is equivalent to "+str(ctemp)+"° Celsius.")
elif(unit=='c' or unit =='C'):
  ftemp=(temp*9/5)+32
  print(str(temp)+"° in Celsius is equivalent to "+str(ftemp)+"° Fahrenheit.")
else:
  print("Invalid unit("+unit+").")
