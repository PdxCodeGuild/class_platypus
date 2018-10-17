from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import MapType, Title

from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'demograph/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Title.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Title
    template_name = 'demograph/detail.html'


class ResultsView(generic.DetailView):
    model = Title
    template_name = 'demograph/results.html'


def vote(request, title_id):
    title = get_object_or_404(Title, pk=title_id)
    try:
        selected_choice = title.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'demograph/detail.html', {
            'title': title,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('demograph:results', args=(title.id,)))

