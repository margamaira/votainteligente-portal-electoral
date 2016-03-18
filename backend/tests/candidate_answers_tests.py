# coding=utf-8
from elections.tests import VotaInteligenteTestCase as TestCase
from backend.models import CandidateAnswerIdentifier
from elections.models import Candidate
from django.core.urlresolvers import reverse


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
