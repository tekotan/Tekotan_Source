from recipe_extraction.ingredient_pull import init
from django.shortcuts import render
# Create your views here.
def get_ingredients(request):
    i = init()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = request.POST.get('recipe')
        # check whether it's valid:
        if len(form) != 0:
            ret_var = i.get_ingredients_string(form)
            return render(request, 'recipe_extraction/index.html', {'ingredients': ret_var})

    # if a GET (or any other method) we'll create a blank form
    else:
        pass

    return render(request, 'recipe_extraction/index.html', {'ingredients': ''})
