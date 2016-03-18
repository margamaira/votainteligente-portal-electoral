from django.shortcuts import render
from django.views.generic import DetailView
from elections.models import Candidate
from django.shortcuts import get_object_or_404


class CandidateAnswerView(DetailView):
    model = Candidate

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return get_object_or_404(self.model, answer_identifiers__key=self.kwargs['key'])

    def get_queryset(self):
        qs = self.model.objects.get(answer_identifiers__key=self.kwargs['key'])
        return qs

