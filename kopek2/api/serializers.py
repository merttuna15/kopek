from rest_framework import serializers
from kopek2.models import *


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class ColorReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
        depth = 1


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"


class SizeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"
        depth = 1


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class CountryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"
        depth = 1


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class CityReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"
        depth = 1


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class BranchReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"
        depth = 1


class IllnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Illness
        fields = "__all__"


class IllnessReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Illness
        fields = "__all__"
        depth = 2


class IllnessCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IllnessCategory
        fields = "__all__"


class IllnessCategoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = IllnessCategory
        fields = "__all__"
        depth = 1


class IllnessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IllnessType
        fields = "__all__"


class IllnessTypeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = IllnessType
        fields = "__all__"
        depth = 1


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = "__all__"


class AwardReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = "__all__"
        depth = 1


class JudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = "__all__"


class JudgeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = "__all__"
        depth = 1


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"


class HospitalReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"
        depth = 2


class GadgetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GadgetType
        fields = "__all__"


class GadgetTypeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = GadgetType
        fields = "__all__"
        depth = 1


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"


class OwnerReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"
        depth = 2


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
        # depth = 2


class DoctorReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
        depth = 3


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"


class PetReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"
        depth = 1


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = "__all__"


class ChallengeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = "__all__"
        depth = 2


class PetIllnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetIllness
        fields = "__all__"


class PetIllnessReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetIllness
        fields = "__all__"
        depth = 3


class PetChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetChallenge
        fields = "__all__"
        # depth = 3


class PetChallengeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetChallenge
        fields = "__all__"
        depth = 3


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = "__all__"
