from django import forms
from .models import *

class AddFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'meal', 'course', 'price', 'image']

    # def __init__(self,*args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['course'].queryset= Course.objects.none()

    #     if 'meal' in self.data:
    #         try:
    #             meal_id =int(self.data.get('meal'))
    #             self.fields['course'].queryset=Course.objects.filter(meal_id=meal_id).order_by('name')
    #         except(ValueError,TypeError):
    #             pass
    #     elif self.instance.pk:
    #         self.fields['course'].queryset = self.instance.meal.course_set.order_by('name')


