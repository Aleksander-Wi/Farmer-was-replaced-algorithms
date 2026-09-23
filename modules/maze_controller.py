import MAZE



max_drones_number = max_drones()

if max_drones_number > 4:
	max_drones_number = 4

while True:
	MAZE.maze_creator()
	while max_drones_number != num_drones():
		if max_drones_number == 4:
			spawn_drone(MAZE.maze_drone2)
			spawn_drone(MAZE.maze_drone3)
			spawn_drone(MAZE.maze_drone4)
			MAZE.maze_drone1()
		elif max_drones_number == 3:
			spawn_drone(MAZE.maze_drone3)
			spawn_drone(MAZE.maze_drone4)
			MAZE.maze_drone1()
		elif max_drones_number == 2:
			spawn_drone(MAZE.maze_drone4)
			MAZE.maze_drone1()
		else:
			MAZE.maze_drone1()