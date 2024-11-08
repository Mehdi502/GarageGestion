from rest_framework.permissions import BasePermission

class IsAdminUserCustom(BasePermission):
    """
    Permission pour vérifier si l'utilisateur a le rôle 'admin'.
    """
    def has_permission(self, request, view):
        # Vérifie que l'utilisateur est authentifié et a le rôle 'admin'
        return request.user.is_authenticated and request.user.fonction == 'admin'
