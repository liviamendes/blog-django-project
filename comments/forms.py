from django.forms import ModelForm
from .models import Comment


class FormComment(ModelForm):
    def clean(self):
        data = self.cleaned_data
        name = data.get('comment_name')
        email = data.get('comment_email')
        comment = data.get('comment')

        if len(name) < 5:
            self.add_error(
                'comment_name',
                'Name field must have more than 5 characters'
            )

    class Meta:
        model = Comment
        fields = ('comment_name', 'comment_email', 'comment')
