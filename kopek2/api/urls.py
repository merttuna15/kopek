from rest_framework.routers import DefaultRouter

from kopek2.api.views import *

router = DefaultRouter()

router.register('color', ColorViewSet)
router.register('size', SizeViewSet)
router.register('country', CountryViewSet)
router.register('city', CityViewSet)
router.register('branch', BranchViewSet)
router.register('hospital', HospitalViewSet)
router.register('illness', IllnessViewSet)
router.register('illnesstype', IllnessTypeViewSet)
router.register('doctor', DoctorViewSet)
router.register('gadgettype', GadgetTypeViewSet)
router.register('award', AwardViewSet)
router.register('judge', JudgeViewSet)
router.register('owner', OwnerViewSet)
router.register('challenge', ChallengeViewSet)




urlpatterns = router.urls