class Story {
    constructor(storyName, length, moralLesson, ageGroup) {
      this.storyName = storyName;
      this.length = length;
      this.moralLesson = moralLesson;
      this.ageGroup = ageGroup;
    }
  
    info() {
      console.log(`The story ${this.storyName} has a moral lesson '${this.moralLesson}' and is for ages ${this.ageGroup}.`);
    }
  
    isAppropriateForAge(age) {
      const [minAge, maxAge] = this.ageGroup.split('-').map(Number);
      return age >= minAge && age <= maxAge;
    }
  }
  
  class StoryTeller extends Story {
    constructor(name, language, isAvailable = true) {
      super("", "", "", "");
      this.name = name;
      this.language = language;
      this.isAvailable = isAvailable;
    }
  
    tellStory(story) {
      if (this.isAvailable) {
        return `The storyteller ${this.name} is telling a story in ${this.language}.`;
      } else {
        return `The storyteller ${this.name} is not available.`;
      }
    }
  
    setAvailability(isAvailable) {
      this.isAvailable = isAvailable;
    }
  }
  
  class Translator extends StoryTeller {
    constructor(name, language, targetLanguage, isAvailable = true) {
      super(name, language, isAvailable);
      this.targetLanguage = targetLanguage;
    }
  
    translatedStory(story) {
      if (this.isAvailable) {
        return `The story has been translated from ${this.language} to ${this.targetLanguage}.`;
      } else {
        return `The translator ${this.name} is not available.`;
      }
    }
  }
  
  // Create a story
  const story1 = new Story("The Cat and the Dog", "10 pages", "Don't be greedy", "children");
  story1.info();
  
  // Check if the story is appropriate for a given age
  const age = 8;
  const isAppropriate = story1.isAppropriateForAge(age);
  console.log(`The story is ${isAppropriate ? 'appropriate' : 'not appropriate'} for age ${age}.`);
  
  // Creating a storyteller
  const storyteller1 = new StoryTeller("Rita", "English");
  console.log(storyteller1.tellStory(story1));
  
  // Set the availability of the storyteller
  storyteller1.setAvailability(false);
  console.log(storyteller1.tellStory(story1));
  
  // Creating a translator
  const translator1 = new Translator("Wendy", "English", "Swahili");
  console.log(translator1.translatedStory(story1));
  
  // Set the availability of the translator
  translator1.setAvailability(false);
  console.log(translator1.translatedStory(story1));
  ////////////////////////////////////////////////////////////
  //QUESTION 2
  class Recipe {
    constructor(name, country, ingredients, preparationTime, cookingMethod, nutritionInfo) {
      this.name = name;
      this.country = country;
      this.ingredients = ingredients;
      this.preparationTime = preparationTime;
      this.cookingMethod = cookingMethod;
      this.nutritionInfo = nutritionInfo;
    }
  }
  class MoroccanRecipe extends Recipe {
    constructor(name, country, ingredients, preparationTime, cookingMethod, nutritionInfo, spicy) {
      super(name, country, ingredients, preparationTime, cookingMethod, nutritionInfo);
      this.spicy = spicy;
    }
  
    moroccanChickenTangerine() {
      if (this.ingredients.includes(this.cookingMethod)) {
        return `The Moroccan food is prepared with ${this.ingredients} using ${this.cookingMethod}.`;
      } else {
        return `That is not Moroccan food.`;
      }
    }
  }
  
  class NigerianRecipe extends Recipe {
    constructor(name, country, ingredients, preparationTime, cookingMethod, nutritionInfo, pepperish) {
      super(name, country, ingredients, preparationTime, cookingMethod, nutritionInfo);
      this.pepperish = pepperish;
    }
  
    prepare() {
      if (this.preparationTime && this.nutritionInfo.includes(this.pepperish)) {
        return `The Nigerian Jollof Rice is prepared with ${this.ingredients} for ${this.preparationTime}.
        It has to be ${this.cookingMethod} for it to have ${this.nutritionInfo} and must have ${this.pepperish}.`;
      } else {
        return `That is not a well-prepared Jollof Rice.`;
      }
    }
  }

  class EthiopianRecipe extends Recipe{
    constructor(name, country, ingredients, preparationTime, cookingMethod, nutritionInfo,soft){
      super(name, country, ingredients, preparationTime, cookingMethod, nutritionInfo);
      this.soft = soft
    }
    Injerameal(){
      return `Injera is cooked using  ${this.ingredients} for ${this.preparationTime}.
      It is sweet when ${this.cookingMethod} for it to have ${this.nutritionInfo} must have ${this.pepperish}`
       
  
    }
  }
  const jollofRice = new NigerianRecipe(
    "Jollof Rice",
    "Nigeria",
    ["rice", "tomatoes", "onions", "pepper", "oil"],
    "1 hour",
    "boiling",
    "high in carbohydrates and vitamins",
    true
  );
  
  console.log(jollofRice.prepare());

  // console.log(jollofRice.Nigerianjollofrice())
 
  const Injera = new EthiopianRecipe(
    "Injera",
    "Ethiopa",
    ["dough", "onions", "tomatoes", "apricots", "almonds"],
    "2 hours",
    "fried",
    ["fat", "carbs", "vitamins"] ,
    "yeast,carbs",
    
  );
  console.log(Injera.Injerameal())


  const moroccanChicken = new MoroccanRecipe(
    "Moroccan Chicken with Tangerine",
    "Morocco",
    ["chicken", "tangerine", "onion", "garlic", "olive oil", "cumin", "coriander", "cinnamon", "paprika", "salt", "pepper"],
    "1 hour",
    "grilling",
    "high in protein and vitamin C",
    true
  );
  
  console.log(moroccanChicken.moroccanChickenTangerine());
  //question3
  /////////////////////////////////////////////////////

  class Species {
    constructor(name, diet, lifespan) {
      this.name = name;
      this.diet = diet;
      this.lifespan = lifespan;
    }
      
    displayInfo() {
      console.log(`Name: ${this.name}`);
      console.log(`Diet: ${this.diet}`);
      console.log(`Lifespan: ${this.lifespan}`);
    }
  }
  class Predator extends Species {
    constructor(name, diet, lifespan, huntingMethod) {
      super(name, diet, lifespan);
      this.huntingMethod = huntingMethod;
    }
  
    displayInfo() {
      super.displayInfo();
      console.log(`Hunting Method: ${this.huntingMethod}`);
    }
  }
  class Prey extends Species {
    constructor(name, diet, lifespan, migrationPattern) {
      super(name, diet, lifespan);
      this.migrationPattern = migrationPattern;
    }
  
    displayInfo() {
      super.displayInfo();
      console.log(`Migration Pattern: ${this.migrationPattern}`);
    }
  }
  
  const lion = new Predator("Lion", "Carnivore", 15, "Stalking");
  lion.displayInfo();
  
  const zebra = new Prey("Zebra", "Herbivore", 25, "Seasonal");
  zebra.displayInfo();
  





  
  //question4
  /////////////////////////////////////////////////////

  class Artist {
    constructor(name, country, musicalStyle, instruments) {
      this.name = name;
      this.country = country;
      this.musicalStyle = musicalStyle;
      this.instruments = instruments;
    }
  }
  
  class Performance extends Artist {
    constructor(artist, startDateTime, endDateTime, stage) {
      this.artist = artist;
      this.startDateTime = startDateTime;
      this.endDateTime = endDateTime;
      this.stage = stage;
    }
    stageArrangements(){
      if (this.artist && this.musicalStyle.includes(this.instruments)) {
        return `The kind of music played on ${this.stage}is Lingala.
        It has to be ${this.startDateTime} to ${this.endDateTime}`;
      } else {
        return `That it is not time to play Lingala`;
      }
    }
  }
  
  class Stage extends Artist{
    constructor(name, capacity) {
      this.name = name;
      this.capacity = capacity;
    }
    stageCapacity(){
      if (this.name === this.artist.includes(this.capacity)) {
        return `The band is complete`
      }
      else{ 
        return `The band is incomplete`
      }
    }

  }
  

  
  