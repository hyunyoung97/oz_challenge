# Flask 웹을 만들기 위해 Flask 클래스를 가져옴
from flask import Flask
# flask_smorest에서 Api 클래스를 가져옴
from flask_smorest import Api
# book_blp = 블루프린트 / api.py 파일에서 가져옴
from api import book_blp

# Flask 애플리케이션 생성
app = Flask(__name__)

# OpenAPI 관련 설정
app.config["API_TITLE"] = "Book Management API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

# book_blp를 API에 등록
# 책 관련 url들을 자동으로 연결
api.register_blueprint(book_blp)

if __name__ == '__main__':
    app.run(debug=True)
