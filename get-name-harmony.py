def get_name_harmony(request):
    """이름 조화 기능을 제공합니다."""

    # 이름1 가져오기
    name1 = request.GET.get("name1")

    # 이름2 가져오기
    name2 = request.GET.get("name2")

    # 이름 조화 점수 가져오기
    name_harmony_score = name_dao.get_name_harmony_score(name1, name2)

    # 이름 조화 점수 반환
    return {
        "name_harmony_score": name_harmony_score
    }
