from django.forms import ModelForm
from keywords.models import Keywords


class KeywordForm(ModelForm):
    class Meta:
        model = Keywords
        fields = ['word']