from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Question

# Create your views here.
def index(request):
    latest_question_list=Question.objects.order_by("-pub_date")[:5]
    context={"latest_question_list":latest_question_list}
    return render(request,"polls/index.html",context)
    # return HttpResponse(output)

    # The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.


def detail(request,question_id):
    # return HttpResponse(f"You are looking at the question {question_id}")
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,"polls/detail.html",{"question":question})

def results(request,question_id):
    response=f"you are looking at the results of question {question_id}"
    return HttpResponse(response)

def vote(request,question_id):
    return HttpResponse(f"You're voting on question {question_id}")