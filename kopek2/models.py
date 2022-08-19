from datetime import datetime

from django.db import models

from kopek2.helpers import IllnessCategory


class Color(models.Model):
    name = models.CharField(max_length=32, verbose_name="colorNames", unique=True)


class Size(models.Model):
    name = models.CharField(max_length=32, verbose_name="size")


class Country(models.Model):
    name = models.CharField(max_length=32, verbose_name="country")


class City(models.Model):
    name = models.CharField(max_length=32, verbose_name="city")
    country = models.ForeignKey(Country, verbose_name="country", related_name="countries", on_delete=models.CASCADE)


class Branch(models.Model):
    name = models.CharField(max_length=64, verbose_name="branch")


class Hospital(models.Model):
    name = models.CharField(max_length=512, verbose_name="hospital")
    address = models.TextField(verbose_name="address")
    phone = models.CharField(max_length=11, blank=True, null=True)
    city = models.ForeignKey(City, verbose_name="City", on_delete=models.CASCADE)


class Race(models.Model):
    name = models.CharField(max_length=64, unique=True)


class IllnessType(models.Model):
    name = models.CharField(max_length=512)


class Illness(models.Model):
    name = models.CharField(max_length=512)
    branch = models.ForeignKey(Branch, verbose_name="branch", on_delete=models.CASCADE)
    is_medicine = models.BooleanField(verbose_name="isMedicine")


class Judge(models.Model):
    first_name = models.CharField(max_length=128, verbose_name="firstName")
    last_name = models.CharField(max_length=128, verbose_name="lastName")
    birth_date = models.DateField()
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)

    @property
    def age(self):
        return datetime.now().date() - self.birth_date


class Award(models.Model):
    name = models.CharField(max_length=512)


class GadgetType(models.Model):
    dress = models.TextField(blank=True, null=True)
    shoes = models.TextField(blank=True, null=True)
    collet = models.TextField(blank=True, null=True)


class Doctor(models.Model):
    first_name = models.CharField(max_length=128, verbose_name="firstName")
    last_name = models.CharField(max_length=128, verbose_name="lastName")
    branch = models.ForeignKey(Branch, verbose_name="branch", null=True, on_delete=models.SET_NULL)
    hospital = models.ForeignKey(Hospital, verbose_name="Hospital", null=True, on_delete=models.SET_NULL)
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)


class Owner(models.Model):
    first_name = models.CharField(max_length=128, verbose_name="firstName")
    last_name = models.CharField(max_length=128, verbose_name="lastName")
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    tc = models.CharField(max_length=11, unique=True)
    city = models.ForeignKey(City, verbose_name="City", null=True, on_delete=models.SET_NULL)
    address = models.TextField()


class Pet(models.Model):
    name = models.TextField(verbose_name="Name")
    color = models.ForeignKey(Color, verbose_name="Color", null=True, on_delete=models.SET_NULL)
    size = models.ForeignKey(Size, verbose_name="Size", null=True, on_delete=models.SET_NULL)
    birth_date = models.DateField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="pets")
    parent = models.ForeignKey("self", verbose_name="Parent", null=True, on_delete=models.SET_NULL, related_name="pets")
    race = models.ForeignKey(Race, verbose_name="Race", null=True, on_delete=models.SET_NULL)
    illness = models.ManyToManyField(Illness, verbose_name="Illness")
    gadget = models.ForeignKey(GadgetType, verbose_name="Gadget", null=True, on_delete=models.SET_NULL)

    @property
    def age(self):
        return datetime.now().date() - self.birth_date


class Challenge(models.Model):
    name = models.CharField(max_length=512)
    country = models.ForeignKey(Country, verbose_name="Country", null=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(City, verbose_name="City", null=True, on_delete=models.SET_NULL)
    address = models.TextField()
    judge = models.ManyToManyField(Judge, verbose_name="judge", related_name="judges")
    pet = models.ManyToManyField(Pet, verbose_name="pet", related_name="pet")


class PetIllness(models.Model):
    type = models.ForeignKey(IllnessType, verbose_name="IllnessType", null=True, on_delete=models.SET_NULL)
    pet = models.ForeignKey(Pet, verbose_name="pet", null=True, on_delete=models.SET_NULL)
    category = models.TextField(choices=IllnessCategory.choices)


class PetChallenge(models.Model):
    race = models.ForeignKey(Race, related_name="races", verbose_name="race", null=True, on_delete=models.SET_NULL)
    pet = models.ManyToManyField(Pet, verbose_name="pet")
    challenge = models.ManyToManyField(Challenge, verbose_name="challenge")
    award = models.ForeignKey(Award, verbose_name="award", null=True, on_delete=models.SET_NULL)
