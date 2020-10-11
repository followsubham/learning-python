#In the main lesson we talked about deciding whether we're prepared for the weather. I said that I'm safe from today's weather if...
#I have an umbrella...
#or if the rain isn't too heavy and I have a hood...
#otherwise, I'm still fine unless it's raining and it's a workday
#The function below uses our first attempt at turning this logic into a Python expression. I claimed that there was a bug in that code. Can you find it?
#To prove that prepared_for_weather is buggy, come up with a set of inputs where either:
#the function returns False (but should have returned True), or
#the function returned True (but should have returned False).
#To get credit for completing this question, your code should return a Correct result.


def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)


