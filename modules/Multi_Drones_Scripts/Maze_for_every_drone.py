import reset_maze

def maze_drone3():
	change_hat(Hats.Traffic_Cone)
	tresure_found = False
	move(South)
	start_maze_pos_x = get_pos_x()
	start_maze_pos_y = get_pos_y()
	plant(Entities.Bush)
	substance = (get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)) / 2
	use_item(Items.Weird_Substance, substance)
	
	while True:
		visited = [(get_pos_x(), get_pos_y())]
		visited_2 = [(get_pos_x(), get_pos_y())]
	
		while not tresure_found:
			if get_entity_type() == Entities.Treasure:
				break
			first_pos = get_pos_x(), get_pos_y()
			if can_move(North) and (get_pos_x() ,get_pos_y() + 1) not in visited:
				move(North)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
			elif can_move(East) and (get_pos_x()+ 1 ,get_pos_y()) not in visited:
				move(East)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
			elif can_move(West) and (get_pos_x() - 1 ,get_pos_y()) not in visited:
				move(West)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
			elif can_move(South) and (get_pos_x() ,get_pos_y() - 1) not in visited:
				move(South)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
	
			second_pos = get_pos_x(), get_pos_y()
			last_visited_x, last_visited_y = visited[-1]
			if first_pos == second_pos:
				if len(visited_2) > 0:
					visited_2.pop()
					if len(visited_2) > 0:
						last_pos_x, last_pos_y = visited_2[-1]
						if (get_pos_y() - last_pos_y == -1):
							move(North)
						elif (get_pos_y() - last_pos_y == 1):
							move(South)
			
						elif (get_pos_x() - last_pos_x == -1):
							move(East)
						elif (get_pos_x() - last_pos_x == 1):
							move(West)
					else:
						visited = [(get_pos_x(), get_pos_y())]
						visited_2 = [(get_pos_x(), get_pos_y())]

		if get_entity_type() == Entities.Treasure:
			tresure_found = True
			harvest()
			while get_pos_x() != start_maze_pos_x:
				move(West)
			while get_pos_y() != start_maze_pos_y:
				move(North)
							
							
			plant(Entities.Bush)
			substance = (get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)) / 2
			use_item(Items.Weird_Substance, substance)
			tresure_found = False
			
		
def maze_drone4():
	change_hat(Hats.Wizard_Hat)
	tresure_found = False
	start_maze_pos_x = get_pos_x()
	start_maze_pos_y = get_pos_y()
	plant(Entities.Bush)
	substance = (get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)) / 2
	use_item(Items.Weird_Substance, substance)
	
	while True:
		visited = [(get_pos_x(), get_pos_y())]
		visited_2 = [(get_pos_x(), get_pos_y())]
	
		while not tresure_found:
			if get_entity_type() == Entities.Treasure:
				break
			first_pos = get_pos_x(), get_pos_y()
			if can_move(North) and (get_pos_x() ,get_pos_y() + 1) not in visited:
				move(North)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
			elif can_move(East) and (get_pos_x()+ 1 ,get_pos_y()) not in visited:
				move(East)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
			elif can_move(West) and (get_pos_x() - 1 ,get_pos_y()) not in visited:
				move(West)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
			elif can_move(South) and (get_pos_x() ,get_pos_y() - 1) not in visited:
				move(South)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
	
			second_pos = get_pos_x(), get_pos_y()
			last_visited_x, last_visited_y = visited[-1]
			if first_pos == second_pos:
				if len(visited_2) > 0:
					visited_2.pop()
					if len(visited_2) > 0:
						last_pos_x, last_pos_y = visited_2[-1]
						if (get_pos_y() - last_pos_y == -1):
							move(North)
						elif (get_pos_y() - last_pos_y == 1):
							move(South)
			
						elif (get_pos_x() - last_pos_x == -1):
							move(East)
						elif (get_pos_x() - last_pos_x == 1):
							move(West)
					else:
						visited = [(get_pos_x(), get_pos_y())]
						visited_2 = [(get_pos_x(), get_pos_y())]

		if get_entity_type() == Entities.Treasure:
			tresure_found = True
			harvest()
			while get_pos_x() != start_maze_pos_x:
				move(West)
			while get_pos_y() != start_maze_pos_y:
				move(South)
			plant(Entities.Bush)
			substance = (get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)) / 2
			use_item(Items.Weird_Substance, substance)
			tresure_found = False

def maze_drone2():
	change_hat(Hats.Pumpkin_Hat)
	move(West)
	tresure_found = False
	start_maze_pos_x = get_pos_x()
	start_maze_pos_y = get_pos_y()
	plant(Entities.Bush)
	substance = (get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)) / 2
	use_item(Items.Weird_Substance, substance)
	
	while True:
		visited = [(get_pos_x(), get_pos_y())]
		visited_2 = [(get_pos_x(), get_pos_y())]
	
		while not tresure_found:
			if get_entity_type() == Entities.Treasure:
				break
			first_pos = get_pos_x(), get_pos_y()
			if can_move(North) and (get_pos_x() ,get_pos_y() + 1) not in visited:
				move(North)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
			elif can_move(East) and (get_pos_x()+ 1 ,get_pos_y()) not in visited:
				move(East)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
			elif can_move(West) and (get_pos_x() - 1 ,get_pos_y()) not in visited:
				move(West)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
			elif can_move(South) and (get_pos_x() ,get_pos_y() - 1) not in visited:
				move(South)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
	
			second_pos = get_pos_x(), get_pos_y()
			last_visited_x, last_visited_y = visited[-1]
			if first_pos == second_pos:
				if len(visited_2) > 0:
					visited_2.pop()
					if len(visited_2) > 0:
						last_pos_x, last_pos_y = visited_2[-1]
						if (get_pos_y() - last_pos_y == -1):
							move(North)
						elif (get_pos_y() - last_pos_y == 1):
							move(South)
			
						elif (get_pos_x() - last_pos_x == -1):
							move(East)
						elif (get_pos_x() - last_pos_x == 1):
							move(West)
					else:
						visited = [(get_pos_x(), get_pos_y())]
						visited_2 = [(get_pos_x(), get_pos_y())]

		if get_entity_type() == Entities.Treasure:
			tresure_found = True
			harvest()
			while get_pos_x() != start_maze_pos_x:
				move(East)
			while get_pos_y() != start_maze_pos_y:
				move(South)
			plant(Entities.Bush)
			substance = (get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)) / 2
			use_item(Items.Weird_Substance, substance)
			tresure_found = False
			
def maze_drone1():
	change_hat(Hats.Gold_Hat)
	move(South)
	move(West)
	tresure_found = False
	start_maze_pos_x = get_pos_x()
	start_maze_pos_y = get_pos_y()
	plant(Entities.Bush)
	substance = (get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)) / 2
	use_item(Items.Weird_Substance, substance)
	
	while True:
		visited = [(get_pos_x(), get_pos_y())]
		visited_2 = [(get_pos_x(), get_pos_y())]
	
		while not tresure_found:
			if get_entity_type() == Entities.Treasure:
				break
			first_pos = get_pos_x(), get_pos_y()
			if can_move(North) and (get_pos_x() ,get_pos_y() + 1) not in visited:
				move(North)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
			elif can_move(East) and (get_pos_x()+ 1 ,get_pos_y()) not in visited:
				move(East)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
			elif can_move(West) and (get_pos_x() - 1 ,get_pos_y()) not in visited:
				move(West)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
			elif can_move(South) and (get_pos_x() ,get_pos_y() - 1) not in visited:
				move(South)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
	
			second_pos = get_pos_x(), get_pos_y()
			last_visited_x, last_visited_y = visited[-1]
			if first_pos == second_pos:
				if len(visited_2) > 0:
					visited_2.pop()
					if len(visited_2) > 0:
						last_pos_x, last_pos_y = visited_2[-1]
						if (get_pos_y() - last_pos_y == -1):
							move(North)
						elif (get_pos_y() - last_pos_y == 1):
							move(South)
			
						elif (get_pos_x() - last_pos_x == -1):
							move(East)
						elif (get_pos_x() - last_pos_x == 1):
							move(West)
					else:
						visited = [(get_pos_x(), get_pos_y())]
						visited_2 = [(get_pos_x(), get_pos_y())]

		if get_entity_type() == Entities.Treasure:
			tresure_found = True
			harvest()
			while get_pos_x() != start_maze_pos_x:
				move(East)
			while get_pos_y() != start_maze_pos_y:
				move(North)
			plant(Entities.Bush)
			substance = (get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)) / 2
			use_item(Items.Weird_Substance, substance)
			tresure_found = False
			

max_drones_number = max_drones()

reset_maze.reset()

if max_drones_number > 4:
	max_drones_number = 4

while True:
	while max_drones_number != num_drones():
		if max_drones_number == 4:
			spawn_drone(maze_drone1)
			spawn_drone(maze_drone2)
			spawn_drone(maze_drone3)
			maze_drone4()
		elif max_drones_number == 3:
			spawn_drone(maze_drone1)
			spawn_drone(maze_drone2)
			maze_drone4()
		elif max_drones_number == 2:
			spawn_drone(maze_drone1)
			maze_drone4()
		else:
			maze_drone1()







