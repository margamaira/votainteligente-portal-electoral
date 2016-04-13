# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-11 20:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('popular_proposal', '0005_popularproposal_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposalLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('proposal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popular_proposal.PopularProposal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('proposal_like', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='popular_proposal.ProposalLike')),
            ],
        ),
    ]