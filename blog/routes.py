
from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__)

entradas = {
    '1': 'Introduccion al desarrollo web',
    '2': 'Aprendiendo Flask con Python',
    '3': 'Uso de plantillas en Flask'
}

@blog_bp.route('/entrada/<id>')
def entrada(id):

    titulo = entradas.get(id, 'Entrada no encontrada')

    return render_template(
        'blog/entrada.html',
        titulo=titulo,
        id=id
    )
