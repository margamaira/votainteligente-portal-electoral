from django import forms


class OneAnswerForm(forms.Form):
    question = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        self.question_ = args[0].pop('question')
        super(OneAnswerForm, self).__init__(*args, **kwargs)
        self.fields['question'].label = self.question_.label
        choices = []
        for position in self.question_.positions.all():
            choices.append((position.id, position.label))
        self.fields['question'].choices = choices

