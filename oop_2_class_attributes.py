class Agent:
    # CLASS ATTRIBUTE — defined directly inside the class, NOT inside __init__
    # Shared by every object made from this class
    company = "KrishAI Technologies"

    def __init__(self, name, role):
        self.name = name      # instance attribute — unique per object
        self.role = role      # instance attribute — unique per object

    def introduce(self):
        print(f"Hi, I'm {self.name}, working as a {self.role} at {self.company}.")


agent1 = Agent("Researcher-Bot", "web researcher")
agent2 = Agent("Coder-Bot", "code generator")

agent1.introduce()
agent2.introduce()

print(agent1.company)   # accessing class attribute via an object
print(Agent.company)    # accessing class attribute via the class itself