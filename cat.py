# Since we're working toward the goal of building apps for the web, we may as well start with the one thing that the web wouldn't exist without: cats!

# In this exercise, we're going to create a cat class so we can populate our software with a menagerie of feline friends.

# Start a new project (create a new subfolder) and add a new file called "cat.py". Run your program and commit your work after each step.

# Create a class called Cat
# Every cat should have three attributes when they're created: name, preferred_food and meal_time
# Create two instances of the Cat class in your file
# They should each have unique names, preferred foods and meal times
# Let's assume meal_time is an integer from 0 to 23 (representing the hour of the day in 24 hour time)
# Define a __str__() instance method.
# Add an instance method called eats_at that returns the hour of the day with AM or PM that this cat eats.
# The return value should be something like "11 AM" or "3 PM"
# Make sure your method returns this string rather than printing it
# Add another instance method called meow that returns a string of the cat telling you all about itself
# The return value should be something like "My name is Sparkles and I eat tuna at 11 AM"
# Call the meow method on each of the cats you instantiated in step 3

class Cat:
    def __init__(self, name, preferred_food, meal_time):
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time
    def __str__(self):
        return 'meow my name is {}'.format(self.name)
    def eats_at(self):
        if self.meal_time <=12:
            return f'{self.meal_time} am'
        else:
            return f'{self.meal_time-12} pm'
    def meow(self):
        return ('My name is {} and I like {}, I eat at {}'.format(self.name, self.preferred_food, self.eats_at()))
cat1 = Cat('Charlie', 'Kibble', 19)
cat2 = Cat('Lucy', 'Chicken', 6)

print(cat1.meow())
print(cat2.meow())