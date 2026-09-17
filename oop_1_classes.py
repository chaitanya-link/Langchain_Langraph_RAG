class Agent:
    def __init__(self, name, role):
        self.name = name      # instance attribute
        self.role = role      # instance attribute

    def introduce(self):      # instance method
        print(f"Hi, I'm {self.name}, and I work as a {self.role}.")


# Creating objects (instances) from the Agent class
agent1 = Agent("Researcher-Bot", "web researcher")
agent2 = Agent("Coder-Bot", "code generator")


agent1.introduce()
agent2.introduce()