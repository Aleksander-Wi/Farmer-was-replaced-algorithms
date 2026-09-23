tresure_found = None

def maze_creator():
	global tresure_found
	global tresure_x
	global tresure_y
	till()
	till()
	visited = []
	visited_2 = []
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	tresure_x, tresure_y = measure()
	tresure_found = False
	visited = [(get_pos_x(), get_pos_y())]
	visited_2 = [(get_pos_x(), get_pos_y())]
	return tresure_found

def maze_drone1():

	global tresure_found
	global tresure_x
	global tresure_y
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
			plant(Entities.Bush)
			substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
			use_item(Items.Weird_Substance, substance)
			tresure_found = False

def maze_drone2():
	global tresure_found
	global tresure_x
	global tresure_y
	while True:
		visited = [(get_pos_x(), get_pos_y())]
		visited_2 = [(get_pos_x(), get_pos_y())]
		while not tresure_found:
			if get_entity_type() == Entities.Treasure:
				break
			first_pos = get_pos_x(), get_pos_y()
			if can_move(South) and (get_pos_x() ,get_pos_y() - 1) not in visited:
				move(South)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
			elif can_move(East) and (get_pos_x() + 1 ,get_pos_y()) not in visited:
				move(East)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
			elif can_move(West) and (get_pos_x() - 1 ,get_pos_y()) not in visited:
				move(West)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
			elif can_move(North) and (get_pos_x() ,get_pos_y() + 1) not in visited:
				move(North)
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
			plant(Entities.Bush)
			substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
			use_item(Items.Weird_Substance, substance)
			tresure_found = False

def maze_drone3():
	global tresure_found
	global tresure_x
	global tresure_y
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
			elif can_move(West) and (get_pos_x() - 1 ,get_pos_y()) not in visited:
				move(West)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
			elif can_move(East) and (get_pos_x() + 1 ,get_pos_y()) not in visited:
				move(East)
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
			plant(Entities.Bush)
			substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
			use_item(Items.Weird_Substance, substance)
			tresure_found = False

def maze_drone4():
	global tresure_found
	global tresure_x
	global tresure_y
	while True:
		visited = [(get_pos_x(), get_pos_y())]
		visited_2 = [(get_pos_x(), get_pos_y())]
		while not tresure_found:
			if get_entity_type() == Entities.Treasure:
				break
			first_pos = get_pos_x(), get_pos_y()
			if can_move(South) and (get_pos_x() ,get_pos_y() - 1) not in visited:
				move(South)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
			elif can_move(West) and (get_pos_x() - 1 ,get_pos_y()) not in visited:
				move(West)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
			elif can_move(East) and (get_pos_x() + 1 ,get_pos_y()) not in visited:
				move(East)
				visited_2.append((get_pos_x(), get_pos_y()))
				visited.append((get_pos_x(), get_pos_y()))
			elif can_move(North) and (get_pos_x() ,get_pos_y() + 1) not in visited:
				move(North)
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
			plant(Entities.Bush)
			substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
			use_item(Items.Weird_Substance, substance)
			tresure_found = False