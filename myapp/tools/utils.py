# HttpRequest 사용
# META - content_legnth, content_type, http_user-agent ...(헤더에 따라 붙는 정보)을 불러올수 있음

# 정형화된 코드


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[-1].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")  # 사용자 정보를 가지고 올 수 있음

    return ip
