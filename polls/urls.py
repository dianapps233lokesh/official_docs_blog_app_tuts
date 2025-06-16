from django.urls import path
# from .views import index,detail,results,vote
from . import views

# The tutorial project has just one app, polls. In real Django projects, there might be five, ten, twenty apps or more. How does Django differentiate the URL names between them? For example, the polls app has a detail view, and so might an app on the same project that is for a blog. How does one make it so that Django knows which app view to create for a url when using the {% url %} template tag?

# The answer is to add namespaces to your URLconf. In the polls/urls.py file, go ahead and add an app_name to set the application namespace:

app_name="polls"


urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('<int:pk>/results/', views.ResultView.as_view(), name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote"),
]

# When somebody requests a page from your website – say, “/polls/34/”, Django will load the mysite.urls Python module because it’s pointed to by the ROOT_URLCONF setting. It finds the variable named urlpatterns and traverses the patterns in order. After finding the match at 'polls/', it strips off the matching text ("polls/") and sends the remaining text – "34/" – to the ‘polls.urls’ URLconf for further processing. There it matches '<int:question_id>/', resulting in a call to the detail() view like so:


# detail(request=<HttpRequest object>, question_id=34)

# The question_id=34 part comes from <int:question_id>. Using angle brackets “captures” part of the URL and sends it as a keyword argument to the view function. The question_id part of the string defines the name that will be used to identify the matched pattern, and the int part is a converter that determines what patterns should match this part of the URL path. The colon (:) separates the converter and pattern name.