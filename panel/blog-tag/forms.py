from django import forms

from common.models import BlogTag


class BlogTagForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = BlogTag
        fields = (
                "title",
                )

        widgets = {
                "title": forms.TextInput(
                    attrs={"class": "form-control", "language": "all"}
                    ),
                }
