from django.shortcuts import render

# Create your views here.


def random(request):

    return render(request, 'chat/basic_count.html', context={'text': "hello world"})
