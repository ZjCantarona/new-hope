from django import forms

from .models import Member, Ministry, Speaker


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'speaker', 'ministry', 'telephone', 'location', 'fathers_name', 'mothers_name',
                  'guardians_name', 'new_believer_school', 'pays_tithe', 'working', 'schooling',
                  'picture']

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)

        not_required = ('telephone', 'fathers_name', 'mothers_name', 'guardians_name', 'picture')
        for field in not_required:
            self.fields[field].required = False


class MinistryForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'leader', 'description', 'telephone']
        model = Ministry

    def __init__(self, *args, **kwargs):
        super(MinistryForm, self).__init__(*args, **kwargs)

        not_required = ('telephone',)
        for field in not_required:
            self.fields[field].required = False


class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = ['name', 'age', 'telephone', 'picture']

    def __init__(self, *args, **kwargs):
        super(SpeakerForm, self).__init__(*args, **kwargs)

        not_required = ('telephone', 'age', 'picture')
        for field in not_required:
            self.fields[field].required = False
