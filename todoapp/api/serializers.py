from rest_framework import serializers
from base.models import Task, User


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = ['id', 'url', 'user','title', 'due_date']


class UserSeralizer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='task-detail'
    )

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'tasks'] 