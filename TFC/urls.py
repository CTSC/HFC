from django.urls import path
from TFC  import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('organizations',views.OrganizationListView.as_view(),name='organization_list'),
    path('organizations/signup',views.OrganizationCreateView.as_view(),name='organization signup'),
    path('setpassword/<auth_token>',views.PasswordResetView.as_view(),name="setpassword"),
    path('login',views.LoginView.as_view(),name="login"),
    path('members',views.MemberListView.as_view(),name='team_member'),
    path('dashboard',views.OrgDashboard.as_view(),name='dashboard'),
    path('logout',views.logout,name='logout'),
    path('volunteer',views.VolunteerCreateView.as_view(),name='volunteer signup'),
    path('addmember',views.MemberCreateView.as_view(),name='member signup'),
    path('volunteerlist',views.VolunteerList.as_view(),name='volunteerlist'),
    path('memberupdate/<member_id>',views.MemberUpdate.as_view(),name='memberupdate'),
    path('memberdelete/<member_id>',views.MemberDelete.as_view(),name='memberdelete'),

    
]