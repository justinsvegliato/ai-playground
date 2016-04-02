import numpy as np
import random

PLAYS_COUNT = 500
PLAYS_CHECK_POINT = PLAYS_COUNT / 10

SLOT_MACHINE_COUNT = 10
SLOT_MACHINE = np.random.rand(SLOT_MACHINE_COUNT)

REWARD_ITERATIONS = 10
EPSILON = 0.1

def get_reward(probability):
    reward = 0;

    for i in range(REWARD_ITERATIONS):
        if random.random() < probability:
            reward += 1

    return reward

def get_best_slot_machine(action_value_map):
    return np.argmax(action_value_map) 

def get_choice(action_value_map):
    return get_best_slot_machine(action_value_map) if random.random() > EPSILON else np.where(SLOT_MACHINE == np.random.choice(SLOT_MACHINE))[0][0]

action_value_map = np.ones(SLOT_MACHINE_COUNT) 
counts = np.zeros(SLOT_MACHINE_COUNT)

for i in range(PLAYS_COUNT):
    choice = get_choice(action_value_map)
    reward = get_reward(SLOT_MACHINE[choice])

    counts[choice] += 1

    old_average = action_value_map[choice]
    new_average = (old_average * (counts[choice] - 1) + reward) / counts[choice] 

    action_value_map[choice] = new_average
    
    running_mean = np.average(action_value_map, weights=np.array([counts[k] / np.sum(counts) for k in range(len(counts))])) 

    if i % PLAYS_CHECK_POINT == 0:
        print "Average Slot Machine Reward = %f" % (running_mean,)