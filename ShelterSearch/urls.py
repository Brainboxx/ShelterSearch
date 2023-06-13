from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.views import home, contact, RegisterView, AboutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/index.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('contact/', contact, name='contact'),
    path('properties/', include('properties.urls')),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', include('blog.urls')),
    path('agents/', include('agents.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
