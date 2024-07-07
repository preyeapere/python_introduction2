#write a python function  code to add numbers below together, print out the sum
#check if the total is greater than 50, if yes, divide by 20 and add 19.otherwise add 500
list1=[12,154,79,134,3,10]
def add_sum():
    total_number=0
    for i in list1:
        total_number=total_number+i
    print(total_number)

    if total_number>50:
        result=(total_number/20)+19
        print(result)
    else:
       result=total_number+500
       print(result)

add_sum()