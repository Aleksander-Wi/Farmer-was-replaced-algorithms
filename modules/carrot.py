def carrot(carrot_loops):
	for i in range(get_world_size() * carrot_loops):
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Carrot)
			if can_harvest():
				harvest()
				if get_entity_type() != Entities.Carrot :
					plant(Entities.Carrot)
			if get_pos_y() == get_world_size() - 1:
				move(East)
			move(North)
			
