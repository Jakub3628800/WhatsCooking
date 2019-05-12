## define a preprocessing function that can be used on a dataframe in other files
def preprocess_recipes(df):
    from nltk.stem.porter import PorterStemmer
    porter = PorterStemmer()


    import re
    meaningless_words = r'crush|crumbl|ground|minc|powder|chop|slice|free|less|sodium|kosher|plain|natur|extra-virgin'


    # functions operating on an recipe (sentence) level
    lower_recipe = lambda x:[word.lower() for word in x]
    stem_recipe = lambda x:[" ".join([porter.stem(word) for word in ing.split(' ')]) for ing in x]
    remove_meaningless_words_recipe = lambda x: [re.sub(meaningless_words,'',ing).strip() for ing in x]
    replace_whitespaces_recipe = lambda x: [re.sub(' +', '_', string) for string in x]


    # functions operating on a dataset level - to be used for df.assign 
    lower = lambda x: [lower_recipe(recipe) for recipe in x.ingredients]
    stem = lambda x: [stem_recipe(recipe) for recipe in x.ingredients] 
    remove_meaningless_words = lambda x: [remove_meaningless_words_recipe(recipe) for recipe in x.ingredients] 
    replace_whitespace = lambda x: [replace_whitespaces_recipe(recipe) for recipe in x.ingredients]
    join_ingredients = lambda x:[" ".join(recipe) for recipe in x.ingredients]

    return (df.assign(ingredients=lower)
            .assign(ingredients=stem)
            .assign(ingredients=remove_meaningless_words)
            .assign(ingredients=replace_whitespace)
            .assign(ingredients=join_ingredients)
            )
