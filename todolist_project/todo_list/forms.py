from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        # model = Task
        fields = ['title'] # This will allow us to use all the fields in the model