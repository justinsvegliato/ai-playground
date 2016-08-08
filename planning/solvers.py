import random
import utils
import numpy as np

def get_initial_values(mdp):
    values = {}
    for state in mdp.states:
        key = mdp.get_key(state)
        values[key] = 0
    return values

def get_initial_policy(mdp):
    policy = {}
    for state in mdp.states:
        key = mdp.get_key(state)
        actions = mdp.get_actions(state)
        policy[key] = random.choice(actions)
    return policy

def get_expected_value(mdp, action, state, values):
    expected_value = 0
    for result_state, probability in mdp.get_transition_probabilities(state, action):
        key = mdp.get_key(result_state)
        expected_value += probability * values[key]
    return expected_value

def get_new_value(mdp, state, values):
    reward = mdp.get_reward(state)

    expected_values = []
    for action in mdp.get_actions(state):
        expected_value = get_expected_value(mdp, action, state, values)
        expected_values.append(expected_value)

    return reward + mdp.gamma * max(expected_values)

def get_best_action(mdp, state, values):
    get_value = lambda action: get_expected_value(mdp, action, state, values)
    actions = mdp.get_actions(state)
    return utils.argmax(actions, get_value)

def get_optimal_policy(mdp, values):
    policy = {}
    for state in mdp.states:
        key = mdp.get_key(state)
        policy[key] = get_best_action(mdp, state, values)
    return policy

def evaluate_policy(mdp, policy, values, iterations):
    for _i in range(iterations):
        for state in mdp.states:
            key = mdp.get_key(state)
            reward = mdp.get_reward(state)
            expected_value = get_expected_value(mdp, policy[key], state, values)
            values[key] = reward + mdp.gamma * expected_value
    return values

def get_improved_policy(mdp, policy, values):
    has_policy_changed = False
    for state in mdp.states:
        action = get_best_action(mdp, state, values)

        key = mdp.get_key(state)
        if action != policy[key]:
            policy[key] = action
            has_policy_changed = True

    return policy if has_policy_changed else None

def get_optimal_values(mdp, epsilon):
    values = get_initial_values(mdp)

    while True:
        new_values = values.copy()
        delta = 0

        for state in mdp.states:
            key = mdp.get_key(state)
            new_values[key] = get_new_value(mdp, state, values)
            delta = max(delta, abs(new_values[key] - values[key]))
            values = new_values

        if delta < epsilon * (1 - mdp.gamma) / mdp.gamma:
            return values

def value_iteration(mdp, epsilon):
    values = get_optimal_values(mdp, epsilon)
    return get_optimal_policy(mdp, values)

def policy_iteration(mdp, iterations):
    values = get_initial_values(mdp)
    policy = get_initial_policy(mdp)

    while True:
        values = evaluate_policy(mdp, policy, values, iterations)
        new_policy = get_improved_policy(mdp, policy, values)

        if not new_policy:
            return policy

        policy = new_policy

# TODO: First, this code sucks. Second, and more importantly, I think it's wrong.
def rtdp(ssp, trials):
    values = get_initial_values(ssp)
    visited_states = {}

    for _i in range(trials):
        current_state = ssp.start_state

        while not np.array_equal(current_state, ssp.goal_state):
            for state in ssp.states:
                action_values = []
                for action in ssp.get_actions(state):
                    action_value = 0
                    for new_state, probability in ssp.get_transition_probabilities(state, action):
                        new_state_key = ssp.get_key(new_state)
                        action_value += probability * values[new_state_key]
                    action_value += ssp.get_cost(new_state) 
                    action_values.append(action_value)

                state_key = ssp.get_key(state)
                values[state_key] = min(action_values)

            current_state_key = ssp.get_key(current_state)
            visited_states[current_state_key] = current_state

            get_value = lambda action: get_expected_value(ssp, action, current_state, values)
            best_action = utils.argmin(ssp.get_actions(current_state), get_value)

            transition_probabilities = ssp.get_transition_probabilities(current_state, best_action)
            current_state = utils.get_random_variable(transition_probabilities)

        current_state_key = ssp.get_key(current_state)
        visited_states[current_state_key] = current_state

    policy = {}
    for state in visited_states.values():
        action_values = {} 
        for action in ssp.get_actions(state):
            action_value = 0 
            for new_state, probability in ssp.get_transition_probabilities(state, action):
                new_state_key = ssp.get_key(new_state)
                action_value += probability * values[new_state_key]
            action_value += ssp.get_cost(new_state) 
            action_values[action] = action_value
            
        state_key = ssp.get_key(state)
        get_value = lambda action: action_values[action] 
        policy[state_key] = utils.argmin(ssp.get_actions(state), get_value)

    return policy
