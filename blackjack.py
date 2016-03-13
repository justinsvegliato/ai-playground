import math
import random

def get_random_card():
    card = random.randint(1,13)
    return 10 if card > 10 else card

def is_ace_usable(hand):
    val, ace = hand
    return ace and val + 10 <= 21

def get_total_value(hand):
    val, ace = hand
    return val + 10 if is_ace_usable(hand) else val

def add_card(hand, card):
    val, ace = hand
    ace = True if card == 1 else ace
    return (val + card, ace)

def evaluate_dealer(dealer_hand):
    while get_total_value(dealer_hand) < 17:
        dealer_hand = add_card(dealer_hand, get_random_card())
    return dealer_hand

def get_dealer_status(dealer_total, player_total):
    if dealer_total > 21:
        return 2 
    elif dealer_total == player_total:
        return 3 
    elif dealer_total < player_total:
        return 2
    elif dealer_total > player_total:
        return 4
    return 1

def get_player_status(dealer_total, player_total):
    if player_total == 21:
        return 3 if dealer_total == 21 else 2
    elif player_total > 21:
        return 4
    return 1

def play(state, decision):
    player_hand = state[0] 

    dealer_hand = evaluate_dealer(state[1])
    dealer_total = get_total_value(dealer_hand)

    status = 1

    if decision == 0: 
        player_total = get_total_value(player_hand)
        status = get_dealer_status(dealer_total, player_total)
    elif decision == 1: 
        player_hand = add_card(player_hand, get_random_card())
        player_total = get_total_value(player_hand)
        status = get_player_status(dealer_total, player_total)

    return (player_hand, dealer_hand, status)

def initialize_game():
    player_hand = add_card((0, False), get_random_card())
    player_hand = add_card(player_hand, get_random_card())
    player_total = get_total_value(player_hand)

    dealer_hand = add_card((0, False), get_random_card())
    dealer_total = get_total_value(dealer_hand)    

    status = get_player_status(dealer_total, player_total)

    return (player_hand, dealer_hand, status)
