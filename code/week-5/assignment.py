import numpy as np
import itertools

# Given map
grid = np.array([
    [1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1]
])

# List of possible actions defined in terms of changes in
# the coordinates (y, x)
forward = [
    (-1,  0),   # Up
    ( 0, -1),   # Left
    ( 1,  0),   # Down
    ( 0,  1),   # Right
]

# Three actions are defined:
# - right turn & move forward
# - straight forward
# - left turn & move forward
# Note that each action transforms the orientation along the
# forward array defined above.
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

init = (4, 3, 0)    # Representing (y, x, o), where
                    # o denotes the orientation as follows:
                    # 0: up
                    # 1: left
                    # 2: down
                    # 3: right
                    # Note that this order corresponds to forward above.
goal = (2, 0)
cost = (2, 1, 20)   # Cost for each action (right, straight, left)

# EXAMPLE OUTPUT:
# calling optimum_policy_2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]

def optimum_policy_2D(grid, init, goal, cost):
    # Initialize the value function with (infeasibly) high costs.
    value = np.full((4, ) + grid.shape, 999, dtype=np.int32)
    # Initialize the policy function with negative (unused) values.
    policy = np.full((4,) + grid.shape, -1, dtype=np.int32)
    # Final path policy will be in 2D, instead of 3D.
    policy2D = np.full(grid.shape, ' ')

    # Apply dynamic programming with the flag change.
    change = True
    while change:
        change = False
        # This will provide a useful iterator for the state space.
        p = itertools.product(
            range(grid.shape[0]),
            range(grid.shape[1]),
            range(len(forward))
        )

        # Compute the value function for each state and
        # update policy function accordingly.
        for y, x, t in p:
            # Mark the final state with a special value that we will
            # use in generating the final path policy.
            if (y, x) == goal and value[(t, y, x)] > 0:
                change = True
                value[(t,y,x)] = 0
                policy[(t,y,x)] = 999


                # TODO: implement code.

            # Try to use simple arithmetic to capture state transitions.
            elif grid[(y, x)] == 0:
                for a in action:
                    n_t  = (t + a) % 4
                    n_y =  y + forward[n_t][0]
                    n_x = x + forward[n_t][1]
                    n_cost = cost[a + 1]

                    if n_y < 0 or n_y >= grid.shape[0] or n_x < 0 or n_x >= grid.shape[1] or grid[(n_y, n_x)] != 0 :
                        continue
                    n_v = value[(n_t, n_y, n_x)] + n_cost
                    if n_v < value[(t,y,x)]:
                        value[(t,y,x)] = n_v
                        policy[(t,y,x)] = a
                        change = True
                # TODO: implement code.

    # Now navigate through the policy table to generate a
    # sequence of actions to take to follow the optimal path.
    # TODO: implement code.

    y, x, o = init
    min_v = 999

    while (y, x) != goal:
        for t in range(len(forward)):
            if value[(t, y, x)] < min_v:
                min_v = value[(t, y, x)]
                policy2D[(y, x)] = action_name[policy[(o, y, x)] + 1]
        min_v = 999

        o = (o + policy[o, y, x]) % len(forward)
        y = y + forward[o][0]
        x = x + forward[o][1]

        if (y, x) == goal:
            policy2D[(y, x)] = '*'

    # Return the optimum policy generated above.
    return policy2D

print(optimum_policy_2D(grid, init, goal, cost))
