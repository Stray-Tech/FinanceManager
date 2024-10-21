from django.forms import Form, CharField, TextInput, Textarea

class BillTitle(Form):
    attrs = {
        "data": {
            "wrapperClass": "form"
        },
        "type": "text",
        "id": "bill-title",
        "placeholder": "Enter title here"
    }
    user_input = CharField(widget=TextInput(attrs=attrs), label="Bill Title:")

class BillDescription(Form):
    attrs = {
        "data": {
            "wrapperClass": "form"
        },
        "type": "text",
        "id": "bill-description",
        "placeholder": "Enter description here"
    }
    user_input = CharField(widget=Textarea(attrs=attrs), label="Bill Description:")