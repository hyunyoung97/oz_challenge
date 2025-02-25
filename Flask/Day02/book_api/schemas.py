# marshmallow에서 스키마, 필드 가져오기
from marshmallow import Schema, fields

# 스키마 만들기
# 책 정보를 어떻게 저장하고 확인할지 미리 약속
class BookSchema(Schema):
    # id는 숫자로 저장, 가져올 때만(dump_only=True) 사용
    # 책 고유번호 / 직접 입력x 자동으로 생성
    id = fields.Int(dump_only=True)
    
    # title은 문자열로 저장, 꼭 있어야하는 필수 필드(required=True)
    # 책 제목을 나타내는 필드
    title = fields.Str(required=True) 
    
    # author도 문자열로 저장, 꼭 있어야하는 필수 필드(required=True)
    # 저자 이름을 나타내는 필드
    author = fields.Str(required=True) 
