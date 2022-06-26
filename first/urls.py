from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('categories/',views.categories,name='categories'),
    path('foods/',views.foods,name='foods'),
    path('order/<int:id>',views.order,name='order'),
    path('category_food/',views.category_food,name='category_food'),
    path('food_search/',views.food_search,name='food_search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)