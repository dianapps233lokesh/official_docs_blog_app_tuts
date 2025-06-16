from django.urls import path
from .views import index,detail,results,vote


urlpatterns = [
    path('', index, name="index"),
    path('<int:question_id>/', detail, name="detail"),
    path('<int:question_id>/results/', results, name="results"),
    path('<int:question_id>/vote/', vote, name="vote"),
]

# When somebody requests a page from your website – say, “/polls/34/”, Django will load the mysite.urls Python module because it’s pointed to by the ROOT_URLCONF setting. It finds the variable named urlpatterns and traverses the patterns in order. After finding the match at 'polls/', it strips off the matching text ("polls/") and sends the remaining text – "34/" – to the ‘polls.urls’ URLconf for further processing. There it matches '<int:question_id>/', resulting in a call to the detail() view like so:


# detail(request=<HttpRequest object>, question_id=34)

# The question_id=34 part comes from <int:question_id>. Using angle brackets “captures” part of the URL and sends it as a keyword argument to the view function. The question_id part of the string defines the name that will be used to identify the matched pattern, and the int part is a converter that determines what patterns should match this part of the URL path. The colon (:) separates the converter and pattern name.