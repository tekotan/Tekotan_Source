from django.shortcuts import render
from calculator.equation import *
# Create your views here.
def evaluate(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = request.POST.get('ans')
        # check whether it's valid:
        x =False
        xx = False
        y = False
        yy = False
        var_error0 = "You are trying to do a simple expression! Use the equal sign"
        var_error1 = "You are trying to do a linear equation with 1 variable! Use the 1 Variable button"
        var_error2 = "You are trying to do a linear equation with 2 variables! Use the 2 Variable button"
        if len(form) != 0:
            if '=' in request.POST:
                try:
                    ret_var = eval(form)
                    return render(request, 'calculator/index.html', {'answer': ret_var, "error": ""})
                except NameError:
                    for i in form:
                        if i == "x":
                            x = True
                        elif i == "y":
                            y = True
                    if y and x:
                        return render(request, 'calculator/index.html', {'answer': '', "error":var_error2})
                    elif x:
                        return render(request, 'calculator/index.html', {'answer': '', "error":var_error1})
            elif "1 Variable" in request.POST:
                try:
                    ret_var =  solve_1(form)
                    return render(request, "calculator/index.html", {'answer': ret_var, "error": ""})
                except SyntaxError:
                    for i in form:
                        if i == "y":
                            yy = True
                    if yy:
                        return render(request, "calculator/index.html", {'answer': '', "error":var_error2})
                    else:
                        return render(request, "calculator/index.html", {'answer': '', "error":var_error0})
            elif "2 Variable" in request.POST:
                try:
                    ret_var =  solve_2(form)
                    return render(request, "calculator/index.html", {'answer': ret_var, "error": ""})
                except ValueError:
                    for i in form:
                        if i == "x":
                            xx = True
                    if xx:
                        return render(request, "calculator/index.html", {'answer': '', "error":var_error1})
                    else:
                        return render(request, "calculator/index.html", {'answer': '', "error":var_error0})


    # if a GET (or any other method) we'll create a blank form
    else:
        pass

    return render(request, 'calculator/index.html', {'answer': ""})
