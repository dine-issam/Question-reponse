from django.forms import ModelForm
from .models import Answer,Question,User

class AnswerForm(ModelForm):
    class Meta:
        model=Answer
        fields=('detail',)
class QuestionForm(ModelForm):
    class Meta:
        model=Question
        fields=('title','detail','tags')

class ProfileForm(ModelForm):
    class Meta:
        model=User
        fields=('first_name','last_name','username')