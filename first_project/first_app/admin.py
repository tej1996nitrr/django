from django.contrib import admin
# superuser:
#admin,pwd:test
# Register your models here.
from first_app.models import AccessRecord,Topic,Webpage
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)