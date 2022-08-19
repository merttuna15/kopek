from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from kopek2.api.serializers import *
from kopek2.models import *


class BaseViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        read_serializer_class = getattr(self, "read_serializer_class", None)
        if read_serializer_class and self.action in ['list', 'retrieve']:
            return read_serializer_class
        else:
            return self.serializer_class


class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class CountryViewSet(BaseViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    read_serializer_class = CountryReadSerializer


class CityViewSet(BaseViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    read_serializer_class = CityReadSerializer


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer


class IllnessViewSet(viewsets.ModelViewSet):
    queryset = Illness.objects.all()
    serializer_class = IllnessSerializer


class IllnessTypeViewSet(viewsets.ModelViewSet):
    queryset = IllnessType.objects.all()
    serializer_class = IllnessTypeSerializer


class JudgeViewSet(viewsets.ModelViewSet):
    queryset = Judge.objects.all()
    serializer_class = JudgeSerializer


class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer


class GadgetTypeViewSet(viewsets.ModelViewSet):
    queryset = GadgetType.objects.all()
    serializer_class = GadgetTypeSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555.objects.all()
    serializer_class = DoctorSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer


class PetViewSet(BaseViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    read_serializer_class = PetReadSerializer


class PetChallengeViewSet(viewsets.ModelViewSet):
    queryset = PetChallenge.objects.all()
    serializer_class = PetChallengeSerializer


class PetIllnessViewSet(viewsets.ModelViewSet):
    queryset = PetIllness.objects.all()
    serializer_class = PetIllnessSerializer
