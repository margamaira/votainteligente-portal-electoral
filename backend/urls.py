from django.conf.urls import patterns, url
from backend.views import CandidateAnswerView

urlpatterns = patterns('',
    url(r'^candidate_answer/(?P<key>[-\w]+)/?$',
        CandidateAnswerView.as_view(template_name='backend/candidate_answer.html'),
        name='candidate_answer'),
)
