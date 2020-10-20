class Hotel:
    def __init__(self, name, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price):
        self.name = name
        self.place = place
        self.rooms_mid = {room:1 free, room:2 free, room:3 free}
        self.mid_room_price = mid_room_price
        self.rooms_lux = {room:1 free, room:2 free, room:3 free}

    # def presentation(self):


    def booking(self):
        self.rooms_mid["room1"] = "busy"
