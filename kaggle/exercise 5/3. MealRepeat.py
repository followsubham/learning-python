def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever beyaen served two days in a row, and False otherwise.
    """
    # Iterate over all indices of the list, except the last one
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False