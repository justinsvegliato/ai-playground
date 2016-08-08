#!/usr/bin/env python
import time
import grid_world as domain
from mdp import MDP, VI, SSP, RTDP

def execute_mdp_example():
    mdp = MDP(
        domain.get_states(),
        domain.get_actions,
        domain.get_transition_probabilities,
        domain.get_reward,
        domain.get_state_key
    )
    vi = VI(epsilon=0.1)

    t0 = time.clock()
    mdp.solve(solver=vi)
    t1 = time.clock()

    print "VI Policy generated in %d seconds." % (t1 - t0)

def execute_ssp_example():
    ssp = SSP(
        domain.get_states(),
        domain.get_actions,
        domain.get_transition_probabilities,
        domain.get_cost,
        domain.get_state_key,
        domain.get_start_state(),
        domain.get_goal_state()
    )
    rtdp = RTDP(trials=50)

    t0 = time.clock()
    ssp.solve(solver=rtdp)
    t1 = time.clock()

    print "RTDP Policy generated in %d seconds." % (t1 - t0)

def main():
    execute_mdp_example()
    execute_ssp_example()

if __name__ == '__main__':
    main()
