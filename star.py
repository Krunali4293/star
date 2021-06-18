print("****Pattern Printing using star****")
rows=int(input("Enter the row height:"))
print("1 for true and 0 for false")
bool_var=input("Enter 1 or 0:")
if bool_var=="1":
    for i in range(1,rows+1):
        print("*"*i)
if bool_var=="0":
    for i in range(rows,0,-1):
        print("*"*i)


