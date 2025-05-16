from django.contrib.auth.models import AbstractUser
from django.db import models


# مدل کاربران
class User(AbstractUser):
    pass


# مدل لیست‌های مزایده
class Listing(models.Model):
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('fashion', 'Fashion'),
        ('watches', 'Watches'),
        ('accessories', 'Accessories'),
        ('home', 'Home & Living'),
        ('sports', 'Sports & Outdoors'),
    ]

    title = models.CharField(max_length=100, verbose_name="Auction Title")  # عنوان مزایده
    description = models.TextField(verbose_name="Description")  # توضیحات مزایده
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Starting Bid")  # قیمت اولیه
    image_url = models.URLField(blank=True, null=True, verbose_name="Image URL")  # تصویر محصول (اختیاری)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True, null=True, verbose_name="Category")  # دسته‌بندی
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")  # تاریخ ایجاد
    active = models.BooleanField(default=True, verbose_name="Is Active")  # وضعیت فعال بودن مزایده
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings", verbose_name="Owner")  # صاحب مزایده
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="won_auctions")  # 👈 ثبت برنده‌ی مزایده

    class Meta:
        ordering = ['-created_at']  # مرتب‌سازی بر اساس جدیدترین لیست‌ها

    def __str__(self):
        return f"{self.title} ({self.category})"


# مدل پیشنهادات (Bids)
class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids", verbose_name="Auction")  # ارتباط با لیست مزایده
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Bidder")  # کاربری که پیشنهاد داده است
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Bid Amount")  # مقدار پیشنهاد
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Bid Time")  # زمان ثبت پیشنهاد

    class Meta:
        ordering = ['-timestamp']  # مرتب‌سازی بر اساس جدیدترین پیشنهادات

    def __str__(self):
        return f"{self.user} bid ${self.amount} on {self.listing}"


# مدل نظرات (Comments)
class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments", verbose_name="Auction")  # ارتباط با لیست مزایده
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Commenter")  # کاربری که نظر داده است
    content = models.TextField(verbose_name="Comment Text")  # متن نظر
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Comment Time")  # زمان ثبت نظر

    class Meta:
        ordering = ['-timestamp']  # مرتب‌سازی بر اساس جدیدترین نظرات

    def __str__(self):
        return f"Comment by {self.user} on {self.listing}"


# مدل لیست علاقه‌مندی‌ها (Watchlist)
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")  # کاربر صاحب لیست علاقه‌مندی‌ها
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, verbose_name="Auction")  # لیست مزایده‌ای که ذخیره شده است

    class Meta:
        unique_together = ('user', 'listing')  # جلوگیری از ذخیره چندباره یک لیست در علاقه‌مندی‌ها

    def __str__(self):
        return f"{self.user} is watching {self.listing}"
