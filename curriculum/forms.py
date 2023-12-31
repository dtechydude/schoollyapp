# from xml.etree.ElementTree import Comment
from django import forms
from .models import Lesson, Comment, Reply



class LessonForm(forms.ModelForm):
   
    class Meta:
        
        model = Lesson
        fields = ('lesson_id', 'name', 'position', 'ppt', 'video', 'comment')
        widgets = {
            'comment': forms.Textarea(attrs={'class':'form-control', 'rows':4, 'cols':70, 'placeholder':"Enter Your Comment"}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        labels = {"body":"Comment:"}

        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control', 'rows':4, 'cols':70, 'placeholder':"Enter Your Comment"}),
        }

        # def __init__(self, *args, **kwargs):
        #     self.request = kwargs.pop('request', None)
        #     super(CommentForm, self).__init__(*args, **kwargs)


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply_body',)

        widgets = {
            'reply_body': forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':10}),
        }


    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request', None)
    #     super(ReplyForm, self).__init__(*args, **kwargs)

