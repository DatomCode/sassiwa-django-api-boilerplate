from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self, email,username, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        if not username:
            raise ValueError("Username is required")

        email = self.normalize_email(email)

        user = self.model(
            email = email,
            username = username,
            **extra_fields
        )

        user.set_password(password)
        user.save(using= self._db)

        return user


    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff True")

        if extra_fields.get("is_active") is not True:
            raise ValueError("Superuser must have is_active True")

        return self.create_user(
            email = email,
            username= username,
            password= password,
            **extra_fields
        )