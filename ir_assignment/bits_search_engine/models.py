from django.db import models

class ExtractedWords(models.Model):
    file_name = models.CharField(max_length=100, default=None)
    file_path = models.CharField(max_length=100, default=None)
    time_frame = models.CharField(max_length=100, default=None)
    keywords = models.TextField(max_length=5000, default=None) # stopwords are REMOVED
    content = models.TextField(max_length=5000, default=None)
    
    len_key = models.IntegerField() #
    og_wordSTP = models.TextField(max_length=5000, default=None) # keywords WITH stopwords
    len_keyog_wordSTP = models.IntegerField()


class InvertedIndex(models.Model):
    keywords = models.TextField(max_length=5000, default=None) # stopwords are REMOVED
    term_index = models.TextField(max_length=5000, default=None) 
