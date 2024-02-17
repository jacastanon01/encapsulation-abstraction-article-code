# Utilizing Encapsulation to Drive Abstraction in Python

I have recently been using [boot.dev](https://www.boot.dev/) to broaden my knowledge of backend technologies. My background is primarily on the front-end so I wanted to explore concepts that I had heard about, but never pursued. One of the concepts I am beginning to learn is Object Oriented Programming with python. While going through the OOP course on boot.dev, I was still struggling to comprehend the differences between a couple core concepts of OOP: abstraction and encapsulation. I knew whenever I would download an npm package, the owner was using abstraction to present a module to the world, but I never knew the _how_ or the _why_. This is my attempt to help solidify my understanding of abstraction and encapsulation and how they are used together based on the lessons from boot.dev.

# OOP

Object oriented-programming (OOP) is a programming paradigm that is designed to make organizing code more manageable and maintainable. As opposed to functional programming, which is what I was used to with javascript, OOP uses classes to model and organize data and behavior. A class is essentially a static model that we can create to help group how we handle data within it. A class can be instantiated which creates an object reference. Each object has all the internal tools of a class, including its attributes (the data itself) and methods (how we want the class to interact with the data). Let's take a look at how we would create a Human class with python

```python
class Human:
	# Our constructor method
	def __init__(self, name):
		# We can reference the name of each instance by the parameter
		# and set our attributes as such
		self.name = name
		self.is_alive = True # Instance variable

bob = Human("Bob")
```

Meet Bob! He was just born when we called `bob = Human("Bob")` and placed in a variable named bob. When we create an object from a class, if we want to to initialize it with data, we have to define a constructor function. `__init__` is a python method that is commonly used to set attributes to our instance. So when bob was created, he was initialized with a name and an `is_alive` variable. When dealing with classes in python, each instance of a class has an implicit argument (`self`) that references the object in memory. If we want to modify our object's data, we need to specify self as a parameter. So when we call `Human('Bob')`, we set our instance's name to the string `Bob` and create and set the instance variable `is_alive` to true. Here we are encapsulating our instance's name variable with the name being passed from the user.

## Encapsulation

Encapsulation is the process of handling the visibility and accessibility of our class properties. Let's take a closer look.
Right now, we have our human and we can reference its internal properties like so:

`print(bob.name)   # Bob`

If we wanted to, we could also change their attributes:

`bob.is_alive = False`

Darn, RIP to Bob I guess. But fortunately we can still resurrect him:

`bob.is_alive = True`

Great! But playing with someone's life like that is not cool, man. Let's protect our fellow Human's life a bit more shall we?

```python
class Human:
	def __init__(self, name):
		self.name = name
		self.__is_alive = True

bob = Human("Bob")
print(bob.__is_alive)
```

Now if you run this code, an AttributeError will prevent you from accessing this variable:

```
    print(bob.__is_alive)
          ^^^^^^^^^^^^^^
AttributeError: 'Human' object has no attribute '__is_alive'
```

Wait, we clearly defined this in our init method. Why are we unable to access it?
In OOP, there are ways to hide certain data properties from others. Although python does not have an explicit private or public naming standard, there are still [conventions](https://docs.python.org/3/tutorial/classes.html#private-variables) we can follow. By creating a variable with an underscore, we are telling other developers this is non-public. When we initialize our human object with double underscores on our `__is_alive` attribute, python creates a non-public `_Human__is_alive`. This is called name-mangling and is handled internally by python. Because these are just conventions there are still ways we can access or modify these properties, but for our purpose we just need to understand the role this plays in encapsulation. So encapsulation is the implementation of exposing or hiding certain attributes or methods within our class. But how do we decide what we want exposed?

## Abstraction

Abstraction is the process of extracting essential information relevant to a purpose while ignoring details not pertinent to that purpose. Most libraries or modules abstract the process of dealing with internal systems and gives us only the relevant information. For example, most shell commands have to communicate with our operating system. When we want to list our directories with `ls`, we do not care _how_ the commands are grabbing the directories and displaying them, we just want the results. Abstraction allows us to provide useful information without exposing the internal logic of a program, it often goes hand-in-hand with encapsulation.

Back to Bob, we have successfully encapsulated his life in our class, but what if we want to check he is still alive? We see the `__is_alive` attribute has two underscores in front of it, indicating that it is intended to stay private. To grab this value, we need to create a public method that can be accessed from our object.

```python
class Human:
	# init method

	# We are using abstraction to read our internal variable
	# The user doesn't need to know the name of which variable we used to check the life status,
	# we are only returning relevant information when this method is called
	def get_status(self):
		if self.__is_alive:
			return "Alive"
		else:
			return "Dead"
```

Now we can call this method to check the status of bob. By abstracting our logic into a method, the user does not need to know how we are checking if our object is alive. However, if for some reason they do know our internal variable, we have successfully encapsulated it so it can only be changed within our class. Try to modify `bob.__is_alive` and then call the get_status method.

```python
print(bob.get_status())
bob.__is_alive = False
print(bob.get_status())
```

Phew, he's still alive! You may have noticed we didn't need to specify an argument when we called get_status, even though it has a self parameter. This is because self can be thought of as an implicit argument that will just reference the object.

## Using encapsulation and abstraction together

Our human is kinda boring right now. All we can do is get its name and life status. Let's add some internal coordinates and some methods to handle movement.

```python
class Human:
	def __init__(self, name, pos_x, pos_y, steps):
        # Encapsulate the parameters into instance variables
        # These variables can only be accessed and modified internally within the class,
        # promoting data integrity and protecting the object's state.
        self.__name = name
		self.__pos_x = pos_x
		self.__pos_y = pos_y
		self.__steps = steps

    # The following methods hide the internal logic of how a 'move' operation is performed,
    # and provide a single point of control over the object’s state.
    # Instead of modifying the positions externally,
    # we abstract that logic into an internal method
    # that the user can call with their object e.g. bob.move_right()
    # Calling this method makes the human 'move right'
    # without the user needing to understand or manage the object's internal details

	def move_right(self):
		self.__pos_x += self.__steps

    def move_left(self):
        self.__pos_x -= self.__steps

    def move_up(self):
        self.__pos_y += self.__steps

    def move_down(self):
        self.__pos_y -= self.__steps

	# Since only we know where we are in our lives,
	# this needs to be abstracted to expose our positions
	def get_position(self):
		return print(f"X: {self.__pos_x}\nY: {self.__pos_y}\n")


bob = Human("Bob", 0, 0, 1)
bob.get_position()
bob.move_right()
bob.get_position()
```

We can now call the move method with a direction and it will update our object's x or y position.

But who wants to move at one speed their whole life? Not Bob! But before we get ahead of ourselves, let's think about what happens when we sprint. We tend to exert our energy more as our moving speed increases. So we need to add a new stamina parameter to keep track of that.

```python
class Human:
	def __init__(self, name, pos_x, pos_y, steps, stamina):
		self.name = name
		self.__pos_x = pos_x
		self.__pos_y = pos_y
		self.__steps = steps
		self.__stamina = stamina
```

Only our human can control their stamina. For this reason, we need to create a private method to handle and check our stamina before we can execute our sprint.

```python
class Human:
	# constructor code

	# This internal method checks if there's enough stamina for a sprint
    def __raise_if_cannot_sprint(self):
        if (self.__stamina <= 0):
            raise Exception("not enough stamina to sprint")

    # Internal method to decrease stamina by 1
    def __use_sprint_stamina(self):
        self.__stamina -= 1

	# rest of code
```

We have everything in place now to create a sprint method. First let's check if we have enough stamina to sprint. If we do, we're gonna need to determine our direction and number of steps. For our purposes, we are just gonna double the number of steps in our sprint. Then we will need to decrease our stamina. We can implement the methods like so:

```python
class Human:
	# constructor code

	def sprint_right(self):
		self.__raise_if_cannot_sprint()
		self.right()
		self.right()
		self.__use_sprint_stamina()

    def sprint_left(self):
	    self.__raise_if_cannot_sprint()
        self.move_left()
        self.move_left()
        self.__use_sprint_stamina()

    def sprint_up(self):
		self.__raise_if_cannot_sprint()
        self.move_up()
        self.move_up()
        self.__use_sprint_stamina()

    def sprint_down(self):
	    self.__raise_if_cannot_sprint()
        self.move_down()
        self.move_down()
        self.__use_sprint_stamina()
```

Take a look at how we structured the logic in these methods, they all follow the same outline with the only difference being the coordinates being set. A lot of repeated code can be abstracted into a singular module that has an explicit purpose. If we wanted to refactor our sprint methods, how could we encapsulate this logic?

Let's define a new method that holds the logic necessary for our human object to sprint

```python
class Human:
	# constrcutor code

	def sprint(self):
		self.__raise_if_cannot_sprint()
		self.__use_sprint_stamina()
```

That's a good start, but now we are exerting stamina and not even moving!? This would be cool if we wanted the behavior to model a treadmill, but Bob wants to move from point A to point B, in double the steps. To reduce repeating ourselves let's use a for-loop here

```python
	# Internal method that combines the actions needed for any sprint
	def sprint(self):
		self.__raise_if_cannot_sprint()
		for _ in range(self.__steps * 2): # instead of only repeating the loop twice, we can multiple the steps by 2
			self.move_right()
		self.__use_sprint_stamina()
```

Okay now we're moving in the right direction. Call `bob.sprint()` and print out the coordinates again. Did you move two places to the right? Excellent! Everything is gonna be all right with this method. Wait... We still need to specify our sprint direction.

Before we move forward, do we want this `sprint` method to be accessible to the user or is this just gonna be an internal method that will only be referenced in our class? We could keep it public and pass a direction as a parameter like so

```python
def sprint(self, direction):
	self.__raise_if_cannot_sprint()
	for _ in range(self.__steps * 2):
		if (direction == "R"):
			self.move_right()
		elif (direction == "L"):
			self.move_left()
	# rest of direction conditions
	self.__use_sprint_stamina()
```

But this opens us up to being responsible for another parameter on our public method. We would need to add error handling, maybe have to define constants with a string of valid direction strings, etc... This would also conflict with how we are already using our move methods.
Instead let's make sure everyone knows this is gonna be a private method that we want to keep contained to our class.

```python
def __sprint(self, direction):
	self.__raise_if_cannot_sprint()
	for _ in range(self.__steps * 2):
		direction()
	self.__use_sprint_stamina()
```

We have successfully encapsulated our abstracted code into a private method! First we recognized a pattern that could be re-used and moved that logic into a single function. Then we encapsulated that function for internal use only.

Now that it's private, I'm not too worried about adding another parameter since we will have total control of what we pass. You can pass functions as parameters to be invoked at a later time so now we want to refactor our sprint methods to call `__sprint` with an argument of which move method we want invoked in our for-loop. Fortunately, we have already defined a function to sprint right and left and so on. Now we can reduce the code to just call this method, but with a parameter to specify the direction:

```python
def sprint_right(self):
	self.__sprint(self.move_right)
```

This is how we can utilize encapsulation to drive abstraction in Python. Now for each sprint method, we are using abstraction by calling `__sprint` and not worrying about how we are moving faster and we are using encapsulation to hide our `__sprint` method from the user. Now to sprint right, you just need to call `sprint_right()` on your object and viola!

## Conclusion

Object-oriented programming offers a powerful paradigm for organizing code, focusing on classes to manage data. Encapsulation, the first key concept, involves controlling access to class properties. In Python, this is achieved through naming conventions and underscores. Recall how we were able to encapsulate the `__is_alive` attribute. On the other hand, abstraction, the second key concept, centers on distilling essential information while hiding implementation details. I hope this article was able to demonstrate how abstraction often complements encapsulation.

My goal is to continue documenting my progress so if I made any mistakes, please reach out so I can continue learning. Feel free to use this code as a playground to enhance your knowledge and see how it could be improved.
