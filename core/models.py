from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Article(models.Model):
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=300)
	snippet = models.TextField()
	header_img = models.ImageField(upload_to="header_imgs/")
	body = RichTextUploadingField()
	date_posted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
