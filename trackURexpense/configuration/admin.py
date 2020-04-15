from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):
    site_header = 'trackURexpense'


admin_site = MyAdminSite(name='home')
