def pumpkin(pumpkin_loop = 0):
	first_pumpkin_pos = []
	first_pumpkin_pos.append(get_pos_x())
	first_pumpkin_pos.append(get_pos_y())
	dead_pumpkin_y = []
	dead_pumpkin_x = []
	for i in range(get_world_size() * pumpkin_loop):
		plant(Entities.Pumpkin)
		if get_ground_type() == Grounds.Grassland:
			till()
		if get_entity_type() != Entities.Pumpkin :
				till()
				till()
				plant(Entities.Pumpkin)
		if can_harvest():
			plant(Entities.Pumpkin)
			harvest()
		else:
			dead_pumpkin_y.append(get_pos_y())
			dead_pumpkin_x.append(get_pos_x())
		if get_pos_y() == get_world_size() - 1 and i == (get_world_size() * pumpkin_loop) - 1:
			if len(dead_pumpkin_x) == 0 and len(dead_pumpkin_y) == 0:
				move(East)
			while dead_pumpkin_x:
				target_x = dead_pumpkin_x.pop(0)
				target_y = dead_pumpkin_y.pop(0)
				while get_pos_x() != target_x:
					if abs(target_x - get_pos_x()) <= get_world_size() / 2:
						if target_x > get_pos_x():
							move(East)
						else:
							move(West)
					else:
						if target_x > get_pos_x():
							move(West)
						else:
							move(East)
				while get_pos_y() != target_y:
					if abs(target_y - get_pos_y()) <= get_world_size() / 2:
						if target_y > get_pos_y():
							move(North)
						else:
							move(South)
					else:
						if target_y > get_pos_y():
							move(South)
						else:
							move(North)
				if get_water() < 0.2:
					use_item(Items.Water)
				
				plant(Entities.Pumpkin)
				if not dead_pumpkin_x:
					while get_pos_x() != first_pumpkin_pos[0]:
						if abs(first_pumpkin_pos[0] - get_pos_x()) <= get_world_size() / 2:
							if first_pumpkin_pos[0]> get_pos_x():
								move(East)
							else:
								move(West)
						else:
							if first_pumpkin_pos[0] > get_pos_x():
								move(West)
							else:
								move(East)
							
					while get_pos_y() != first_pumpkin_pos[1]:
						if abs(first_pumpkin_pos[1] - get_pos_y()) <= get_world_size() / 2:
							if first_pumpkin_pos[1] > get_pos_y():
								move(North)
							else:
								move(South)
						else:
							if first_pumpkin_pos[1] > get_pos_y():
								move(South)
							else:
								move(North)
					for i in range(get_world_size() * pumpkin_loop):
						if can_harvest() == False:
							dead_pumpkin_y.append(get_pos_y())
							dead_pumpkin_x.append(get_pos_x())
						move(North)
						if get_pos_y() == 0:
							move(East)

		move(North)
		if get_pos_y() == 0:
			move(East)
