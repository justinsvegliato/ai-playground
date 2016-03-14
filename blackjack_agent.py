import numpy as np

def initialize_state_space():
    states = []
    for card in range(1,11):
        for value in range(11,22):
            states.append((value, False, card))
            states.append((value, True, card))
    return states

def initialize_state_actions(states):
    action_value_map = {}
    for state in states:
        action_value_map[(state, 0)] = 0.0
        action_value_map[(state, 1)] = 0.0
    return action_value_map 

def initialize_state_action_count(state_action_pairs):
    counts = {}
    for pair in state_actions_pairs:
        counts[pair] = 0
    return counts

def calculate_reward(outcome):
    return 3 - outcome

#This recalculates the average rewards for our Q-value look-up table
def updateQtable(av_table, av_count, returns):
    for key in returns:
        av_table[key] = av_table[key] + (1 / av_count[key]) * (returns[key]- av_table[key])
    return av_table

#returns Q-value/avg rewards for each action given a state
def qsv(state, av_table):
    stay = av_table[(state,0)]
    hit = av_table[(state,1)]
    return np.array([stay, hit])

#converts a game state of the form ((player total, ace), (dealer total, ace), status) 
#to a condensed state we'll use for our RL algorithm (player total, usable ace, dealer card)
def getRLstate(state):
    player_hand, dealer_hand, status = state
    player_val, player_ace = player_hand
    return (player_val, player_ace, dealer_hand[0])
