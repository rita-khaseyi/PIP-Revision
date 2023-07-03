

class Story:
    def __init__(self, story_name, length, moral_lesson, age_group):
        self.story_name = story_name
        self.length = length
        self.moral_lesson = moral_lesson
        self.age_group = age_group
    def info(self):
        print(f"The story {self.story_name} has a moral lesson '{self.moral_lesson}' and is for ages {self.age_group}.")
    def is_appropriate_for_age(self, age):
        try:
            min_age, max_age = map(int, self.age_group.split("-"))
            return min_age <= age <= max_age
        except ValueError:
            return False
class StoryTeller(Story):
    def __init__(self, name, language, is_available=True):
        super().__init__("", "", "", "")
        self.name = name
        self.language = language
        self.is_available = is_available
    def tell_story(self, story):
        if self.is_available:
            return f"The storyteller {self.name} is telling a story in {self.language}."
        else:
            return f"The storyteller {self.name} is not available."
    def set_availability(self, is_available):
        self.is_available = is_available
class Translator(StoryTeller):
    def __init__(self, name, language, target_language, is_available=True):
        super().__init__(name, language, is_available)
        self.target_language = target_language
    def translated_story(self, story):
        if self.is_available:
            return f"The story has been translated from {self.language} to {self.target_language}."
        else:
            return f"The translator {self.name} is not available."
# Create a story
story1 = Story("The Cat and the Dog", "10 pages", "Don't be greedy", "children")
story1.info()
# Check if the story is appropriate for a given age
age = 8
is_appropriate = story1.is_appropriate_for_age(age)
if is_appropriate:
    print(f"The story is appropriate for age {age}.")
else:
    print(f"The story is not appropriate for age {age}.")
# Creating a storyteller
storyteller1 = StoryTeller("Rita", "English")
print(storyteller1.tell_story(story1))
# Set the availability of the storyteller
storyteller1.set_availability(False)
print(storyteller1.tell_story(story1))
# Creating a translator
translator1 = Translator("Wendy", "English", "Swahili")
print(translator1.translated_story(story1))
# Set the availability of the translator
translator1.set_availability(False)
print(translator1.translated_story(story1))




#QUESTION 3
class Species:
    def __init__(self, name, diet, lifespan):
        self.name = name
        self.diet = diet
        self.lifespan = lifespan

class Predator(Species):
    def __init__(self, name, diet, lifespan, hunting_method):
        super().__init__(name, diet, lifespan)
        self.hunting_method = hunting_method

    def hunt_prey(self, prey):
        print(f"{self.name} is hunting {prey.name} using {self.hunting_method}.")
        prey.get_caught()

class Prey(Species):
    def __init__(self, name, diet, lifespan, migration_pattern):
        super().__init__(name, diet, lifespan)
        self.migration_pattern = migration_pattern
        self.caught = False

    def migrate(self, destination):
        print(f"{self.name} is migrating to {destination} following {self.migration_pattern}.")

    def get_caught(self):
        self.caught = True
        print(f"{self.name} got caught by a predator!")

class Park:
    def __init__(self, name):
        self.name = name
        self.species = []

    def add_species(self, species):
        self.species.append(species)

    def show_species(self):
        print(f"Species in {self.name}:")
        for species in self.species:
            print(f"- {species.name}")

    def find_predators(self):
        predators = [species for species in self.species if isinstance(species, Predator)]
        print(f"Predators in {self.name}:")
        for predator in predators:
            print(f"- {predator.name}")

    def find_prey(self):
        prey = [species for species in self.species if isinstance(species, Prey)]
        print(f"Prey in {self.name}:")
        for p in prey:
            print(f"- {p.name}")

lion = Predator("Lion", "Carnivore", 15, "Ambush hunting")
zebra = Prey("Zebra", "Herbivore", 20, "Seasonal migration")
gazelle = Prey("Gazelle", "Herbivore", 12, "Long-distance migration")

park = Park("Wildlife Park")
park.add_species(lion)
park.add_species(zebra)
park.add_species(gazelle)

park.show_species()
park.find_predators()
park.find_prey()

lion.hunt_prey(zebra)
zebra.migrate("Grasslands")

park.find_prey()




class Artist:
    def __init__(self, name, country, instruments):
        self.name = name
        self.country = country
        self.instruments = instruments

    def play_instrument(self, instrument):
        if instrument in self.instruments:
            return f"{self.name} is playing {instrument}."
        else:
            return f"{self.name} does not play {instrument}."
class Performance(Artist):
    def __init__(self, artist, starting_time, finish_time):
        super().__init__(artist.name, artist.country, artist.instruments)
        self.starting_time = starting_time
        self.finish_time = finish_time

    def is_performance_over(self, current_time):
        if current_time >= self.finish_time:
            return True
        else:
            return False

class Stage:
    def__init__(self,name,capacity):
        self.name= name
        self.capacity
        self.performances= []
    
    def add_performance(self,performance):
        self.performances.append(performance)


class Festival:
    def __init__(self):
        self.stages=[]
    
    def add_stage(self,stage):
        self.stages.append(stage)


    def add_performance(self,performance):
        for stage in self.stages:
            if len(stage.performance)==1:
                stage.add_performance(performance)
                return True
            elif performance.starting_time>=stage.performance[-2].finish_time:
                stage.add_performance(performance)
                return True
        return False


class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        if self.price > 0 and self.quantity > 0:
            return f"The total price is {self.price * self.quantity}$"

        else:
            return f"The total price is invalid"

product = Product("apple",122,2)
print(product.total_value())
product1= Product("mango",0,0)
print(product1.total_value())
        
    


