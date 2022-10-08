def hide_and_seek():
    print("Who wants to play a game?")
    print("It's time to play hide and seek!")
    print("Run, run, run! Time to run and hide! ")
def greet():
    print("Hello Jack")
    print("How do you do Jack?")
    print("Isn't the weather nice today?")
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is the like in {location}")          
hide_and_seek()
greet()
greet_with_name("Jack")
greet_with("Joe","Nowhere")
greet_with(location="LA",name="Bill")
