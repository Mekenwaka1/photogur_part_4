from django.shortcuts import render
# import ipdb
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from photogur.models import Picture, Comment

def pictures(request):
    # print(Picture.title)
    pictures = Picture.objects.all()
    context = {"pictures": pictures}
    return render(request, 'pictures.html', context)

def picture_show(request, id):
    picture = Picture.objects.get(pk=id)
    context = {'picture': picture}
    return render(request, 'picture.html', context)

def picture_search(request):
    query = request.GET['query']
    search_results = Picture.objects.filter(artist=query)
    context = {'pictures': search_results, 'query': query}
    html_response = render(request, 'new.html', context)
    return HttpResponse(html_response)

# @require_http_methods(['POST'])
def create_comment(request):
    # ipdb.set_trace()
    picture_id = request.POST['picture']
    picture = Picture.objects.filter(id=picture_id)[0]
    name = request.POST['name']
    message  = request.POST['message']
    comment = Comment(name=name, message=message, picture=picture)
    comment.save()
    print(picture)
    return HttpResponseRedirect('/pictures')
