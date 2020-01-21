from appliances.appliance import Appliance

class Stove(Appliance):

    def __init__(self, color, heat_method):
        super().__init__(color, heat_method)

    def bake_cake(self):
        print("It's your birthday!  Have a cake!")
