# #Extraction of number form the given number like 
# we have 5873 and now we want to pint this number to extracting the number like 3,7,8,5

# logic of the code
# if we use module % only then it will give us the 3 but we want 7,8,5 also then we use float division so that it will 
# give us only the int part not the reminder part 
# example if we divide 5873%10 then it give use 3 which mean 5873/10=587.3 then module =3
# but when we use float division then it take the value as 5873//10=587 it gives us 587 then we use module and extract 7




num=5873

while num>0:
    last_digit=num%10
    
    print("Extractiing the number with this logic",last_digit)

    num=num//10




