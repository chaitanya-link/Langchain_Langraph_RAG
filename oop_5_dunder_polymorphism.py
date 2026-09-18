class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        # controls what print(object) shows
        return f"Agent(name={self.name}, role={self.role})"

    def work(self):
        print(f"{self.name} is doing generic agent work.")


class ResearchAgent(Agent):
    def work(self):                  # SAME method name, DIFFERENT behavior
        print(f"{self.name} is researching the web.")


class CoderAgent(Agent):
    def work(self):                  # SAME method name, DIFFERENT behavior
        print(f"{self.name} is writing code.")


agents = [
    Agent("Generic-Bot", "base agent"),
    ResearchAgent("Researcher-Bot", "web researcher"),
    CoderAgent("Coder-Bot", "code generator"),
]

for a in agents:
    print(a)         # uses __str__ automatically
    a.work()          # POLYMORPHISM: same call, different behavior per class