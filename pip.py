

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
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f"{self.name} from {self.country}"


class Performance:
    def __init__(self, artist, start_time, end_time):
        self.artist = artist
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"Performance by {self.artist}, {self.start_time} to {self.end_time}"


class Stage:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.performances = []

    def add_performance(self, performance):
        self.performances.append(performance)

    def is_available(self, start_time, end_time):
        for performance in self.performances:
            if (start_time >= performance.start_time and start_time < performance.end_time) or \
                    (end_time > performance.start_time and end_time <= performance.end_time) or \
                    (start_time <= performance.start_time and end_time >= performance.end_time):
                return False
        return True

    def __str__(self):
        return f"Stage: {self.name}, Capacity: {self.capacity}, Performances: {len(self.performances)}"


class Festival:
    def __init__(self, name):
        self.name = name
        self.stages = []

    def add_stage(self, stage):
        self.stages.append(stage)

    def schedule_performance(self, performance):
        for stage in self.stages:
            if stage.is_available(performance.start_time, performance.end_time):
                stage.add_performance(performance)
                return True
        return False

    def print_schedule(self):
        print(f"--- {self.name} Schedule ---")
        for stage in self.stages:
            print(f"\n{stage.name}:")
            for performance in stage.performances:
                print(performance)

# Create artists
artist1 = Artist("Femi Kuti", "Nigeria")
artist2 = Artist("Salif Keita", "Mali")
artist3 = Artist("Angelique Kidjo", "Benin")

# Create performances
performance1 = Performance(artist1, "18:00", "19:30")
performance2 = Performance(artist2, "20:00", "21:30")
performance3 = Performance(artist3, "19:00", "20:30")
performance4 = Performance(artist2, "22:00", "23:30")

# Create stages
stage1 = Stage("Main Stage", 5000)
stage2 = Stage("Acoustic Stage", 1000)

# Create festival
festival = Festival("Pan-African Music Festival")

# Add stages to festival
festival.add_stage(stage1)
festival.add_stage(stage2)

# Schedule performances
if festival.schedule_performance(performance1):
    print(f"Performance by {performance1.artist} scheduled successfully.")
else:
    print(f"Unable to schedule performance by {performance1.artist}.")
if festival.schedule_performance(performance2):
    print(f"Performance by {performance2.artist} scheduled successfully.")
else:
    print(f"Unable to schedule performance by {performance2.artist}.")
if festival.schedule_performance(performance3):
    print(f"Performance by {performance3.artist} scheduled successfully.")
else:
    print(f"Unable to schedule performance by {performance3.artist}.")
if festival.schedule_performance(performance4):
    print(f"Performance by {performance4.artist} scheduled successfully.")
else:
    print(f"Unable to schedule performance by {performance4.artist}.")

# Print festival schedule
festival.print_schedule()

# QUESTION 4



