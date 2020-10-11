#The boolean variables ketchup, mustard and onion represent whether a customer wants a particular topping on their hot dog. We want to implement a number of boolean functions that correspond to some yes-or-no questions about the customer's order. For example:


"""Return whether the customer doesn't want onions.
"""
return bool(onion) == 1


def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not bool(ketchup) and not bool(mustard) and not bool(onion)


def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return bool(ketchup) or bool(mustard) or bool(onion) == True



    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return int(bool(ketchup))+int(bool(mustard))+int(bool(onion)) == 1