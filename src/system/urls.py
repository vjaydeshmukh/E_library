from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'system'
urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
    path('view_books/', views.viewbooks, name='viewbooks'),
    path('user_login/', auth_views.LoginView.as_view(template_name='system/userlogin.html'), name='userlogin'),
    path('admin_login/', views.adminlogin, name='adminlogin'),
    path('signup/', views.signup, name='signup'),
    path('admin_author_management/', views.adminauthormanagement, name='adminauthormanagement'),
    path('admin_member_management/', views.adminmembermanagement, name='adminmembermanagement'),
    path('admin_book_issuing/', views.adminbookissuing, name='adminbookissuing'),
    path('admin_book_inventory/', views.adminbookinventory, name='adminbookinventory'),
    path('admin_publisher_management/', views.adminpublishermanagement, name='adminpublishermanagement'),
    path('shyamkumaryadav/', views.shyamkumaryadav	, name='shyamkumaryadav'),
    path('<int:pk>/update', views.AuthorUpdate.as_view(template_name="system/shyamkumaryadav.html"), name="update"),
    # path('', ),
]
