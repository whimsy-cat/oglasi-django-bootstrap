from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models, IntegrityError


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password, phone_number=None,
                    type=None, identification_number=None, tax_id=None, newsletter_subscribed=False, address=None, **kwargs):
        if not email:
            raise ValueError('Email je obavezan')

        if not username:
            raise ValueError('Korisničo ime je obavezno')

        if not first_name:
            raise ValueError('Unesite ime/naziv')

        if not password or len(password) < 8:
            raise ValueError('Lozinka mora biti bar 8 karaktera')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            type=int(type) if type else 0,
            identification_number=identification_number,
            tax_id=tax_id,
            newsletter_subscribed=newsletter_subscribed,
            address=address,
            **kwargs
        )

        user.set_password(password)
        user.full_clean()
        user.save(using=self.db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            first_name=first_name, last_name=last_name, username=username, email=email, password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True

        user.save(using=self.db)
        return user


class Account(AbstractBaseUser):
    USER_TYPE = (
        ("0", 'Fizičko lice'),
        ("1", 'Pravno lice'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True, default='')
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True, default='')

    type = models.CharField(max_length=25, choices=USER_TYPE, default="0")

    identification_number = models.CharField(max_length=100, null=True, blank=True, default='')
    tax_id = models.CharField(max_length=100, null=True, blank=True, default='')

    newsletter_subscribed = models.BooleanField(default=False)

    image = models.FileField(max_length=255, upload_to='users', blank=True, null=True)
    address = models.CharField(max_length=255, null=True, blank=True, default='')

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
