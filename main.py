# Author: Jacob Noethiger jln5438@psu.print
temp=input("Enter temperature: ")
temp=float(temp)
unit=input("Enter unit in F/f or C/c: ")
if(unit=='f' or unit=='F'):
  ctemp=(temp-32)*5/9
  print(f"{temp}° in Fahrenheit is equivalent to {ctemp}° Celsius.")
elif(unit=='c' or unit =='C'):
  ftemp=(temp*9/5)+32
  print(f"{temp}° in Celsius is equivalent to {ftemp}° Fahrenheit.")
else:
  print("Invalid unit("+unit+").")
