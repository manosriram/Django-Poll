from django.shortcuts import render
from .models import Question, Choice
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

# Get questions and display them.


def index(req):
    latestQuestions = {
        'latestQuestions': Question.objects.order_by('-publishedDate')[:5]}
    # context = {'latestQuestionList': latestQuestions}
    return render(req, "polls/index.html", latestQuestions)

# Show specific question and choices.


def detail(req, qID):
    try:
        question = Question.objects.get(pk=qID)
    except Question.DoesNotExist:
        raise Http404("Question Doesn't Exist.")
    return render(req, 'polls/detail.html', {'question': question})

# Get question and display results.


def results(req, qID):
    question = get_object_or_404(Question, pk=qID)
    return render(req, 'polls/results.html', {'question': question})


def vote(req, qID):
    question = get_object_or_404(Question, pk=qID)
    # print(req.POST)
    # print(question.choice_set)

    try:
        selectedChoice = question.choice_set.get(pk=req.POST['choice'])
        # print(selectedChoice)
    except(KeyError, Choice.DoesNotExist):
        return render(req, 'polls/detail.html', {
            'question': question,
            'errorMessage': "You didn't select a choice."
        })
    else:
        selectedChoice.votes += 1
        selectedChoice.save()
        # Always return an HttpResponseRedirect after successfully
        # dealing with POST data. This prevents data from being posted twice if a
        # user hits the back button.
        return HttpResponseRedirect(reverse('polls:results', args=(qID, )))
