from django.contrib import admin

from ads.models import Ad, Comment
from users.models import User

admin.site.register(Ad)
admin.site.register(Comment)
admin.site.register(User)

