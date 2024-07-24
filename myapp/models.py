from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify




class ProductCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    url = models.CharField(max_length=200, verbose_name="url")
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی محصولات'



class ProductInformation(models.Model):
    color = models.CharField(max_length=20,verbose_name="رنگ")
    size = models.CharField(max_length=20,verbose_name="سایز")
    def __str__(self):
        return f"({self.color}-{self.size})"

    class Meta:
        verbose_name_plural = 'مشخصات محصولات'



class ProductTag(models.Model):
    tag = models.CharField(verbose_name='تگ', max_length=20)

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'


class Product(models.Model):
    title = models.CharField(max_length=20)
    price = models.IntegerField()
    rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5),
    ], default=0, )
    short_description = models.CharField(max_length=350, null=True)
    in_active = models.BooleanField(default=False)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, null=True
    )
    product_information = models.OneToOneField(
        ProductInformation, on_delete=models.CASCADE, null=True,
        blank=True, verbose_name="اطلاعات", related_name="information"
    )
    product_tag = models.ManyToManyField(ProductTag)
    slug = models.SlugField(
        default='',
        null=False,
        db_index=True,
        # editable=False,
        blank=True,
    )

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"









# https://virgool.io/@dori-dev/django-model-relationships-x7fyucdtzhak
# روابط در جداول