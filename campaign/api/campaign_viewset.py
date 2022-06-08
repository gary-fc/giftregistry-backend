import json

from django.db.models import Sum, Q
from rest_framework import viewsets, serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response

from campaign.api import CampaignImgSerializer, CampaignCategorySerializer
from campaign.models import Campaign
from comment.api import CommentSerializer
from donation.api import DonationCustomSerializer
from donation.models import Donation

from user.api import UserLimitSerializer


class CampaignSerializer(serializers.ModelSerializer):
    category = CampaignCategorySerializer(many=False, read_only=True)
    imgs = CampaignImgSerializer(many=True, read_only=True)
    user = UserLimitSerializer(many=False, read_only=True)
    donations = DonationCustomSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Campaign
        fields = '__all__'


class CampaignCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def create(self, request, *args, **kwargs):
        serializer = CampaignCustomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['GET'], detail=False, url_path='view-campaign', url_name='obtener la informacion de una campaña')
    def get_view_campaign(self, request):
        url_campaign = request.GET['url']
        queryset = Campaign.objects.filter(url_campaign=url_campaign).first()
        serializer = self.get_serializer(queryset, many=False)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False, url_path='top-4', url_name='obtener el top 4 de campañas')
    def get_top4_campaign(self, request):
        queryset = Campaign.objects.all()[0:4]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False, url_path='get8', url_name='obtener las 8 ultimas campañas creadas')
    def get_8_campaign(self, request):
        queryset = Campaign.objects.all()[0:12]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False, url_path='get_campaign_for_user', url_name='obtener las campañas de un '                                                              'usuario')
    def get_campaign_for_user(self, request):
        if 'user_id' in request.GET:
            user_id = request.GET['user_id']
        queryset = Campaign.objects.all().filter(user_id=user_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False, url_path='get_campaigns_state',url_name="obtener campañas segun su estado")
    def get_campaigns_pendientes(self, request):
        state = request.GET['state']
        queryset = Campaign.objects.all().filter(state=state)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False, url_path='get_stadisticas',url_name="obtener estadisticas")
    def get_stadisticas(self, request):
        total = Campaign.objects.all().count()
        pendientes = Campaign.objects.all().filter(state=1).count()
        aceptadas = Campaign.objects.all().filter(state=2).count()
        finalizadas = Campaign.objects.all().filter(state=3).count()
        array = [total, pendientes, aceptadas, finalizadas]
        return Response(array)

    @action(methods=['GET'], detail=False, url_path='get_money_generated', url_name="obtener estadisticas de ingresos")
    def get_stadisticas_money(self, request):
        total = Donation.objects.all().aggregate(recaudado_campaigns=Sum('campaign_donation'))
        categorias = (Donation.objects.values('campaign_id').annotate(recaudado_campaigns=Sum('campaign_donation')))
        array = [total, categorias]
        return Response(array)

    @action(methods=['GET'], detail=False,url_path='get_donation_total_campaign', url_name="obtener la donacion total de una campaña")
    def get_donation_total_campaing(self,request):
        id_campaing = request.GET['id_campaign']
        total = Donation.objects.all().filter(campaign_id=id_campaing).aggregate(recaudado_campaigns=Sum('campaign_donation'))
        return  Response(total)

    @action(methods=['GET'], detail=False, url_path='get_campaigns_search',
            url_name="obtener campañas por criterio de busqueda")
    def get_campaigns_search(self, request):
        q = request.GET['q']
        queryset = Campaign.objects.all().filter(Q(campaign_name__contains=str(q)) | Q(campaign_description__contains=str(q)))
        serializer = self.get_serializer(queryset, many= True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False, url_path='get_campaigns_category',
            url_name="obtener campañas por categoria")
    def get_campaigns_category(self, request):
        category = request.GET['category']
        queryset = Campaign.objects.all().filter(category_id=category)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)




