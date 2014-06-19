from django.forms import ModelForm, Textarea, TextInput
from flashers.models import Post

class CardForm(ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'question', 'answer')
        widgets = {
            'category': TextInput(attrs={'style': 'width:100%;', 'placeholder': 'Category...'}),
            'question': Textarea(attrs={'cols': 50, 'rows': 10,'style': 'width:100%;', 'placeholder': 'Question...'}),
            'answer': Textarea(attrs={'cols': 50, 'rows': 10, 'style': 'width:100%;', 'placeholder': 'Answer...'}),
        }

