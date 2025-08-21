from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Faqat obyekt egasi (Barber.user) yoki adminlarga ruxsat beradi.
    """
    def has_object_permission(self, request, view, obj):
        # Adminlar to'liq ruxsatga ega
        if request.user.is_staff or request.user.is_superuser:
            return True
        # Obyekt egasi
        return hasattr(obj, 'user') and obj.user == request.user or request.user.is_staff

class IsBarberOrAdmin(permissions.BasePermission):
    """
    Faqat barber profili mavjud bo'lgan foydalanuvchi yoki adminlarga ruxsat beradi.
    """
    def has_permission(self, request, view):
        # Adminlarga ruxsat
        if request.user.is_staff or request.user.is_superuser:
            return True
        # Barber profili borligini tekshirish
        return request.user.is_authenticated and hasattr(request.user, 'barber_profile')