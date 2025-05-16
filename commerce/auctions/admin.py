from django.contrib import admin
from django.utils.html import format_html
from .models import Listing, Bid, Comment, Watchlist, User


# تنظیمات پنل مدیریت برای مدل Listing
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'starting_bid', 'category', 'owner', 'active', 'image_preview', 'created_at')
    list_filter = ('active', 'category', 'created_at')
    search_fields = ('title', 'description', 'owner__username')
    ordering = ['-created_at']
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" style="width:80px; height:80px; border-radius:5px;" />', obj.image_url)
        return "No Image"

    image_preview.short_description = "Preview"


# تنظیمات پنل مدیریت برای مدل Bid
class BidAdmin(admin.ModelAdmin):
    list_display = ('listing', 'user', 'amount', 'timestamp')
    list_filter = ('listing', 'user', 'timestamp')
    search_fields = ('listing__title', 'user__username')
    ordering = ['-timestamp']


# تنظیمات پنل مدیریت برای مدل Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ('listing', 'user', 'content', 'timestamp')
    list_filter = ('listing', 'user', 'timestamp')
    search_fields = ('listing__title', 'user__username', 'content')
    ordering = ['-timestamp']


# تنظیمات پنل مدیریت برای مدل Watchlist
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'listing')
    search_fields = ('user__username', 'listing__title')
    ordering = ['user']


# ثبت مدل‌ها در پنل مدیریت
admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(User)
