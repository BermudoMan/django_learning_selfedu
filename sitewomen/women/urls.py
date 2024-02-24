from django.urls import path, re_path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.WomenHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.WomenCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.TagPostList.as_view(), name='tag'),
    path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'),
    path('delete/<slug:slug>/', views.DeletePage.as_view(), name='delete_page'),
    # path('cats/<int:cat_id>/', views.categories, name='cats_id'), # http://127.0.0.1:8000/cats/1/
    # path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),  # http://127.0.0.1:8000/cats/dfsfsd/
    # path('archive/<year4:year>/', views.archive, name='archive'),
    # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive),
]