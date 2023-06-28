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

  

  class Species {
    constructor(name, diet, lifespan) {
      this.name = name;
      this.diet = diet;
      this.lifespan = lifespan;
    }
  }
  
  class Predator extends Species {
    constructor(name, diet, lifespan, huntingMethod) {
      super(name, diet, lifespan);
      this.huntingMethod = huntingMethod;
    }
  
    huntPrey(prey) {
      console.log(`${this.name} is hunting ${prey.name} using ${this.huntingMethod}.`);
      prey.getCaught();
    }
  }
  
  class Prey extends Species {
    constructor(name, diet, lifespan, migrationPattern) {
      super(name, diet, lifespan);
      this.migrationPattern = migrationPattern;
      this.caught = false;
    }
  
    migrate(destination) {
      console.log(`${this.name} is migrating to ${destination} following ${this.migrationPattern}.`);
    }
  
    getCaught() {
      this.caught = true;
      console.log(`${this.name} got caught by a predator!`);
    }
  }
  
  class Park {
    constructor(name) {
      this.name = name;
      this.species = [];
    }
  
    addSpecies(species) {
      this.species.push(species);
    }
  
    showSpecies() {
      console.log(`Species in ${this.name}:`);
      for (const species of this.species) {
        console.log(`- ${species.name}`);
      }
    }
  
    findPredators() {
      const predators = this.species.filter(species => species instanceof Predator);
      console.log(`Predators in ${this.name}:`);
      for (const predator of predators) {
        console.log(`- ${predator.name}`);
      }
    }
  
    findPrey() {
      const prey = this.species.filter(species => species instanceof Prey);
      console.log(`Prey in ${this.name}:`);
      for (const p of prey) {
        console.log(`- ${p.name}`);
      }
    }
  }
  
  const lion = new Predator("Lion", "Carnivore", 15, "Ambush hunting");
  const zebra = new Prey("Zebra", "Herbivore", 20, "Seasonal migration");
  const gazelle = new Prey("Gazelle", "Herbivore", 12, "Long-distance migration");
  
  const park = new Park("Wildlife Park");
  park.addSpecies(lion);
  park.addSpecies(zebra);
  park.addSpecies(gazelle);
  
  park.showSpecies();
  park.findPredators();
  park.findPrey();
  
  lion.huntPrey(zebra);
  zebra.migrate("Grasslands");
  
  park.findPrey();

  