from django.urls import path

from Accounts.views import (

    UserLoginView,
    UserRegistrationView,
    UserPasswordChangeView,
    # PassUserProfileView,
    PasswordResetView,
    UserPasswordResetView,
     ProfileView,
    # UserProfileView,
   

    
 
)

urlpatterns = [
    path(
        "register/", UserRegistrationView.as_view(), name="register"
    ),  # Registation of user
    path("login/", UserLoginView.as_view(), name="UserLogin"),  # User Login
    # path("profile/", UserProfileView.as_view(), name="user_view"),  #User Profile View
    path("profile/", ProfileView.as_view(), name="user_view"),  # Profile View
    path(
        "changepassword/", UserPasswordChangeView.as_view(), name="user_password_change"
    ),  # Password Change
    path("send_reset_password_email/",PasswordResetView.as_view(),
         name="send_password_reset_token",
     ),  # Passowrd Reset
     path(
         "user_password_reset/<uid>/<token>/",
         UserPasswordResetView.as_view(),
         name="user_password_reset",
     ),  # PPassword reset token send

     path("student/profile/",UserLoginView.as_view(),name='stu_profile') # url for the student profile


     
]
