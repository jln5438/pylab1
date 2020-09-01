# Author: Jacob Noethiger jln5438@psu.print
temp=input("Enter temperature: ")
unit=input("Enter unit in F/f or C/c: ")
if(unit=='f' or unit=='F'):
  temp=(temp-32)*5/9
elif(unit=='c' or unit ='C'):
   