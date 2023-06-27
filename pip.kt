fun main() {
    var stories = Story("80 pages","Handwork is the key to success",18,true,"Hardwork Pays")
    var telling = StoryTeller("Alberto","English",true)
    var translating = Translator("Khosa","Alberto","English")
    println(translating.translate())
    println(telling.tellStory())
}
    open class Story(
        var length: String,
        var moralLesson: String,
        var ageGroup: Int,
        var isAvailable: Boolean,
        var storyName: String
    ) {
        fun isStoryAvailable(): String {
            if (isAvailable) {
                return "The story is available."
            }
            
            else {
                return "The story is not available."
            }
        }
    }
    open class StoryTeller(var tellerName: String, var language: String, var isAvailable: Boolean) {
        fun tellStory(): String {
            return if (isAvailable) {
                "${tellerName} was telling a really interesting story to the children in ${language}."
            } else {
                "${tellerName} does not have any story to tell."
            }
        }
    }
    class Translator(var targetLanguage: String, tellerName: String, language: String) :
        StoryTeller(tellerName, language, true) {
        fun translate(): String {
            return "The story in ${language} was translated to ${targetLanguage}."
        }
    }


