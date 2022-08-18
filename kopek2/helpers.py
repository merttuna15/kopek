from django.db import models


class IllnessCategory(models.TextChoices):
    STOMACH = "Stomach"
    HEART = "Heart"
    BOWEL = "Bowel"
    BRAIN = "Brain"
    BONE = "Bone"
    MUSCLE = "Muscle"
