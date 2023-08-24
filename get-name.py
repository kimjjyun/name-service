def get_name(request):
    """이름 추천 기능을 제공합니다."""

    # 사용자 정보 가져오기
    user_info = request.json

    # 이름 추천 알고리즘 실행
    name_list = name_recommendation(user_info)

    # 이름 목록 반환
    return {
        "name_list": name_list
    }
