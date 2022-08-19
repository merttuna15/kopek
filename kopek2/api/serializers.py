from rest_framework import serializers

from kopek2.models import Branch, Award, Judge, Pet, PetChallenge, PetIllness, \
    Challenge, Hospital, Owner, Doctor, IllnessType, IllnessCategory, GadgetType, Illness, Color, Size, Country, City, \
    Race


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"
        # #depth = 1


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class IllnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Illness
        fields = "__all__"
        # depth = 1


class IllnessCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IllnessCategory
        fields = "__all__"


class IllnessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IllnessType
        fields = "__all__"


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = "__all__"


class JudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = "__all__"


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"
        # depth = 2


class GadgetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GadgetType
        fields = "__all__"


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"
        # ##depth = 2


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
        # depth = 2


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"
        # depth = 2


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = "__all__"
        # depth = 2


class PetIllnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetIllness
        fields = "__all__"
        # depth = 1d>


class PetChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetChallenge
        fields = "__all__"
        # depth = 3


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = "__all__"
