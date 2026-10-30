
from flask import Flask

from admin.routes import admin_bp
from blog.routes import blog_bp

app = Flask(__name__)

# Registrar los modulos
app.register_blueprint(admin_bp)
app.register_blueprint(blog_bp)

if __name__ == '__main__':
    app.run(debug=True)
