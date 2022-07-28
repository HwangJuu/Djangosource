from django import template
import markdown
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg


# 마크다운 적용 필터
@register.filter
def mark(value):
    # markdown 확장 도구 적용
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))


# 템플릿 필터
# 템플릿 태그에서 | 문자 뒤에 사용하는 필터
# ex : {{form.subject.value | default_if_none:''}}


# 게시물 번호
# 일련번호 =  전체 게시물 개수 - 시작 인덱스 - 현재 인덱스 + 1
# 페이지당 게시물을 10건씩 보여줄 때
# 1 page 인 경우는 시작 인덱스 1,
# 2 page 인 경우는 시작 인덱스 11
# 현재 인덱스 : 0 ~ 9반복
