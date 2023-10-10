from rest_framework import serializers


class UrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        url = value.get('video_url')
        if url != 'Null':
            if 'youtube' not in url:
                raise serializers.ValidationError('Можно использовать только ссылки с YouTube!')
