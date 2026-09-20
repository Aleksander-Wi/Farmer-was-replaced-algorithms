#--Imports--
import sunflower
import carrot
import WOOD
import HAY
import reset
import PUMPKIN

#--Hat_Changer
change_hat(Hats.Carrot_Hat)

#--Loops--
wheat_loops = 12
bush_loops = 0
carrot_loops = 0
sun_flower_loop = 0
pumpkin_loop = 0

#--Reset--
reset.reset()
quality_lower = 0
quality_higher_1 = 0
quality_higher_2 = 0
quality_higher_3 = 0
quality_higher_y_1 = 0
quality_higher_x_1 = 0
quality_higher_y_2 = 0
quality_higher_x_2 = 0
quality_higher_y_3 = 0
quality_higher_x_3 = 0
#--MAIN
while True:
	sunflower.sunflowerloop()
	HAY.HAY(wheat_loops)
	WOOD.wood(bush_loops)
	carrot.carrot(carrot_loops)
	PUMPKIN.pumpkin(pumpkin_loop)
	reset.reset()

