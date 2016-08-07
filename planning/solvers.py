import random

def argmax(args, function):
    best = args[0]
    best_score = float('-inf')
    for arg in args:
        score = function(arg)
        if score > best_score:
            best, best_score = arg, score
    return best

def get_initial_values(mdp):
    values = {}
    for state in mdp.states:
        state_key = mdp.get_state_key(state)
        values[state_key] = 0
    return values

def get_initial_policy(mdp):
    policy = {}
    for state in mdp.states:
        state_key = mdp.get_state_key(state)
        policy[state_key] = random.choice(mdp.get_actions(state))
    return policy

def get_values(mdp, epsilon):
    values = get_initial_values(mdp)

    while True:
        new_values = values.copy()
        delta = 0

        for state in mdp.states:
            action_values = []
            for action in mdp.get_actions(state):
                action_value = 0
                for probability, new_state in mdp.get_transition_probabilities(state, action):
                    new_state_key = mdp.get_state_key(new_state)
                    action_value += probability * values[new_state_key]
                action_values.append(action_value)

            state_key = mdp.get_state_key(state)
            new_values[state_key] = mdp.get_reward(state) + mdp.gamma * max(action_values)
            delta = max(delta, abs(new_values[state_key] - values[state_key]))
            values = new_values

        if delta < epsilon * (1 - mdp.gamma) / mdp.gamma:
            return values

def get_best_policy(mdp, values):
    policy = {}
    for state in mdp.states:
        state_key = mdp.get_state_key(state)
        get_action_value = lambda action: get_expected_value(mdp, action, state, values)
        policy[state_key] = argmax(mdp.get_actions(state), get_action_value)
    return policy

def get_expected_value(mdp, action, state, values):
    expected_value = 0
    for probability, next_state in mdp.get_transition_probabilities(state, action):
        next_state_key = mdp.get_state_key(next_state)
        expected_value += probability * values[next_state_key]
    return expected_value

def evaluate_policy(mdp, policy, values, iterations):
    for _i in range(iterations):
        for state in mdp.states:
            state_key = mdp.get_state_key(state)
            action_value = 0
            action = policy[state_key]
            for probability, new_state in mdp.get_transition_probabilities(state, action):
                new_state_key = mdp.get_state_key(new_state)
                action_value += probability * values[new_state_key]

            values[state_key] = mdp.get_reward(state) + mdp.gamma * action_value

    return values

def value_iteration(mdp, epsilon):
    values = get_values(mdp, epsilon)
    return get_best_policy(mdp, values)

def policy_iteration(mdp, iterations):
    values = get_initial_values(mdp)
    policy = get_initial_policy(mdp)

    while True:
        values = evaluate_policy(mdp, policy, values, iterations)

        has_policy_changed = False
        for state in mdp.states:
            state_key = mdp.get_state_key(state)
            get_action_value = lambda action: get_expected_value(mdp, action, state, values)
            action = argmax(mdp.get_actions(state), get_action_value)

            if action != policy[state_key]:
                policy[state_key] = action
                has_policy_changed = True

            if not has_policy_changed:
                return policy
