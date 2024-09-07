from django import forms

from common.models import Slider


class SliderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Slider
        fields = (
                "title",
                "description",
                "image",
                )

        widgets = {
                "title": forms.TextInput(
                    attrs={"class": "form-control", "language": "all"}
                    ),

                "description": forms.TextInput(
                    attrs={"class": "form-control", "language": "all"}
                    ),
                "image" : forms.ClearableFileInput(),
            
                
                }
