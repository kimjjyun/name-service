def search_name(request):
    """이름 검색 기능을 제공합니다."""

    # 검색어 가져오기
    keyword = request.GET.get("keyword")

    # 이름 목록 가져오기
    name_list = name_dao.search_name(keyword)

    # 이름 목록 반환
    return {
        "name_list": name_list
    }
