from django.db import models


class Letter(models.Model):
    id = models.AutoField(primary_key=True)
    letter = models.CharField(max_length=15)
    last_word_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'letter'


class Category(models.Model):
    id = models.IntegerField(primary_key=True)


class Word(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.TextField(unique=True)
    transcription = models.TextField(null=True, blank=True)
    link = models.TextField()

    class Meta:
        db_table = 'word'


class Description(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    sentence = models.TextField(null=True, blank=True)
    source = models.TextField(null=True, blank=True)
    word = models.ForeignKey(Word, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'description'

