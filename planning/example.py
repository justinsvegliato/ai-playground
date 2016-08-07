#!/usr/bin/env python
import grid_world as domain
from mdp import MDP, VI

def main():
    mdp = MDP(
        domain.get_states(),
        domain.get_actions,
        domain.get_transition_probabilities,
        domain.get_reward,
        domain.get_state_key
    )
    vi = VI(epsilon=0.1)
    policy = mdp.solve(solver=vi)

if __name__ == '__main__':
    main()
