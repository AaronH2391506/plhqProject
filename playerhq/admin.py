from django.contrib import admin

from playerhq.models import Games,Reviews,Comments,Categories

class comments(admin.ModelAdmin):
    list_display = ('GameName','CommentName','Comments')
    
class game(admin.ModelAdmin):
    list_display = ('GameName','GameCategory')
    
class review(admin.ModelAdmin):
    list_display = ('GameName','ReviewerName')

class categories(admin.ModelAdmin):
    list_display = ('catName',)

admin.site.register(Reviews,review)
admin.site.register(Games, game)
admin.site.register(Comments,comments )
admin.site.register(Categories,categories)
