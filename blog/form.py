from django.forms import ModelForm
from .models import Blog_Model

class Blog(ModelForm):
    class Meta:
        model= Blog_Model
        fields= ['url']
