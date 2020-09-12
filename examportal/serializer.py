from rest_framework import serializers
from .models import exam

class examserial(serializers.ModelSerializer):
    class Meta:
        model = exam
        fields = '__all__'