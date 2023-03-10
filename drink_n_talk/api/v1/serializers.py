from rest_framework import serializers

from core.models import Bar, Drink, Language, Theme
from users.serializers import UserSerializer


class LanguageSerializer(serializers.ModelSerializer):
    """Сериализатор для языков общения."""

    class Meta:
        model = Language
        fields = ('name', 'abbreviation')


class DrinkSerializer(serializers.ModelSerializer):
    """Сериализатор для напитков."""

    users = UserSerializer(many=True)

    class Meta:
        model = Drink
        fields = ('title', 'degree', 'users')


class ThemeSerializer(serializers.ModelSerializer):
    """Сериализатор для тем общения."""

    class Meta:
        model = Theme
        fields = ('title', 'tag')


class BarSerializer(serializers.ModelSerializer):
    """Сериализатор для барных стоек."""

    initiator = UserSerializer()
    participants = UserSerializer(many=True)
    theme = ThemeSerializer()
    language = LanguageSerializer()

    class Meta:
        model = Bar
        fields = '__all__'


class BarCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания барных стоек."""

    initiator = UserSerializer(
        default=serializers.CurrentUserDefault(),
        read_only=True
    )
    participants = UserSerializer(
        default=serializers.CurrentUserDefault(),
        read_only=True
    )
    theme = serializers.SlugRelatedField(
        queryset=Theme.objects.all(),
        slug_field='tag'
    )
    language = serializers.SlugRelatedField(
        queryset=Language.objects.all(),
        slug_field='abbreviation'
    )

    class Meta:
        model = Bar
        fields = '__all__'

    def to_representation(self, instance):
        """
        После создания объект барной стойки сериализуется через
        `BarSerializer`.
        """
        return BarSerializer(instance, context=self.context).data
