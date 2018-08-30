
from django.conf.urls import url,include

from .views import PaymentAPIView,CallBackURL


urlpatterns = [
    url(r'^payment-pay/$', PaymentAPIView.as_view(), name='storystory-pay'),

    url(r'^call/$', CallBackURL.as_view(), name='call_back'),
]
