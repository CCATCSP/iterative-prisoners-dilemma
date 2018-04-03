
team_name = 'TF2' # Only 10 chars displayed.
strategy_name = 'Good Boys'
strategy_description = 'Collude at start and betray if they start getting ahead of us'
    
def move(my_history, their_history, my_score, their_score):
    if  my_history=='c' and their_history=='b':
        if my_score<their_score:
            return 'b'
        else:
            return 'c'
    else:
        return 'c'        