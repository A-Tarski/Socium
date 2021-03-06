from django import forms
from . import models

class ReportForm(forms.ModelForm):

    plate_nubmer = forms.CharField(max_length=20, label='Номер автомобиля', help_text='Только российские номера')

    class Meta:
        model = models.Report
        fields = ('plate_nubmer', 'header', 'description', 'video_link_report', 'image_report',)
        # widgets = {
        #     'image_report': forms.FileInput(),
        # }

    def clean(self):
        cleaned_data = super().clean()
        # print(cleaned_data)
        return cleaned_data



class CommentForm(forms.ModelForm):

    class Meta():
        model = models.Comment
        fields = ('body',)
        widgets = {
          'body': forms.Textarea(attrs={'rows':3}),
        }
        labels = {'body': ""}

class LikeForm(forms.ModelForm):

    class Meta():
        model = models.Like
        fields = ('side',)
