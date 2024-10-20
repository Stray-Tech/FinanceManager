from django.forms import Form, CharField, Textarea, ModelForm

class UserInput(Form):
    attrs = {
        "data": {
            "wrapperClass": "form"
        },
        "type": "text",
        "id": "user-input",
        "name": "user-input",
        "placeholder": "Enter text here",
        "rows": "4",
        "cols": "10"
    }
    user_input = CharField(widget=Textarea(attrs=attrs), label="Bill Description:")
    # user_input.
    # user_input = CharField(widget=MyWidget, label="Bill Description:")

# class MyForm(ModelForm):
#     class Meta:
#         # model = MyModel
#         fields = ['myfield']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['myfield'].widget.attrs.update({'class': 'myfield-wrapper'})


# class YourForm(Form):
#     ...
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(Div(  # or Fieldset, MultiField, etc.
#             'field1',
#             'field2',
#             template='forms/p.html'
#         ))