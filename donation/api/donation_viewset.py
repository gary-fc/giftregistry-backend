from django.db.models import Sum
from rest_framework import serializers, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from donation.models import Donation
from user.api import UserLimitSerializer


class DonationSerializer(serializers.ModelSerializer):
    user = UserLimitSerializer(many=False, read_only=True)

    class Meta:
        model = Donation
        fields = '__all__'


class DonationCustomSerializer(serializers.ModelSerializer):
    userdonation = UserLimitSerializer(many=False, read_only=True)

    class Meta:
        model = Donation
        fields = '__all__'


class DonationCustomLastSerializer(serializers.ModelSerializer):
    userdonation = UserLimitSerializer(many=False, read_only=True)

    class Meta:
        model = Donation
        fields = '__all__'


class DonationSumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'


class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    @action(methods=['GET'], detail=False, url_path='last-donation', url_name="obtener la ultima donacion una campaña")
    def get_last_dontaion(self, request):
        campaign = request.GET['campaign']
        queryset = Donation.objects.filter(campaign=campaign).last()
        serializer = DonationCustomLastSerializer(queryset)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False, url_path='total-recaudado', url_name="obtener el total recaudado")
    def get_total_recaudado(self, request):
        campaign = request.GET['campaign']
        queryset = Donation.objects.filter(campaign=campaign).aggregate(recaudado=Sum('campaign_donation'))
        return Response(queryset)
