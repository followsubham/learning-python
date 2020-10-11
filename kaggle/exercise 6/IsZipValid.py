#There is a saying that "Data scientists spend 80% of their time cleaning data, and 20% of their time complaining about cleaning data." Let's see if you can write a function to help clean US zip code data. Given a string, it should return whether or not that string represents a valid zip code. For our purposes, a valid zip code is any string consisting of exactly 5 digits.

def is_valid_zip(zip_code):
    Valid=False
    only_number=False
    """Returns whether the input string is a valid (5 digit) zip code
    """
    if len(zip_code)==5 and zip_code.isdigit(): #NewLearning
             valid= True
    else:
            valid=False
    return valid