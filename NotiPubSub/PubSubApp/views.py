from django.shortcuts import render

from .forms import CategoriaForm, NoticiaForm

class Noticia():
    def __init__(self, id,  titulo, cuerpo, id_categoria):
        self.id = id
        self.titulo = titulo
        self.cuerpo = cuerpo
        self.id_categoria = id_categoria
    
    def aJson(self):
        return {
            'titulo' : self.titulo,
            'cuerpo' : self.cuerpo,
            'id': self.id,
            'tags': ['tag1', 'tag2', 'tag3', 'tag4', 'tag5', 'tag6', 'tag7']
        }

def categoria_create(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()

    contexto = {
        'form': form
    }
    return render(request, 'categoria_form.html', contexto)

def noticia_create(request):
    form = NoticiaForm(request.POST or None)
    if form.is_valid():
        form.save()

    contexto = {
        'form': form
    }
    return render(request, 'noticia_form.html', contexto)

def iniciarSesion(request):
    return render(request, 'login.html')

def noticias(request):

    titulo = "Noticia bien mamalona!"
    cuerpo = """Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
                Repellendus, earum quo esse aliquid accusamus natus modi 
                ex odit cupiditate iure neque labore debitis eos! Possimus 
                sit quos ratione corporis aliquam.
                """
    noticia1 = Noticia(1, "Noticia numero 1", cuerpo, 1)
    noticia2 = Noticia(2, "Noticia numero 2", cuerpo, 1)
    noticia3 = Noticia(3, "Noticia numero 3", cuerpo, 1)
    noticias = [noticia1, noticia2, noticia3]

    #doc_arch = open("./NoticiasPubSub/templates/noticia.html")

    #plt=Template(doc_arch.read())

    # doc_arch = loader.get_template('noticia.html')

    #ctx = Context(noticia.aJson())
    #doc_arch.close()

    # documento = doc_arch.render(noticia.aJson())

    return render(request, 'noticias.html', {'noticias': noticias})
