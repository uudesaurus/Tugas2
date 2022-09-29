from atexit import register
from todolist.views import register
from todolist.views import login_user 
from todolist.views import logout_user 

app_name = 'todolist'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]