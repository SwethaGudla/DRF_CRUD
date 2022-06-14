from rest_framework import serializers
from .models import Task
class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

    def validate_age(self, age_value):
        if age_value<=18:
            message="please enter age is greaterthan 18"
            raise serializers.ValidationError(message)
        else:
            return age_value

    def validate_name(self, name_value):         
        if len(name_value)<=2:
            message="Name should be more than 2 characters..!"
            raise serializers.ValidationError(message)
        else:
            return name_value
        