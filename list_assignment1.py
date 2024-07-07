#A list contains 3 black balls, 4 yellow balls, 5 white balls. if you pick a
#yellow ball, print it with a message  should be done using python function
def random_pick():
 ball_list=["black ball", "yellow balls", "white balls"]
 for i in ball_list:
  print("pick a ball")
  i=input()
  if i=="yellow":
   print("I have picked a yellow ball !")
  else:
   print("I have picked a wrong ball !")
   break
random_pick()


