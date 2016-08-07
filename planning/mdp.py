from solvers import value_iteration, policy_iteration

class VI:
    def __init__(self, epsilon=0.01):
        self.epsilon = epsilon

    def solve(self, mdp):
        return value_iteration(mdp, self.epsilon)

class PI:
    def __init__(self, iterations=20):
        self.iterations = iterations

    def solve(self, mdp):
        return policy_iteration(mdp, self.iterations)

SOLVERS = {
    'vi': VI,
    'pi': PI
}

class MDP:
    def __init__(self, states, get_actions, get_transition_probabilities, get_reward, get_state_key, gamma=0.9):
        self.states = states
        self.get_actions = get_actions
        self.get_transition_probabilities = get_transition_probabilities
        self.get_reward = get_reward
        self.get_state_key = get_state_key
        self.gamma = gamma

    def solve(self, solver='vi'):
        if isinstance(solver, basestring):
            solver = SOLVERS[solver]()
        return solver.solve(self)
