import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1) # 현재에서 하루전날 즉 어제

	 
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE) # Question 테이블을 참조하겠다.
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default=0)  # 숫자형 필드

	def __str__(self):
		return self.choice_text 