from django.shortcuts import render
import operator
from .counter import count_words


def home(request):
    return render(
        request, "index.html", context={"key1": "I am from Python code"}
    )


def result(request):
    article = request.GET["article"]
    var_dict, word_count = count_words(article)
    return render(
        request,
        "result.html",
        context={
            "article": article,
            "word_count": word_count,
            "var_dict": var_dict,
        },
    )
                  