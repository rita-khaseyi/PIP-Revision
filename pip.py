

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
