# from appliances.kitchen import Dishwasher
# from appliances.laundry import Dryer
# from appliances.laundry import Washer
# from appliances.kitchen.utility import Refrigerator
# from appliances import CoffeeMaker, Dryer, Washer, CanOpener, Stove
# from appliances.kitchen import DishWasher, Refrigerator
from appliances import Dryer, Washer, Stove, CoffeeMaker, CanOpener

# whirlpool_dishwasher = Dishwasher("black",)
# whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red", "electric")
samsung_washer.wash_clothes("delicates")
samsung_dryer = Dryer("red", "gas")
lg_stove = Stove("stainless", "Electric")
lg_stove.bake_cake()

# lg_fridge = Refrigerator("stainless")
# lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white", "electric")
mr_coffee.make_coffee()

old_can_opener = CanOpener("black", "none")
old_can_opener.open_can()
