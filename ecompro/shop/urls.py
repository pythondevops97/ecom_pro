from django.urls import path
from . import views
app_name = 'shop'
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.All_Prod_Cat,name='All_Prod_Cat'),
    path('<slug:c_slug>/',views.All_Prod_Cat,name='Products_By_Category'),
    path('<slug:c_slug>/<slug:product_slug>', views.ProDetail, name='prodcatdetail'),
    path('product/',views.product,name='products'),
]