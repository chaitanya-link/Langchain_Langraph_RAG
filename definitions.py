OOP in Python — Definitions

1.Class — A blueprint/template for creating objects. Defines what data (attributes) and behavior (methods) something will have. Doesn't do anything by itself until you create an object from it.

2.Object (Instance) — An actual thing created from a class. Each object has its own copy of the data defined in the class.

3.__init__ — A special method (constructor) that runs automatically when a new object is created. Used to set up the object's starting data.

4.self — Refers to "this specific object." Always the first parameter in any method inside a class. Python passes it automatically — you never type it when calling the method.

5.Instance Attribute — A variable that belongs to one specific object (e.g. self.name). Different objects can have different values for it.

6.Class Attribute (Class Variable) — A variable shared by all objects of that class, defined directly inside the class (not inside __init__ with self.). Same value across every object unless individually overridden.

7.Method — A function defined inside a class. Represents a behavior/action the object can perform. Always takes self as its first parameter.

8.Instantiation — The act of creating an object from a class (e.g. agent1 = Agent("Bot", "researcher")).

9.Inheritance — When one class (child/subclass) reuses and extends the code of another class (parent/superclass), instead of rewriting everything from scratch.

10.super() — Used inside a child class to call the parent class's methods (commonly super().__init__() to run the parent's constructor first).

11.Encapsulation — Bundling data and the methods that work on that data together inside a class, and controlling access to that data (e.g. keeping some data "private" so it's only changed through defined methods).

12.Polymorphism — Different classes can have methods with the same name but different behavior, and you can call them the same way without caring which exact class it is.

13.Abstraction — Hiding complex internal details and only exposing what's necessary to use the object (e.g. you call .introduce() without needing to know how it's implemented inside).

14.Dunder/Magic methods — Special methods surrounded by double underscores (e.g. __init__, __str__, __repr__) that let your objects work with built-in Python behavior (printing, creation, comparison, etc.).

15.__str__ — A dunder method that controls what gets printed when you do print(object). Makes output human-readable.
