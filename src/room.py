# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = "Sorry, not possible move."
        self.s_to = "Sorry, not possible move."
        self.e_to = "Sorry, not possible move."
        self.w_to = "Sorry, not possible move."

    def __str__(self):
        return f"name: {self.name}, description: {self.description}"

