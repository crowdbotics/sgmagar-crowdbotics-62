from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'django-twitter-api', 'url': 'http://pypi.python.org/pypi/django-twitter-api/0.2.10'},
	{'name':'django-twitterbootstrap-form', 'url': 'http://pypi.python.org/pypi/django-twitterbootstrap-form/0.4.0'},
	{'name':'django-twitter-feed', 'url': 'http://pypi.python.org/pypi/django-twitter-feed/0.2'},
	{'name':'django-twitterflux', 'url': 'http://pypi.python.org/pypi/django-twitterflux/0.0.3'},
	{'name':'django-twitter', 'url': 'http://pypi.python.org/pypi/django-twitter/0.1.0'},
	{'name':'django-paypal', 'url': 'http://pypi.python.org/pypi/django-paypal/0.4.1'},
	{'name':'cmsplugin-twitter', 'url': 'http://pypi.python.org/pypi/cmsplugin-twitter/1.1.2'},
    ]
    context = {
        'title': 'sgmagar-crowdbotics-62',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
