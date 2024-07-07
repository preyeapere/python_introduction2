#Write a user input python function code that will ask for your name, designation,
#email address, phone number and print the details
def personal_details():
    print("what is your Full Name")
    name=input()
    print("State your designation")
    designation=input()
    print("what is your email address")
    email_address=input()
    print("what is your phone Number")
    phone_Number=input()
    print("This are your personal details " + name + "," + designation + "," + email_address + "," + phone_Number)
personal_details()