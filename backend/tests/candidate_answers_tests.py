# coding=utf-8
from elections.tests import VotaInteligenteTestCase as TestCase
from backend.models import CandidateAnswerIdentifier
from elections.models import Candidate, Topic
from django.core.urlresolvers import reverse
from backend.forms import OneAnswerForm
from django.forms.fields import ChoiceField


class CandidatesAnsweringTestCase(TestCase):
    def setUp(self):
        super(CandidatesAnsweringTestCase, self).setUp()
        self.candidate = Candidate.objects.get(id=4)

    def test_create_identifier_per_candidate(self):
        identifier = CandidateAnswerIdentifier.objects.create(candidate=self.candidate)
        self.assertIn(identifier, self.candidate.answer_identifiers.all())
        self.assertTrue(identifier)
        self.assertTrue(identifier.key)
        self.assertIsInstance(identifier.key, str)
        self.assertNotIn('-', identifier.key)
        url = reverse('backend:candidate_answer', kwargs={'key': identifier.key})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['candidate'], self.candidate)

    def test_answer_form(self):
        question = Topic.objects.get(id=1)
        position_1 = question.positions.get(id=1)
        position_2 = question.positions.get(id=2)
        position_3 = question.positions.get(id=3)
        data = {'question':question}
        form = OneAnswerForm(data)
        self.assertTrue(form)
        self.assertEquals(len(form.fields), 1)
        question_field = form.fields['question']
        self.assertIsInstance(question_field, ChoiceField)
        self.assertEquals(question_field.label, question.label)
        self.assertIn((position_1.id, position_1.label), question_field.choices)

