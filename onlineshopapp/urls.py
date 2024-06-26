from django.urls import path
from .views import *

app_name = "onlineshopapp"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("all-products/", AllProductsView.as_view(), name="allproducts"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="productdetail"),

    path('add-to-cart-<int:pro_id>/', AddToCartView.as_view(), name="addtocart"),
    path('my-cart/', MyCartView.as_view(), name="mycart"),
    path("manage-cart/<int:cp_id>/", ManageCartView.as_view(), name="managecart"),
    path("empty-cart/", EmptyCartView.as_view(), name="emptycart"),

    path("checkout/", CheckOutView.as_view(), name="checkout"),

    path("register/", CustomerRegistrationView.as_view(), name="customerregistration"),
    path("logout/", CustomerLogoutView.as_view(), name="customerlogout"),
    path("login/", CustomerLoginView.as_view(), name="customerlogin"),

    path("profile/", CustomerProfileView.as_view(), name="customerprofile"),
    path("profile/order-<int:pk>/", CustomerOrderDetailView.as_view(), name="customerorderdetail"),

    path("search/", SearchView.as_view(), name="search"),

    # admin side pages
    path("admin-login/", AdminLoginView.as_view(), name="adminlogin"),
    path("admin-pending-orders/", AdminPendingOrdersView.as_view(), name="adminpendingorders"),
    path("admin-order/<int:pk>/", AdminOrderDetailView.as_view(), name="adminorderdetail"),
    path("admin-all-orders/", AdminOrderListView.as_view(), name="adminorderlist"),
    path("admin-order-<int:pk>-change/", AdminOrderStatusChangeView.as_view(), name="adminorderstatuschange"),
]