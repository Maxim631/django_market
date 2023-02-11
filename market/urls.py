from django.urls import path
from . import views

app_name = 'market'
urlpatterns = [
    path('', views.main, name="main"),
    path('products', views.ShowProducts.as_view(), name="products"),
    path('products/<int:product_id>', views.ShowProduct.as_view(), name="product"),
    path('products/new_order', views.NewOrder.as_view(), name="new-order"),

    path('profile', views.ShowProfile.as_view(), name="profile"),
    path('profile/<int:order_id>/edit_order', views.EditOrder.as_view(), name="edit-order"),
    path('profile/<int:order_id>/delete_order', views.DeleteOrder.as_view(), name="delete_order"),

    path('tickets/', views.AddPoints.as_view(), name="tickets")

]