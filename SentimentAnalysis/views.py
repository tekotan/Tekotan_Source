from django.shortcuts import render
from SentimentAnalysis.Twitter_LSTM import *

# Create your views here.
sentiment_array = []
def evaluate(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        texts = request.POST.get('text')
        # check whether it's valid:
        if len(texts) != 0:
#            temp = '{}) {}: {}'.format(len(sentiment_array)+1,texts,test(texts))
            sentiment_array.append([len(sentiment_array)+1, texts, test(texts)])
            return render(request, 'SentimentAnalysis/index.html', {'Sentiment':sentiment_array})
        else:
            return render(request, 'SentimentAnalysis/index.html', {'Sentiment':'please enter something'})




    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'SentimentAnalysis/index.html', {'Sentiment':sentiment_array})
