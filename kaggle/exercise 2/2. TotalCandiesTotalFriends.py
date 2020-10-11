##In a previous programming problem, the candy-sharing friends Alice, Bob and Carol tried to split candies evenly. For the sake of their friendship, any candies left over would be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.
#Below is a simple function that will calculate the number of candies to smash for *any* number of total candies.
#Modify it so that it optionally takes a second argument representing the number of friends the candies are being split between. If no second argument is provided, it should assume 3 friends, as before.
#Update the docstring to reflect this new behaviour.

def to_smash(total_candies, total_friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.

    >>> to_smash(91)
    1
    """
    return total_candies % total_friends