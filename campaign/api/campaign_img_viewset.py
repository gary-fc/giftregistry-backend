from rest_framework import viewsets, serializers

from campaign.models import CampaignImg


class CampaignImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignImg
        fields = '__all__'


class CampaignImgViewSet(viewsets.ModelViewSet):
    queryset = CampaignImg.objects.all()
    serializer_class = CampaignImgSerializer
