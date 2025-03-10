from django import forms
from .models import Student, Teacher

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  # Include all fields from the Student model in the form
        # Or, you can explicitly list the fields:
        # fields = ['name', 'grade', 'other_field1', 'other_field2']  # If you don't want all fields

        # To customize widgets (e.g., changing a CharField to a TextField, or adding classes for styling):
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),  # Example
        #     'grade': forms.NumberInput(attrs={'class': 'form-control'}),
        # }

        # To add labels to the form fields
        # labels = {
        #     'name': 'Student Name',
        #     'grade': 'Grade Level',
        # }

        # To add help text
        # help_texts = {
        #     'name': 'Enter the student\'s full name.',
        #     'grade': 'Enter the student\'s current grade level.',
        # }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'  # Include all fields from the Teacher model
        # Or, you can explicitly list the fields:
        # fields = ['name', 'subject', 'other_teacher_field']

        # Customize widgets, labels, and help_texts as needed (same as for StudentForm)
        # widgets = {
        #      'name': forms.TextInput(attrs={'class': 'form-control'}),
        #      'subject': forms.TextInput(attrs={'class': 'form-control'}),
        # }
        # labels = {
        #     'name': 'Teacher Name',
        #     'subject': 'Subject Taught',
        # }
        # help_texts = {
        #     'name': 'Enter the teacher\'s full name.',
        #     'subject': 'Enter the subject the teacher teaches.',
        # }