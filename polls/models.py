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
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1) # ���翡�� �Ϸ����� �� ����

	 
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE) # Question ���̺��� �����ϰڴ�.
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default=0)  # ������ �ʵ�

	def __str__(self):
		return self.choice_text 