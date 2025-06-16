from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Question, Choice
from django.db.models import F
from django.urls import reverse

# Create your views here.
def index(request):
    latest_question_list=Question.objects.order_by("-pub_date")[:5]
    context={"latest_question_list":latest_question_list}
    return render(request,"polls/index.html",context)
    # return HttpResponse(output)

    # The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.


# def detail(request,question_id):
#     # return HttpResponse(f"You are looking at the question {question_id}")
#     try:
#         question=Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request,"polls/detail.html",{"question":question})

def detail(request,question_id):
    # return HttpResponse(f"You are looking at the question {question_id}")
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detail.html",{"question":question})

def results(request,question_id):
    # response=f"you are looking at the results of question {question_id}"
    # return HttpResponse(response)

    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/results.html",{"question":question})

def vote(request,question_id):
    # return HttpResponse(f"You're voting on question {question_id}")
    question=get_object_or_404(Question,pk=question_id)
    try:
        print(request.POST["choice"])
        selected_choice=question.choice_set.get(pk=request.POST["choice"])
        print(selected_choice)
    except (KeyError,Choice.DoesNotExist):
        return render(request,"polls/detail.html",{"question":question,"error_message":"You didn't select a choice."})
    else:
        selected_choice.votes=F("votes")+1
        selected_choice.save()

    return HttpResponseRedirect(reverse("polls:results",args=(question.id,)))


#   request.POST is a dictionary-like object that lets you access submitted data by key name. In this case, request.POST['choice'] returns the ID of the selected choice, as a string. request.POST values are always strings.

# Note that Django also provides request.GET for accessing GET data in the same way – but we’re explicitly using request.POST in our code, to ensure that data is only altered via a POST call.

# request.POST['choice'] will raise KeyError if choice wasn’t provided in POST data. The above code checks for KeyError and redisplays the question form with an error message if choice isn’t given.

# F("votes") + 1 instructs the database to increase the vote count by 1.

# After incrementing the choice count, the code returns an HttpResponseRedirect rather than a normal HttpResponse. HttpResponseRedirect takes a single argument: the URL to which the user will be redirected (see the following point for how we construct the URL in this case).

# As the Python comment above points out, you should always return an HttpResponseRedirect after successfully dealing with POST data. This tip isn’t specific to Django; it’s good web development practice in general.

# We are using the reverse() function in the HttpResponseRedirect constructor in this example. This function helps avoid having to hardcode a URL in the view function. It is given the name of the view that we want to pass control to and the variable portion of the URL pattern that points to that view. In this case, using the URLconf we set up in Tutorial 3, this reverse() call will return a string like

# "/polls/3/results/" 