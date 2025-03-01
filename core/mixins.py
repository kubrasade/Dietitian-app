class BaseMixin:
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user, is_deleted=False)