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
  }
  
  class StoryTeller extends Story {
    constructor(name, language) {
      super();
      this.name = name;
      this.language = language;
    }
  
    tellStory(story) {
      return `The storyteller ${this.name} is telling a story in ${this.language}`;
    }
  }
  
  class Translator extends StoryTeller {
    constructor(name, language, targetLanguage) {
      super(name, language);
      this.targetLanguage = targetLanguage;
    }
  
    translatedStory(story) {
      return `The story has been translated from ${this.language} to ${this.targetLanguage}`;
    }
  }
  
  class AncestralStory extends Story {
    constructor(storyName, length, moralLesson, ageGroup, generation) {
      super(storyName, length, moralLesson, ageGroup);
      this.generation = generation;
    }
  
    info() {
      console.log(`The ancestral story ${this.storyName} has a moral lesson '${this.moralLesson}', is for ages ${this.ageGroup}, and belongs to the ${this.generation} generation.`);
    }
  }
  
  class OralStory {
    constructor(story, language) {
      this.story = story;
      this.language = language;
    }
  
    recordStory() {
      return `The story '${this.story.storyName}' is being recorded in ${this.language}.`;
    }
  }
  
  class TranslatedStory extends Story {
    constructor(story, targetLanguage) {
      super(story.storyName, story.length, story.moralLesson, story.ageGroup);
      this.targetLanguage = targetLanguage;
    }
  
    info() {
      console.log(`The translated story ${this.storyName} has a moral lesson '${this.moralLesson}' and is for ages ${this.ageGroup}. It has been translated to ${this.targetLanguage}.`);
    }
  }
  
  // Create a story
  const story1 = new Story("The Cat and the Dog", "10 pages", "Don't be greedy", "children");
  story1.info();
  
  // Creating a storyteller
  const storyteller1 = new StoryTeller("Rita", "English");
  
  // Creating a translator
  const translator1 = new Translator("Wendy", "English", "Swahili");
  
  // Telling the story in the original language
  console.log(storyteller1.tellStory(story1));
  
  // Translating the story into the new language
  console.log(translator1.translatedStory(story1));
  
  // Create an ancestral story
  const ancestralStory1 = new AncestralStory("The Lion and the Rabbit", "15 pages", "Cleverness overcomes strength", "all ages", "Great-grandparents");
  ancestralStory1.info();
  
  // Creating an oral story
  const oralStory1 = new OralStory(ancestralStory1, "English");
  
  // Recording the story in the given language
  console.log(oralStory1.recordStory());
  
  // Translating the story into the target language
  const translatedStory1 = new TranslatedStory(ancestralStory1, translator1.targetLanguage);
  translatedStory1.info();
  