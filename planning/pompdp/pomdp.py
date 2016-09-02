class PBVI(object):
    def __init__(self):
        pass

    def solve(self, mdp):
        return False

SOLVERS = {
    'pbvi': PBVI
}

class POMDP(object):
    def __init__(self, states, get_actions, get_transition_probabilities, get_reward, get_observation_probabilities, get_observations):
        self.states = states
        self.get_actions = get_actions
        self.get_transition_probabilities = get_transition_probabilities
        self.get_reward = get_reward
        self.get_observation_probabilities = get_observation_probabilities
        self.get_observation = get_observations

    def solve(self, solver='pbvi'):
        if isinstance(solver, basestring):
            solver = SOLVERS[solver]()
        return solver.solve(self)

