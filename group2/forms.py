from django import forms

from group2.models import PartnerFindingProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = PartnerFindingProfile
        fields = ['biography', 'appear_in_search', 'language_proficiency', 'learning_goal']
        exclude = ['user', 'created_at', 'updated_at']
        widgets = {
            'biography': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'appear_in_search': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'language_proficiency': forms.Select(attrs={'class': 'form-select'}),
            'learning_goal': forms.Select(attrs={'class': 'form-select'}),
        }