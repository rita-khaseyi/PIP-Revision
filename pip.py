

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



# question2
class Recipe:
    def __init__(self, uniqueIngredients, preparationTime, cookingMethod, nutritionalInfo):
        self.uniqueIngredients = uniqueIngredients
        self.preparationTime = preparationTime
        self.cookingMethod = cookingMethod
        self.nutritionalInfo = nutritionalInfo
class MoroccanRecipe(Recipe):
    def __init__(self, uniqueIngredients, preparationTime, cookingMethod, nutritionalInfo, spicy):
        super().__init__(uniqueIngredients, preparationTime, cookingMethod, nutritionalInfo)
        self.spicy = spicy

    def Moroccan_chicken_tagine(self):
        return f"The Moroccan Chicken Tagine is prepared using {self.spicy} and {self.uniqueIngredients} for {self.preparationTime}. It is cooked by {self.cookingMethod} to give {self.nutritionalInfo}."

    def is_vegetarian(self):
        if "chicken" not in self.uniqueIngredients and "beef" not in self.uniqueIngredients and "lamb" not in self.uniqueIngredients:
            return True
        else:
            return False
class NigerianRecipe(Recipe):
    def __init__(self, uniqueIngredients, preparationTime, cookingMethod, nutritionalInfo, peprish):
        super().__init__(uniqueIngredients, preparationTime, cookingMethod, nutritionalInfo)
        self.peprish = peprish

    def jollof_rice(self):
        return f"The popular Nigerian Jollof Rice is prepared using {self.uniqueIngredients} for {self.preparationTime}, making it {self.peprish}. It's cooked by {self.cookingMethod} and is recommended because it has {self.nutritionalInfo}."

    def is_spicy(self):
        if "pepper" in self.uniqueIngredients or "chili" in self.uniqueIngredients:
            return True
        else:
            return False
class EthiopianRecipe(Recipe):
    def __init__(self, uniqueIngredients, preparationTime, cookingMethod, nutritionalInfo, saucy):
        super().__init__(uniqueIngredients, preparationTime, cookingMethod, nutritionalInfo)
        self.saucy = saucy

    def injera(self):
        return f"Injera is cooked using {self.uniqueIngredients} for {self.preparationTime}, and you have to {self.cookingMethod} for it to be sweet. Injera is the best because it has {self.nutritionalInfo}."

    def is_gluten_free(self):
        if "teff flour" in self.uniqueIngredients:
            return True
        else:
            return False
