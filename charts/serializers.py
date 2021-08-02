from rest_framework import serializers


class AmiiboChartSerializer(serializers.Serializer):
    def get_amiibo_chart(self, validated_data):
        return 'Sucesso'
    
 
    