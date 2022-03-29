from django.contrib import admin
from Licenta.models import *

# Register your models here.
admin.site.register(Location)
admin.site.register(CustomUser)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(UserLikePost)
admin.site.register(UserFollow)
admin.site.register(VisitedLocations)
