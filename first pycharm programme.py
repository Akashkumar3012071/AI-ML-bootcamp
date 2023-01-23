class InvalidAccountCreation(Exception):
    def __str__(self):
        return "You are not eligible to create a facebook account."


age = int(input("Enter your age "))

try:
    if age < 16:
        raise InvalidAccountCreation
    else:
        print("Account Created Successfully!")

except InvalidAccountCreation as iac:
    print(iac)

print("details checked")
