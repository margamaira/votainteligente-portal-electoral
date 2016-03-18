from __future__ import unicode_literals

from django.db import models
from elections.models import Candidate
from preguntales.models import uuid_with_no_dashes

# Create your models here.
class CandidateAnswerIdentifier(models.Model):
    candidate = models.ForeignKey(Candidate, related_name='answer_identifiers')
    key = models.CharField(max_length=255, default=uuid_with_no_dashes)
