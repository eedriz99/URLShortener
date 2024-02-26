from django.shortcuts import render, redirect
from .models import ShortURL
from urllib.parse import urlparse
from django.views.decorators.http import require_http_methods, require_GET

# Create your views here.


@require_http_methods(['POST', 'GET'])
def index(request):
    if request.method == 'POST':
        long_url = request.POST['url']
        # Checking whether the URL is valid or not
        try:
            parsed_url = urlparse(long_url)
            # print(long_url)
            if all([parsed_url.scheme, parsed_url.netloc]):
                shortener = ShortURL.objects.create(link=long_url)
                return render(request, 'index.html', {'short_url': shortener.get_short_url()})
            else:
                raise ValueError
        except ValueError:
            return render(request, 'index.html', {'error_message': 'Invalid URL'})
    elif request.method == 'GET':
        return render(request, 'index.html')


@require_GET
def shortened(request, slug):
    if request.method == "GET":
        try:
            link = ShortURL.objects.get(slug=slug)
            link.stat += 1
            link.save(update_fields=["stat"])
            return redirect(link.link)
        except ShortURL.DoesNotExist:
            return render(request, 'error.html', {"error_message": slug})
        # else:
        #     link.stat += 1
        #     link.save(update_fields=["stat"])
        #     return redirect(link.link)


@require_http_methods(['POST', 'GET'])
def statistics(request):
    if request.method == 'POST':
        short_url = request.POST['short_url']
        if short_url:
            slug = short_url.split('/')[-1]
            try:
                url = ShortURL.objects.get(slug=slug)
            except ShortURL.DoesNotExist:
                return render(request, "stat.html", {"error_message": "URL not found."})
            else:
                return render(request, "stat.html", {"stat": url.get_stat()})
    elif request.method == 'GET':
        return render(request, 'stat.html')
