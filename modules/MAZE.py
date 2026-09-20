
harvest()

def maze():
	
	till()
	till()
	plant(Entities.Bush)
	visited = []
	visited_2 = []
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	tresure_x, tresure_y = measure()
	visited = [(get_pos_x(), get_pos_y())]
	visited_2 = [(get_pos_x(), get_pos_y())]
	while get_pos_x() != tresure_x or get_pos_y() != tresure_y:
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
	harvest()
			
		
			
		
			
	
	
	
while True:
	maze()
