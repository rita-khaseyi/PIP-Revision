fun main() {
    var stories = Story("80 pages","Handwork is the key to success",18,true,"Hardwork Pays")
    var telling = StoryTeller("Alberto","English",true)
    var translating = Translator("Khosa","Alberto","English")
    println(translating.translate())
    println(telling.tellStory())


    val jollofRice = NigerianRecipe(
        "Jollof Rice",
        "Nigeria",
        listOf("rice", "tomatoes", "onions", "peppers", "chicken"),
        "1 hour",
        "Steamed",
        listOf("fats", "carbs", "proteins"),
        true
    )
    println(jollofRice.nigerianJollofRice())
    val injera = EthiopianRecipe(
        "Injera",
        "Ethiopia",
        listOf("dough", "onions", "tomatoes", "apricots", "almonds"),
        "2 hours",
        "fried",
        listOf("fat", "carbs", "vitamins"),
        "so soft"
    )
    println(injera.injeraMeal())
    val moroccanChicken = MoroccanRecipe(
        "Moroccan Chicken with Tangerine",
        "Morocco",
        listOf(
            "chicken", "tangerine", "onion", "garlic", "olive oil",
            "cumin", "coriander", "cinnamon", "paprika", "salt", "pepper"
        ),
        "1 hour",
        "grilling",
        listOf("high in protein and vitamin C"),
        true
    )
    println(moroccanChicken.moroccanChickenTangerine())
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

//2.
    open class Recipe(
    val name: String,
    val country: String,
    val ingredients: List<String>,
    val preparationTime: String,
    val cookingMethod: String,
    val nutritionInfo: List<String>
)
class MoroccanRecipe(
    name: String,
    country: String,
    ingredients: List<String>,
    preparationTime: String,
    cookingMethod: String,
    nutritionInfo: List<String>,
    val spicy: Boolean
) : Recipe(name, country, ingredients, preparationTime, cookingMethod, nutritionInfo) {
    fun moroccanChickenTangerine(): String {
        return if (ingredients.contains(cookingMethod)) {
            "The Moroccan food is prepared with $ingredients using $cookingMethod."
        } else {
            "That is not Moroccan food."
        }
    }
}
class NigerianRecipe(
    name: String,
    country: String,
    ingredients: List<String>,
    preparationTime: String,
    cookingMethod: String,
    nutritionInfo: List<String>,
    val pepperish: Boolean
) : Recipe(name, country, ingredients, preparationTime, cookingMethod, nutritionInfo) {
    fun nigerianJollofRice(): String {
        return if (preparationTime.isNotBlank() && nutritionInfo.contains(pepperish.toString())) {
            "The Nigerian food is prepared with $ingredients for $preparationTime. " +
                    "It has to be $cookingMethod for it to have $nutritionInfo and must have $pepperish."
        } else {
            "That is not a well-prepared Jollof Rice."
        }
    }
}
class EthiopianRecipe(
    name: String,
    country: String,
    ingredients: List<String>,
    preparationTime: String,
    cookingMethod: String,
    nutritionInfo: List<String>,
    val soft: String
) : Recipe(name, country, ingredients, preparationTime, cookingMethod, nutritionInfo) {
    fun injeraMeal(): String {
        return "Injera is cooked using $ingredients for $preparationTime. " +
                "It is sweet when $cookingMethod for it to have $nutritionInfo and must be $soft."
    }
}
