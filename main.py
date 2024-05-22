from typing import Any


class GameObject:

    #setup the instance of GameObject with name, appearance, feel, and smell
    def __init__(self, name, appearance, feel, smell):
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    #return a string describing an objects appearance
    def look(self):
        return f"You look at the {self.name}. {self.appearance}\n"

    #return a string describing an objects feel
    def touch(self):
        return f"You touch the {self.name}. {self.feel}\n"

    #return a string describing an objects smell
    def sniff(self):
        return f"You smell the {self.name}. {self.smell}\n"
    
class Room:

    #setup instance of room setting the escape code and the game objects
    def __init__(self, escape_code, game_objects):
        self.escape_code = escape_code
        self.game_objects = game_objects

    #check if user found the escape code
    def check_code(self, code):
        return self.escape_code == code
    
    #return  list of all object names in the room
    def get_game_object_names(self):
        names = []
        for object in self.game_objects:
            names.append(object.name)
        return names
    
class Game:

    #setup an instance of a Game with default values of 0 attempts and a room full of objects with 731 as the code
    def __init__(self):
        self.attempts = 0
        self.objects = self.create_objects()
        self.room = Room(731, self.objects)

    #return 5 GameObjects with enough information to guess the code
    def create_objects(self):
        return [
        GameObject(
            "Sweater", 
            "It's a blue sweater that had the number 12 stitched on it.", 
            "Someone has unstitched the second number, leaving only the 1", 
            "The sweater smells of laundry detergent."),
        GameObject(
            "Chair", 
            "It's a wooden chair with only 3 legs.", 
            "Someone had deliberatly snapped off one of the legs.",
            "It smells like old wood."),
        GameObject(
            "Journal",
            "The final entry states that the time should be hours then minutes then seconds (H-M-S).",
            "The cover is worn and several pages are missing.",
            "It smells like musty leather."),
        GameObject(
            "Bowl of soup",
            "It appears to be tomato soup.",
            "It has cooled down to room temerature.",
            "You detect 7 different herbs and spices."),
        GameObject(
            "Clock",
            "The hour hand is pointing towards the soup, the minute hand towards the chair, and the second hand towards the sweater.",
            "The battery compartment is open and empty.",
            "It smells of plactic."),
        ]
    
    #run the main game loop
    def take_turn(self):
        prompt = self.get_room_prompt()
        selection = int(input(prompt))
        if selection >= 1 and selection <= 5:
            self.select_object(selection-1)
            self.take_turn()
        else:
            result = self.guess_code(selection)
            if result:
                print("Congratulations! You escaped!")
            elif self.attempts == 3:
                print("You failed to escape and ran out of guess attempts.  Better luck next time.")
            else:
                print(f"Incorrect guess.  You have {3 - self.attempts} attemps left.")
                self.take_turn()
        

    #return a prompt string telling user to enter the code or select one of the GameObjects to interact with
    def get_room_prompt(self):
        prompt = "Enter the 3 digit lock code or choose an item to interact with:\n"
        names = self.room.get_game_object_names()
        index = 1
        for name in names:
            prompt += f"{index}. {name}\n"
            index += 1
        return prompt
    
    #print out an interaction (look, smell, or touch) with the object at the specified index
    def select_object(self, index:int):
        selected_object = self.room.game_objects[index]
        prompt = self.get_object_interaction_string(selected_object.name)
        interaction = input(prompt)
        clue = self.interact_with_object(selected_object, interaction)
        print(clue)
        return

    #return a string containing the possible interactions along with an object's name
    def get_object_interaction_string(self, name:str):
        return f"How would you like to interact with the {name}?\n1. Look\n2. Touch\n3. Smell\n"

    #return a string representing an interaction with an object(call objects look, touch, or sniff method)
    def interact_with_object(self, object, interaction):
        if interaction == '1':
            return object.look()
        elif interaction == '2':
            return object.touch()
        elif interaction == '3':
            return object.sniff()
        else:
            return "Invalid interaction choice.  Please try again"
        
    def guess_code(self, code:int):
        if self.room.check_code(code):
            return True
        else:
            self.attempts += 1
            return False

game = Game()
game.take_turn()

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


#tests = RoomTests()
#tests.test_check_code()
#tests.test_get_game_object_names()