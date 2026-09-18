# OOP Lesson 1 — Classes & Objects

## Core Idea
A CLASS is a blueprint. An OBJECT is a real thing built from that blueprint.
One class → many objects, each with its own separate data.

---

## The Code, Line by Line

class Agent:
- Declares a new class named "Agent" (this is the blueprint).
- Class names are capitalized by convention (PascalCase).

    def __init__(self, name, role):
- __init__ = constructor. Runs AUTOMATICALLY the moment an object is created.
- This is where you set up the object's starting data.
- Parameters (name, role) are the values you pass in when creating the object.

        self.name = name
        self.role = role
- self = "this specific object" (whichever one is currently being created/used).
- self.name = name  →  "store the value `name` onto THIS object, call it `name`"
- These become INSTANCE ATTRIBUTES — data that belongs to one object only.
- Every object made from this class gets its own separate name/role.

    def change_role(self, new_role):
        self.role = new_role
- A METHOD = a function defined inside a class. Represents a behavior/action.
- Every method needs `self` as its first parameter (Python passes it automatically).
- This method changes the role of ONLY the object it's called on.

    def introduce(self):
        print(f"Hi, I'm {self.name}, and I work as a {self.role}.")
- Another method. Reads this object's own data (self.name, self.role) and prints it.

---

## Creating Objects (Instantiation)

agent1 = Agent("Researcher-Bot", "web researcher")
- This LINE runs __init__ behind the scenes.
- "Researcher-Bot" → becomes self.name
- "web researcher" → becomes self.role
- agent1 is now an OBJECT (instance) of the Agent class.

agent2 = Agent("Coder-Bot", "code generator")
agent3 = Agent("Farmer", "Code farmer")
- Same blueprint, but 3 completely separate objects with their own data.

---

## Calling Methods

agent1.introduce()
- Calls the introduce() method ON agent1.
- Python auto-fills `self` = agent1 behind the scenes.
- You never type `self` yourself when CALLING a method — only when DEFINING one.

agent3.change_role("Senior Code Farmer")
- Updates ONLY agent3's role. agent1 and agent2 stay untouched.

agent3.introduce()
- Prints agent3's NEW role — proof that each object's data is independent.

---

## Key Takeaways (memorize these)

1. Class = blueprint. Object = actual thing made from the blueprint.
2. __init__ runs automatically when an object is created — sets up starting data.
3. self = "this particular object" — always first parameter when DEFINING a method,
   never passed manually when CALLING it.
4. self.something = value  →  creates/updates an INSTANCE ATTRIBUTE (data specific to that object).
5. Changing one object's data (via a method) never affects other objects from the same class.
6. Indentation rule: every line inside a class/function must be indented one level (4 spaces)
   deeper than the line that opened it (the one ending in `:`).

---

## Expected Output
Hi, I'm Researcher-Bot, and I work as a web researcher.
Hi, I'm Coder-Bot, and I work as a code generator.
Hi, I'm Farmer, and I work as a Code farmer.
Hi, I'm Farmer, and I work as a Senior Code Farmer.