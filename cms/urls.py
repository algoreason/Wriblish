from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.home, name='home'),
	url(r'^categories/(?P<category_id>[0-9]+)$',views.posts, name='postsByTopic'),
	url(r'^login/auth/$',views.login_proc, name='loginAuth'),
	url(r'^login/*$',views.loginInitialization, name='loginInitialization'),
	url(r'^login/(?P<error>error)$',views.loginRetry, name='loginRetry'),
	url(r'^addPost$',views.addPostInit, name='addPostInit'),
	url(r'^savePost$',views.savePost, name='savePost'),
	url(r'^logout/$',views.logout_view, name='logout'),
	url(r'^registerNew/$',views.register, name='register'),
	url(r'^register/$',views.registerInit, name='registerInit'),
	url(r'^myProfile/$',views.profileView, name='profileView'),
]
