from rest_framework import serializers
from .models import Programmers


class ProgrammersSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = Programmers
        fields = '__all__'
