from django import forms

from .validators import validate_com, validate_url


class SubmitURLForm(forms.Form):
    url = forms.CharField(
        label="Submit URL",
        validators=[validate_url, validate_com]
    )

    # Clean Called Every Time Form is Submitted
    # def clean(self):
    #     cleaned_data = super(SubmitURLForm, self).clean()
    #     url = cleaned_data.get('url')
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL for this field")
    #     return url

    # Validate on Field
    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     if "http" in url:
    #         return url
    #     return "http://" + url
