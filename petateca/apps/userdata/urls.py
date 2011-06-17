from django.conf.urls.defaults import *
from registration.forms import RegistrationFormUniqueEmail
#from invitation.views import register 
from registration.views import register

urlpatterns = patterns('',
    # Usuarios, invitaciones, registros, avatar, etc
    #(r'^', include('registration.urls')),
    url(r'^register/$',
        register,
        {
            'backend': 'registration.backends.default.DefaultBackend',
            'form_class': RegistrationFormUniqueEmail
        },
        name='registration_register'),
    url(r'^activate/$', 'userdata.views.activate_by_code', name="activate_by_code"),
    (r'^', include('registration.backends.default.urls')),
    (r'^profile/$', 'userdata.views.view_profile'),
    (r'^avatar/', include('avatar.urls')),
    url(r'^tracking/$', 'userdata.views.show_tracking', name='show_tracking'),
    # DEPRECATED
    #(r'^', include('invitation.urls')),
    #url(r'^signin/$',
    #    auth_views.login,
    #    {
    #        'template_name': 'invitation/signin.html', 
    #    },
    #    name='auth_login'),
   # url(r'^invitation/request/$', 'userdata.views.request_invitation', name='request_invitation'),

)
