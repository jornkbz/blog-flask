from flask import Blueprint, render_template, request, jsonify
from .models import User, Post
import psutil
import time

bp = Blueprint('home', __name__ )

# Guardamos el momento exacto en que arranca la app para calcular el Uptime
BOOT_TIME = time.time()

def get_user(id):
    # Nota: Usamos get() en lugar de get_or_404 para evitar errores si un usuario se borra
    user = User.query.get(id)
    return user

def search_posts(query):
    posts = Post.query.filter(Post.title.ilike(f'%{query}%')).all()
    return posts

@bp.route('/', methods=['GET', 'POST'])
def index():
    posts = Post.query.all()
    if request.method == 'POST':
        query = request.form.get('search')
        posts = search_posts(query)
        value = 'hidden'
        return render_template('index.html', posts = posts, get_user = get_user, value=value)
    return render_template('index.html', posts = posts, get_user = get_user)

@bp.route('/blog/<url>')
def blog(url):
    post = Post.query.filter_by(url = url).first()
    return render_template('blog.html', post=post, get_user = get_user)

# --- NUEVA RUTA API PARA EL SIDEBAR (ESTADÍSTICAS) ---
@bp.route('/api/stats')
def server_stats():
    """
    Devuelve JSON con CPU, RAM y Uptime para el sidebar
    """
    try:
        # 1. CPU
        cpu_percent = psutil.cpu_percent(interval=None)
        
        # 2. RAM
        memory = psutil.virtual_memory()
        mem_percent = memory.percent
        mem_used_gb = round(memory.used / (1024 ** 3), 1) # Convertir a GB
        
        # 3. Uptime
        uptime_seconds = time.time() - BOOT_TIME
        uptime_days = int(uptime_seconds // (24 * 3600))
        
        return jsonify({
            'cpu': cpu_percent,
            'mem_pct': mem_percent,
            'mem_gb': mem_used_gb,
            'uptime_days': uptime_days
        })
    except Exception as e:
        # En caso de error, devolvemos valores a cero para no romper el JS
        return jsonify({
            'cpu': 0,
            'mem_pct': 0,
            'mem_gb': 0,
            'uptime_days': 0
        })