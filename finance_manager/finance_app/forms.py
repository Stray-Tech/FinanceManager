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