from django.urls import path
from . import views

urlpatterns = [
    # صفحه اصلی - نمایش لیست‌های فعال
    path("", views.index, name="index"),
    path("listing/", views.listing_index, name="listing_index"),  # نمایش همه لیست‌های فعال

    # احراز هویت کاربران
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),

    # نمایش جزئیات یک لیست مزایده
    path("listing/<int:listing_id>/", views.listing_detail, name="listing_detail"),

    # ثبت پیشنهاد (Bid)
    path("listing/<int:listing_id>/bid/", views.place_bid, name="place_bid"),

    # ثبت نظر (Comment)
    path("listing/<int:listing_id>/comment/", views.add_comment, name="add_comment"),

    # مدیریت لیست علاقه‌مندی‌ها (Watchlist)
    path("listing/<int:listing_id>/watchlist/", views.toggle_watchlist, name="toggle_watchlist"),
    path("watchlist/", views.watchlist, name="watchlist"),

    # بستن مزایده و تعیین برنده
    path("listing/<int:listing_id>/close/", views.close_auction, name="close_auction"),

    # ایجاد لیست مزایده جدید
    path("create/", views.create_listing, name="create_listing"),

    # نمایش مزایده‌های بسته‌شده (Closed Auctions)
    path("closed/", views.closed_auctions, name="closed_auctions"),

    # صفحات جدید
    path("about/", views.about, name="about"),  # صفحه درباره ما
    path("contact/", views.contact, name="contact"),  # صفحه تماس با ما
    path("my_listings/", views.my_listings, name="my_listings"),  # لیست‌های من
    path("category/<str:category>/", views.category_listings, name="category"),
]
