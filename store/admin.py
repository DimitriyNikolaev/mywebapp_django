from django.contrib import admin
from store.models import Good,Group

class GoodAdmin(admin.ModelAdmin):
    fields = ['good_name','good_code','good_article',
              'good_size','good_brand','good_country',
              'good_description','good_price','good_group',
              'good_image']

admin.site.register(Good,GoodAdmin)
admin.site.register(Group)