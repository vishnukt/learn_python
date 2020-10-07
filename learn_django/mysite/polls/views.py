# from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse

from django.http import HttpResponseRedirect

from .models import Question, Choice

from django.urls import reverse

# from django.template import loader

from django.shortcuts import render, get_object_or_404

# from django.http import Http404

from django.views import generic

from django.utils import timezone

# from django.contrib.auth.forms import UserCreationForm

# from django import forms

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    '''def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.all()'''


class DetailView(LoginRequiredMixin, generic.DetailView):
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(LoginRequiredMixin, generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class all_results(LoginRequiredMixin, generic.ListView):
    # model = Question
    template_name = 'polls/all_results.html'
    context_object_name = 'qlist'

    def get_queryset(self):
        return Question.objects.all()


# class registeration(generic.DetailView):
#     model = Question
#     template_name = 'polls/registeration.html'

@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/question_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


'''def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)'''


'''def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})'''

'''def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/question_detail.html', {'question': question})'''
