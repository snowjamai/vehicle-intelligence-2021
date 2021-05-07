import numpy as np


class HybridAStar:
    # Determine how many grid cells to have for theta-axis.
    NUM_THETA_CELLS = 90

    # Define min, max, and resolution of steering angles
    omega_min = -35
    omega_max = 35
    omega_step = 5

    # A very simple bicycle model
    speed = 1.5
    length = 0.5

    # Initialize the search structure.
    def __init__(self, dim):
        self.dim = dim
        self.closed = np.zeros(self.dim, dtype=np.int)
        self.came_from = np.full(self.dim, None)

    # Expand from a given state by enumerating reachable states.
    def expand(self, current, goal):
        g = current['g']
        x, y, theta = current['x'], current['y'], current['t']

        # The g value of a newly expanded cell increases by 1 from the
        # previously expanded cell.
        g2 = g + 1
        next_states = []

        # Consider a discrete selection of steering angles.
        for delta_t in range(self.omega_min, self.omega_max + self.omega_step, self.omega_step):
            # TODO: implement the trajectory generation based on
            # a simple bicycle model.
            # Let theta2 be the vehicle's heading (in radian)
            # between 0 and 2 * PI.
            # Check validity and then add to the next_states list.
            delta_t *= (np.pi / 180)
            omega = self.speed / self.length * np.tan(delta_t)
            theta2 = theta + omega

            while True:
                if theta2 >= 0 and theta2 < 2 * np.pi:
                    break
                if theta2 >= 2 * np.pi:
                    theta2 = theta2 - 2 * np.pi
                elif theta2 < 0:
                    theta2 = theta2 + 2 * np.pi

            n_x = x + self.speed * np.cos(theta2)
            n_y = y + self.speed * np.sin(theta2)

            if 0 <= self.idx(n_x) < self.dim[1] and 0 <= self.idx(n_y) < self.dim[2]:
                next_f = g2 + self.heuristic(n_x, n_y, goal)
                expanded_state = {'x': n_x, 'y': n_y, 't': theta2, 'g': g2, 'f': next_f}

                next_states.append(expanded_state)

        return next_states



    # Perform a breadth-first search based on the Hybrid A* algorithm.
    def search(self, grid, start, goal):
        # Initial heading of the vehicle is given in the
        # last component of the tuple start.
        theta = start[-1]
        # Determine the cell to contain the initial state, as well as
        # the state itself.
        stack = self.theta_to_stack_num(theta)
        g = 0
        s = {
            'f': self.heuristic(start[0], start[1], goal),
            'g': g,
            'x': start[0],
            'y': start[1],
            't': theta,
        }
        self.final = s
        # Close the initial cell and record the starting state for
        # the sake of path reconstruction.
        self.closed[stack][self.idx(s['x'])][self.idx(s['y'])] = 1
        self.came_from[stack][self.idx(s['x'])][self.idx(s['y'])] = s
        total_closed = 1
        opened = [s]

        # Examine the open list, according to the order dictated by
        # the heuristic function.

        while len(opened) > 0:
            # TODO: implement prioritized breadth-first search
            # for the hybrid A* algorithm.

            opened.sort(key=lambda s: s['f'], reverse=True)
            now = opened.pop()


            if (self.idx(now['x']), self.idx(now['y'])) == goal:
                self.final = now
                found = True
                break

            # Compute reachable new states and process each of them.
            next_states = self.expand(now, goal)

            for n in next_states:
                idx_x, idx_y = self.idx(n['x']), self.idx(n['y'])
                stack = self.theta_to_stack_num(n['t'])


                if grid[idx_x, idx_y] == 0:
                    dist_x, dist_y = abs(self.idx(now['x']) - idx_x), abs(self.idx(now['y']) - idx_y)
                    min_x, min_y = np.minimum(self.idx(now['x']), idx_x), np.minimum(self.idx(now['y']), idx_y)
                    possible = True
                    for d_x in range(dist_x + 1):
                        for d_y in range(dist_y + 1):
                            if grid[min_x + d_x, min_y + d_y] != 0:
                                possible = False
                    if possible and self.closed[stack][idx_x][idx_y] == 0:
                        self.closed[stack][idx_x][idx_y] = 1
                        total_closed += 1
                        self.came_from[stack][idx_x][idx_y] = now
                        opened.append(n)

        else:
            # We weren't able to find a valid path; this does not necessarily
            # mean there is no feasible trajectory to reach the goal.
            # In other words, the hybrid A* algorithm is not complete.
            found = False
        print(f"speed: {self.speed} NUM_THETA_CELLS: {self.NUM_THETA_CELLS}")
        return found, total_closed

    # Calculate the stack index of a state based on the vehicle's heading.
    def theta_to_stack_num(self, theta):
        # TODO: implement a function that calculate the stack number
        # given theta represented in radian. Note that the calculation
        # should partition 360 degrees (2 * PI rad) into different
        # cells whose number is given by NUM_THETA_CELLS.
        interval = 2 * np.pi / self.dim[0]
        s_cnt = 0
        while theta > interval:
            theta -= interval
            s_cnt += 1
        if s_cnt == self.NUM_THETA_CELLS:
            s_cnt = 0
        return int(s_cnt)

    # Calculate the index of the grid cell based on the vehicle's position.
    def idx(self, pos):
        # We simply assume that each of the grid cell is the size 1 X 1.
        return int(np.floor(pos))

    # Implement a heuristic function to be used in the hybrid A* algorithm.
    def heuristic(self, x, y, goal):
        # TODO: implement a heuristic function.
        return np.sqrt((x - goal[0])**2 + (y - goal[1])**2)


    # Reconstruct the path taken by the hybrid A* algorithm.
    def reconstruct_path(self, start, goal):
        # Start from the final state, and follow the link to the
        # previous state using the came_from matrix.
        curr = self.final
        x, y = curr['x'], curr['y']
        path = []
        while x != start[0] and y != start[1]:
            path.append(curr)
            stack = self.theta_to_stack_num(curr['t'])
            x, y = curr['x'], curr['y']
            curr = self.came_from[stack][self.idx(x)][self.idx(y)]
        # Reverse the path so that it begins at the starting state
        # and ends at the final state.
        path.reverse()

        return path