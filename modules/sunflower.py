import reset
def sunflowerloop():
	sunflowers = []
	import All_in_Script
	first_sunflower_x = get_pos_x()
	first_sunflower_y = get_pos_y()
	def sunflower_high(sunflowers):
		
		while sunflowers:
			best_sunflower = max(sunflowers)
			quality, target_x, target_y = best_sunflower
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
			while can_harvest() == False:
				if get_water() < 0.2: 
					use_item(Items.Water)
				do_a_flip()
			harvest()
			sunflowers.remove(best_sunflower)
		
	for i in range(get_world_size() * All_in_Script.sun_flower_loop):
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Sunflower)
		if get_entity_type() != Entities.Sunflower:
			till()
			till()
			plant(Entities.Sunflower)
		sunflowers.append((measure(), get_pos_x(), get_pos_y()))
				
		if get_pos_y() == get_world_size() - 1:
			move(East)
		move(North)
	sunflower_high(sunflowers)
	if len(sunflowers) == 0:
		if All_in_Script.sun_flower_loop != get_world_size():
			while get_pos_x() != (first_sunflower_x + All_in_Script.sun_flower_loop):
					if abs(first_sunflower_x + All_in_Script.sun_flower_loop - get_pos_x()) <= get_world_size() / 2:
						if first_sunflower_x + All_in_Script.sun_flower_loop > get_pos_x():
							move(East)
						else:
							move(West)
					else:
						if first_sunflower_x + All_in_Script.sun_flower_loop > get_pos_x():
							move(West)
						else:
							move(East)
			while get_pos_y() != (first_sunflower_y):
					if abs(first_sunflower_y) <= get_world_size() / 2:
						if first_sunflower_y > get_pos_y():
							move(North)
						else:
							move(South)
					else:
						if first_sunflower_y > get_pos_y():
							move(South)
						else:
							move(North)
		else:
			reset.reset()
		
		
		
	
	
	

	
