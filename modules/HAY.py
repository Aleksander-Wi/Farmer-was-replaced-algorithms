def HAY(wheat_loops):
	for i in range(get_world_size() * wheat_loops):
			if get_ground_type() == Grounds.Soil:
				till()
			harvest()
			if get_pos_y() == get_world_size() - 1:
				move(East)
			move(North)
			
