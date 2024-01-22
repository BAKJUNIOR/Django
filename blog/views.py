from datetime import datetime

from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "App-blog/index.html", context={"date": datetime.today()})


def article(request, numero):
    return render(request, f"App-blog/article-{numero}.html")
