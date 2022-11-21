from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import *


admin.site.register(Institution)
admin.site.register(DataEntryOfficer)
#admin.site.register(County)
#admin.site.register(SubCounty)
#admin.site.register(Ward)

admin.site.register(SubSector)
admin.site.register(Domain)
admin.site.register(DomainElement)
admin.site.register(ElementItem)
admin.site.register(ItemCategory)
admin.site.register(ItemSpecify)
admin.site.register(UoM)
admin.site.register(Flags)
admin.site.register(KilimoData)


class CountyAdmin(ImportExportModelAdmin):
    list_display = ("id", "name","code")
    pass
admin.site.register(County, CountyAdmin)


class SubCountyAdmin(ImportExportModelAdmin):
    list_display = ("id", "name","county_id")
    pass
admin.site.register(SubCounty, SubCountyAdmin)


class WardAdmin(ImportExportModelAdmin):
    list_display = ("id", "name","county_id","subcounty_id")
    pass
admin.site.register(Ward, WardAdmin)