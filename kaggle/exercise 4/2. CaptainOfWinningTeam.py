#You are analyzing sports teams. Members of each team are stored in a list. The Coach is the first name in the list, the captain is the second name in the list, and other players are listed after that. These lists are stored in another list, which starts with the best team and proceeds through the list to the worst team last. Complete the function below to select the captain of the worst team.

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    A=teams[-1]
    captain=A[1]
    return captain


#The next iteration of Mario Kart will feature an extra-infuriating new item, the Purple Shell. When used, it warps the last place racer into first place and the first place racer into last place. Complete the function below to implement the Purple Shell's effect.

def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.

    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    temp = racers[0]
    racers[0] = racers[-1]
    racers[-1] = temp
#What are the lengths of the following lists? Fill in the variable lengths with your predictions. (Try to make a prediction for each list without just calling len() on it.)

a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = []


def predictlength():
    def fashionably_late(arrivals, name):
        """Given an ordered list of arrivals to the party and a name, return whether the guest with that
        name was fashionably late.
        """
        order = arrivals.index(name)
        return order >= len(arrivals) / 2 and order != len(arrivals) - 1
