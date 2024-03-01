class Human:
    def __init__(self, pos_x, pos_y, steps, stamina):
        # Encapsulate the parameters into instance variables
        # These variables can only be accessed and modified internally within the class,
        # promoting data integrity and protecting the object's state.
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__steps = steps
        self.__stamina = stamina

    # This internal method checks if there's enough stmaina for a sprint
    def __raise_if_cannot_sprint(self):
        if self.__stamina <= 0:
            raise Exception("not enough stamina to sprint")

    # Internal method to decrease stamina by 1
    def __use_sprint_stamina(self):
        self.__stamina -= 1

    # Internal method that combines the actions needed for any sprint
    def __sprint(self, direction):
        self.__raise_if_cannot_sprint()
        for _ in range(self.__steps * 2):
            direction()
        self.__use_sprint_stamina()

    # This hides the internal logic of how a 'move' operation is performed,
    # and provides a single point of control over the object’s state.
    # Instead of modifying the positions externally,
    # we abstract that logic into an internal method
    # that the user can call with their object e.g. bob.move_right()
    # Calling this method makes the human 'move right',
    # without the user needing to understand or manage the object's internal details
    def move_right(self):
        self.__pos_x += self.__steps

    def move_left(self):
        self.__pos_x -= self.__steps

    def move_up(self):
        self.__pos_y += self.__steps

    def move_down(self):
        self.__pos_y -= self.__steps

    # Sprint methods for each direction
    # They use __sprint and pass the move method as a direction
    def sprint_right(self):
        self.__sprint(self.move_right)

    def sprint_left(self):
        self.__sprint(self.move_left)

    def sprint_up(self):
        self.__sprint(self.move_up)

    def sprint_down(self):
        self.__sprint(self.move_down)

    def get_position(self):
        print(f"X: {self.__pos_x}\nY: {self.__pos_y}\n")


bob = Human(0, 0, 1, 10)
bob.get_position()
bob.sprint_right()
bob.sprint_up()
bob.get_position()

# class Human:
#     def __init__(self, name):
#         self.name = name
#         self.__is_alive = True

#     def get_status(self):
#         if self.__is_alive:
#             return "Alive"
#         else:
#             return "Dead"

# bob = Human("Bob")
# print(bob.get_status())
# bob.__is_alive = False
# print(bob.get_status())
