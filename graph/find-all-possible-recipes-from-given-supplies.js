/**
 * @param {string[]} recipes
 * @param {string[][]} ingredients
 * @param {string[]} supplies
 * @return {string[]}
 */
var findAllRecipes = function(recipes, ingredients, supplies) {
    supplies_set = new Set()
    for(let supply of supplies){
        supplies_set.add(supply)
    }

    recipes_dict = {}
    for(let i = 0;i < recipes.length;i++){
        recipes_dict[recipes[i]] = ingredients[i]
    }

    var craft = function(recipe, ingredients, recipes_used, answer){
        if(recipe in recipes_used){
            return recipes_used[recipe]
        }
        recipes_used[recipe] = false

        for(ingredient of ingredients){
            if(!(supplies_set.has(ingredient)) && !(ingredient in recipes_dict)){
                return false
            }else if(!(supplies_set.has(ingredient)) && ingredient in recipes_dict){
                if(!craft(ingredient, recipes_dict[ingredient], recipes_used, answer)){
                    return false
                }
            }
        }

        supplies_set.add(recipe)
        answer.push(recipe)
        recipes_used[recipe] = true
        return true
    }

    answer = []
    recipes_used = {}
    for(recipe in recipes_dict){
        craft(recipe, recipes_dict[recipe], recipes_used, answer)
    }
    return answer
};