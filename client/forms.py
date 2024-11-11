from django import forms

from client.models import Git


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'


class GitForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Git
        fields = ('name',)

