def get_name_meaning(request):
    """이름 의미 기능을 제공합니다."""

    # 이름 가져오기
    name = request.GET.get("name")

    # 이름 의미 가져오기
    name_meaning = name_dao.get_name_meaning(name)

    # 이름 의미 반환
    return {
        "name_meaning": name_meaning
    }
