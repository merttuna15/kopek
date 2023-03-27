from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from kopek2.api.serializers import *
from kopek2.models import *


class BaseViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        read_serializer_class = getattr(self, "read_serializer_class", None)
        if read_serializer_class and self.action in ['list', 'retrieve']:
            return read_serializer_class
        else:
            return self.serializer_class


class ColorViewSet(BaseViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    read_serializer_class = ColorReadSerializer


class SizeViewSet(BaseViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    read_serializer_class = SizeReadSerializer


class CountryViewSet(BaseViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    read_serializer_class = CountryReadSerializer


class CityViewSet(BaseViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    read_serializer_class = CityReadSerializer


class BranchViewSet(BaseViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    read_serializer_class = BranchReadSerializer


class HospitalViewSet(BaseViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    read_serializer_class = HospitalReadSerializer


class RaceViewSet(BaseViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    read_serializer_class = RaceSerializer


class IllnessViewSet(BaseViewSet):
    queryset = Illness.objects.all()
    serializer_class = IllnessSerializer
    read_serializer_class = IllnessReadSerializer


class IllnessTypeViewSet(BaseViewSet):
    queryset = IllnessType.objects.all()
    serializer_class = IllnessTypeSerializer
    read_serializer_class = IllnessTypeReadSerializer


class JudgeViewSet(BaseViewSet):
    queryset = Judge.objects.all()
    serializer_class = JudgeSerializer
    read_serializer_class = JudgeReadSerializer


class AwardViewSet(BaseViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
    read_serializer_clas = AwardReadSerializer


class GadgetTypeViewSet(BaseViewSet):
    queryset = GadgetType.objects.all()
    serializer_class = GadgetTypeSerializer
    read_serializer_class = GadgetTypeReadSerializer


class DoctorViewSet(BaseViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    read_serializer_class = DoctorReadSerializer


class OwnerViewSet(BaseViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    read_serializer_class = OwnerReadSerializer


class ChallengeViewSet(BaseViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    read_serializer_class = ChallengeReadSerializer


class PetViewSet(BaseViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    read_serializer_class = PetDetailSerializer


class PetChallengeViewSet(BaseViewSet):
    queryset = PetChallenge.objects.all()
    serializer_class = PetChallengeSerializer
    read_serializer_class = PetChallengeReadSerializer


class PetIllnessViewSet(BaseViewSet):
    queryset = PetIllness.objects.all()
    serializer_class = PetIllnessSerializer
    read_serializer_class = PetIllnessReadSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.order_by('-creation_date')
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
