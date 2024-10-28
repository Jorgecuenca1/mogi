from .models import Pagina, Noticia, SubMenu, Menu, Document, Slider, Contract, Documento
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
class DocumentoInline(admin.TabularInline):
    model = Documento
    extra = 1
class DocumentInline(admin.TabularInline):
    model = Document
class SubMenuInline(admin.TabularInline):
    model = SubMenu

class ContractAdmin(admin.ModelAdmin):
    list_display = ("year", "consecutive", "contract_number", "entity")
    inlines = [DocumentoInline]
admin.site.register(Contract, ContractAdmin)


class SliderAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('id', 'name',)
    list_filter = ('name',)
class NoticiaAdmin(ImportExportModelAdmin):
    list_display = ('id', 'titulo',)
    search_fields = ('id', 'titulo',)
    list_filter = ('titulo',)
class DocumentAdmin(ImportExportModelAdmin):
    list_display = ('id', 'titulo',)
    search_fields = ('id', 'titulo',)
    list_filter = ('titulo',)
class SubMenuAdmin(ImportExportModelAdmin):
    list_display = ('id', 'titulo',)
    search_fields = ('id', 'titulo',)
    list_filter = ('titulo',)
class MenuAdmin(ImportExportModelAdmin):
    list_display = ('id', 'titulo',)
    search_fields = ('id', 'titulo',)
    list_filter = ('titulo',)
    inlines = [SubMenuInline]
class PaginaAdmin(ImportExportModelAdmin):
    model = Pagina
    inlines = [DocumentInline]

admin.site.register(Pagina, PaginaAdmin)

admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(SubMenu, SubMenuAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Document, DocumentAdmin)

