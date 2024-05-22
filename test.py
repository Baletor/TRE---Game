from game import GameObject, Game, Room

class RoomTests:
    def __init__(self):
        self.room_1 = Room(111,[GameObject(
            "Sweater", 
            "It's a blue sweater that had the number 12 stitched on it.", 
            "Someone has unstitched the second number, leaving only the 1", 
            "The sweater smells of laundry detergent."),
        GameObject(
            "Chair", 
            "It's a wooden chair with only 3 legs.", 
            "Someone had deliberatly snapped off one of the legs.",
            "It smells like old wood.")])
        self.room_2 = Room(222, [])
        
    def test_check_code(self):
        print(self.room_1.check_code(111) == True)
        print(self.room_1.check_code(222) == False)

    def test_get_game_object_names(self):
        print(self.room_1.get_game_object_names() == ["Sweater", "Chair"])
        print(self.room_2.get_game_object_names() == [])


tests = RoomTests()
tests.test_check_code()
tests.test_get_game_object_names()