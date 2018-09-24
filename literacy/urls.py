
from django.conf.urls import url,include

from .views import (
    PaymentAPIView,
    CallBackURL,
    RootAPIView,
    InitializePaymentAPIView
    )


urlpatterns = [
    url(r'^api/v1/$', RootAPIView.as_view(), name='root_api'),


    url(r'^payment-pay/$', PaymentAPIView.as_view(), name='storystory_stk_pay'),

    url(r'^call-back/$', CallBackURL.as_view(), name='call_back'),

    url(r'^initialize-payment/$', InitializePaymentAPIView.as_view(), name='initialize_payment')
]
