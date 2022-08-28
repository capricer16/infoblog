from accounts.models import User

def has_admin_role(user):
    return user.role == User.ADMIN