from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def dishes(request, dish):
    servings = request.GET.get('servings')
    recipe = DATA.get(dish).copy() if DATA.get(dish) is not None else None
    if servings is not None and recipe is not None:
        try:
            servings = int(servings)
            if servings > -1:
                recipe.update((x , y * servings) for x, y in DATA.get(dish).items())
        except:
            pass
    context = {
        'recipe' : recipe
    }
    return render(request, 'calculator/index.html', context)
