class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def introduce(self):
        print(f"Hi, I'm {self.name}, and I work as a {self.role}.")


class ResearchAgent(Agent):                 # ResearchAgent INHERITS from Agent
    def __init__(self, name, role, search_engine):
        super().__init__(name, role)        # runs Agent's __init__ first
        self.search_engine = search_engine  # extra data only ResearchAgent has

    def search(self, query):
        print(f"{self.name} is searching '{query}' using {self.search_engine}.")


class CoderAgent(Agent):
    def __init__(self, name, role, language):
        super().__init__(name, role)
        self.language = language

    def write_code(self, task):
        print(f"{self.name} is writing {self.language} code for: {task}")


r1 = ResearchAgent("Researcher-Bot", "web researcher", "Tavily")
c1 = CoderAgent("Coder-Bot", "code generator", "Python")

r1.introduce()      # inherited from Agent
r1.search("agentic AI frameworks")

c1.introduce()      # inherited from Agent
c1.write_code("build a LangGraph node")