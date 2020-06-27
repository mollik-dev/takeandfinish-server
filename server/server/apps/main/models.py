from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Level(models.Model):
	level_name = models.CharField('Наименование уровня', max_length=50)
	level_description = models.TextField('Описание уровня')
	level_pubdate = models.DateTimeField('Дата публикации', auto_now = True)
	level_content = models.TextField('Код уровня')

	def __str__(self):
		return self.level_name

class LevelRating(models.Model):
	level = models.ForeignKey(Level, on_delete = models.CASCADE)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	rating = models.IntegerField('Рейтинг')

	def __str__(self):
		return self.rating