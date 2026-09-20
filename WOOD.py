
def wood(bush_loops):
	first_tree_y = 0
	for i in range(get_world_size() * (bush_loops / 2)):
			if get_ground_type() == Grounds.Soil:
				till()
		
			if can_harvest():
				harvest()
			if first_tree_y == 0:
				if get_water() < 0.2:
					use_item(Items.Water)
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
			if get_pos_y() == get_world_size() - 1:
				move(East)
			move(North)
			if can_harvest():
				harvest()
			if first_tree_y == 0:
				plant(Entities.Bush)
			else:
				if get_water() < 0.2:
					use_item(Items.Water)
				plant(Entities.Tree)
			if get_pos_y() != get_world_size() - 1:
				move(North)
			else:
				move(East)
				move(North)

				if first_tree_y == 0:
					first_tree_y = 1
				else:
					first_tree_y = 0