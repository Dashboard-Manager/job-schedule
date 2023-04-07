from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(
        self,
        email,
        first_name,
        last_name,
        birth_date,
        password,
        **extra_fields,
    ):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        if not birth_date:
            raise ValueError("Date must be set in format YYYY-MM-DD")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            **extra_fields,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        email,
        first_name,
        last_name,
        birth_date,
        password,
        **extra_fields,
    ):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_chief", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Staff must be true")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be true")
        if extra_fields.get("is_chief") is not True:
            raise ValueError("Chief must be true")
        return self.create_user(
            email, first_name, last_name, birth_date, password, **extra_fields
        )
