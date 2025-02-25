# 모듈 불러오기
from flask import request  # http 요청 데이터를 처리하기 위한 모듈
from flask.views import MethodView  # 클래스 기반 뷰를 사용하기 위한 모듈
from flask_smorest import Blueprint, abort  # api를 구조화하고 오류 처리를 위한 모듈
from schemas import BookSchema  # 데이터 유효성 검사를 위한 스키마 모듈

# 책 데이터를 저장할 빈 리스트를 만듦 (임시 db 역할)
books = []


# flaks-smorest의 Blueprint 생성 (Blueprint는 api를 그룹화하고 구조화하는데 사용)
# 여기서는 "books"로 api를 정의
book_blp = Blueprint("books", __name__, description="Book management API")
# description은 api가 무엇을 하는지 설명하기 위해 작성 (자동으로 api 문서를 만듦)


# "/books" 경로에 대한 클래스 정의
# 책 목록을 보여주거나 새 책을 추가하는 역할을 함
@book_blp.route("/books")
class BookList(MethodView):
    # GET
    @book_blp.response(200, BookSchema(many=True))  # 성공하면 책 목록을 반환
    def get(self):
        # 책 목록을 보여줌
        return books  # 저장된 책 목록을 반환

    # POST
    @book_blp.arguments(BookSchema)  # 새 책 데이터 검사
    @book_blp.response(201, BookSchema)  # 성공하면 새 책을 반환
    def post(self, new_data):
        # 새 책을 추가함
        books.append(new_data)  # 새 책을 리스트에 추가
        return new_data, 201  # 추가된 책과 성공 메시지를 반환 (상태 코드 201 사용)


# "/books/<int:index>" 경로에 대한 클래스 정의
# 특정 책을 보여주거나 수정, 삭제하는 역할을 함
@book_blp.route("/books/<int:index>")
class Book(MethodView):
    # GET
    @book_blp.response(200, BookSchema)  # 성공하면 책을 반환
    def get(self, index):
        # 특정 책을 보여줌
        if index < 0 or index >= len(books):  # 책이 없으면 오류를 반환
            abort(404, message="책을 찾을 수 없습니다.")
        return books[index]  # 특정 책을 반환

    # PUT
    @book_blp.arguments(BookSchema)  # 수정할 책 데이터를 검사함
    @book_blp.response(200, BookSchema)  # 성공하면 수정된 책을 반환
    def put(self, update_data, index):
        # 특정 책을 수정
        if index < 0 or index >= len(books):  # 책이 없으면 오류를 반환
            abort(404, message="책을 찾을 수 없습니다.")
        books[index].update(update_data)  # 책을 업데이트
        return books[index]  # 수정된 책을 반환

    # DELETE
    @book_blp.response(204)  # 성공하면 내용 없음을 반환
    def delete(self, index):
        # 특정 책을 삭제
        if index < 0 or index >= len(books):  # 책이 없으면 오류를 반환
            abort(404, message="책을 찾을 수 없습니다.")
        books.pop(index)  # 책을 삭제
        return ""  # 삭제 후 아무 내용도 반환하지않음