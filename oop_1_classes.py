class Agent:
    def __init__(self, name, role):
        self.name = name      # instance attribute
        self.role = role      # instance attribute

    def change_role(self, new_role):
        self.role = new_role   # now properly indented inside the method

    def introduce(self):      # instance method
        print(f"Hi, I'm {self.name}, and I work as a {self.role}.")


# Creating objects (instances) from the Agent class
agent1 = Agent("Researcher-Bot", "web researcher")
agent2 = Agent("Coder-Bot", "code generator")
agent3 = Agent("Farmer", "Code farmer")

agent1.introduce()
agent2.introduce()
agent3.introduce()

# testing change_role
agent3.change_role("Senior Code Farmer")
agent3.introduce()