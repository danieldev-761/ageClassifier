#The objective of this project is to correctly 
# classify according to age groups (child, teen, adult, senior).


# This function gets the user's age as input and returns it as an integer.
def get_user_data():
    age = int(input("Enter your age: "))
    return age

#This function classifies the age into categories based on the following criteria:
def classify_age(age):
    if age < 13:
        return "child"
    elif 13 <= age < 18:
        return "teen"
    elif 18 <= age < 60:
        return "adult"
    else:
        return "senior"
    

#Calling the functions to get user data and classify it into a category.   
category= classify_age(get_user_data())


#This function takes the classified category as input and prints it to the user.    
def show_category(category):
    print(f"You are classified as: {category}")


show_category(category)