from django.shortcuts import render

from .models import Noticia, Menu, SubMenu, Slider, Document, Pagina


# Create your views here.
def inicio(request):
    menus = Menu.objects.filter().order_by('id')
    submenus = SubMenu.objects.filter().order_by('id')
    sliders = Slider.objects.filter().order_by('id')
    noticias = Noticia.objects.filter(age__contains='2024').order_by('-id')[:3]
    noticias2 = Noticia.objects.filter(orden='2').order_by('-id')[:4]
    return render(request, 'index.html', {'menus': menus,'submenus': submenus,'sliders': sliders,'noticias2': noticias2,'noticias': noticias})
def noticias(request):
    menus = Menu.objects.filter().order_by('id')
    submenus = SubMenu.objects.filter().order_by('id')
    sliders = Slider.objects.filter().order_by('id')
    noticias = Noticia.objects.filter().order_by('id')
    noticias2023 = Noticia.objects.filter(age__contains='2023').order_by('age')

    noticias2022 = Noticia.objects.filter(age__contains='2022').order_by('id')
    noticias2021 = Noticia.objects.filter(age__contains='2021').order_by('id')
    noticias2020 = Noticia.objects.filter(age__contains='2020').order_by('id')
    noticias2019 = Noticia.objects.filter(age__contains='2019').order_by('id')
    noticias2018 = Noticia.objects.filter(age__contains='2018').order_by('id')
    noticias2017 = Noticia.objects.filter(age__contains='2017').order_by('id')
    noticia2023 = Document.objects.filter(description='2023').order_by('id')
    noticia2022 = Document.objects.filter(description='2022').order_by('id')
    noticia2021 = Document.objects.filter(description='2021').order_by('id')
    noticia2020 = Document.objects.filter(description='2020').order_by('id')
    noticia2019 = Document.objects.filter(description='2019').order_by('id')
    noticia2018 = Document.objects.filter(description='2018').order_by('id')
    noticia2017 = Document.objects.filter(description='2017').order_by('id')

    return render(request, 'noticias.html', {'noticias2023':noticias2023,'menus': menus,'submenus': submenus,'sliders': sliders,'noticias': noticias,'noticia2023':noticia2023,'noticia2022':noticia2022,'noticia2021':noticia2021,'noticia2020':noticia2020,'noticia2019':noticia2019,'noticia2018':noticia2018,'noticia2017':noticia2017})

def noticia(request,slug):
    noticias = Noticia.objects.filter(slug=slug)
    noticia = Noticia.objects.get(slug=slug)

    menus = Menu.objects.filter().order_by('id')
    submenus = SubMenu.objects.filter().order_by('id')
    return render(request, 'noticia.html', {'noticias': noticias, 'menus': menus,'submenus': submenus,})
def pagina(request,slug):
    paginas = Pagina.objects.filter(slug=slug)
    pagina = Pagina.objects.get(slug=slug)
    documentos = Document.objects.filter(pagina=pagina)
    menus = Menu.objects.filter().order_by('id')
    submenus = SubMenu.objects.filter().order_by('id')
    return render(request, 'pagina.html', {'paginas': paginas, 'documentos':documentos, 'menus': menus,'submenus': submenus,})
