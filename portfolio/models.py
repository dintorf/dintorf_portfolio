from __future__ import unicode_literals

from django.db import models


class Portfolio(models.Model):
	name = models.CharField(max_length=100)
	summary = models.ForeignKey(Summary, limit_choices_to=1)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('created',)


class Summary(models.Model):
	name = models.CharField(max_length=100)
	text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('created',)


class Skill(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	position = models.PositiveIntegerField(unique=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('position',)


class TechnicalTool(models.Model):
	name = models.CharField(max_length=100)
	skill = models.ForeignKey(Skill)
	proficiency = models.PositiveIntegerField()
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('proficiency', 'name')


class WorkExperience(models.Model):
	job_title = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	start_date = models.DateField()
	end_date = models.DateField()
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('end_date', 'start_date')


class JobResponsibility(models.Model):
	description = models.TextField()
	job = models.ForeignKey(WorkExperience)
	position = models.PositiveIntegerField(unique=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('position',)
