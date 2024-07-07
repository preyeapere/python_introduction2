#add cassavaflour to a list of item given below  and
#ii.check if carrot is in the list below and print a message “yes it is there or not
#python code that removes kola from the list in no3.

def add_items():
 listofitems=["cucumbar","kola","groundnut","pineapple","carrot","grape"]
 listofitems.insert(0,"cassava flour")
 print(listofitems)

 if "carrot" in listofitems:
  print("yes it is there")

 else:
  print("no it is not there")

add_items()


