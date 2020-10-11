#After completing the exercises on lists and tuples, Jimmy noticed that, according to his estimate_average_slot_payout function, the slot machines at the Learn Python Casino are actually rigged against the house, and are profitable to play in the long run.
#Starting with $200 in his pocket, Jimmy has played the slots 500 times, recording his new balance in a list after each spin. He used Python's matplotlib library to make a graph of his balance over time:

# Import the jimmy_slots submodule
from learntools.python import jimmy_slots
# Call the get_graph() function to get Jimmy's graph
graph = jimmy_slots.get_graph()
graph


#As you can see, he's hit a bit of bad luck recently. He wants to tweet this along with some choice emojis, but, as it looks right now, his followers will probably find it confusing. He's asked if you can help him make the following changes:
#Add the title "Results of 500 slot machine pulls"
#Make the y-axis start at 0.
#Add the label "Balance" to the y-axis
#After calling type(graph) you see that Jimmy's graph is of type matplotlib.axes._subplots.AxesSubplot. Hm, that's a new one. By calling dir(graph), you find three methods that seem like they'll be useful: .set_title(), .set_ylim(), and .set_ylabel().
#Use these methods to complete the function prettify_graph according to Jimmy's requests. We've already checked off the first request for you (setting a title).
#(Remember: if you don't know what these methods do, use the help() function!)

prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests: add a title, make the y-axis
    start at 0, label the y-axis. (And, if you're feeling ambitious, format the tick marks
    as dollar amounts using the "$" symbol.)
    """
    graph.set_title("Results of 500 slot machine pulls")
    # Make the y-axis begin at 0
    graph.set_ylim(bottom=0)
    # Label the y-axis
    graph.set_ylabel("Balance")
    # Bonus: format the numbers on the y-axis as dollar amounts
    # An array of the values displayed on the y-axis (150, 175, 200, etc.)
    ticks = graph.get_yticks()
    # Format those values into strings beginning with dollar sign
    new_labels = ['${}'.format(int(amt)) for amt in ticks]
    # Set the new labels
    graph.set_yticklabels(new_labels)