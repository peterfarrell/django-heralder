def register_notification(*models, **kwargs):
    """
    Registers the given notification with Django Herold
    :param views:
    :param kwargs:
    :return:
    """
    from django.contrib.admin import ModelAdmin
    from django.contrib.admin.sites import site, AdminSite

    def _notification_wrapper(admin_class):
        admin_site = kwargs.pop('site', site)

        if not isinstance(admin_site, AdminSite):
            raise ValueError('site must subclass AdminSite')

        if not issubclass(admin_class, ModelAdmin):
            raise ValueError('Wrapped class must subclass ModelAdmin.')

        admin_site.register(models, admin_class=admin_class)

        return admin_class
    return _notification_wrapper