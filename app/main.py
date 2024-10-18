from flask import Flask
from database import init_app
from routes.user_routes import user_bp

app = Flask(__name__)

db = init_app(app)

app.register_blueprint(user_bp)

if __name__ == '__main__':
    print(app.url_map)
    app.run(host='0.0.0.0', port=5000)
