from inkflow.pagination import calculate_page_count, _page_url, generate_pagination_links


class TestCalculatePageCount:
    def test_exact_division(self) -> None:
        assert(calculate_page_count(16, 8)) == 2

    def test_remainder_rounds_up(self) -> None:
        assert(calculate_page_count(17, 8) == 3)

    def test_one_extra_post(self) -> None:
        assert(calculate_page_count(9, 8) == 2)

    def test_fewer_than_page_size(self) -> None:
        assert(calculate_page_count(3, 8) == 1)

    def test_zero_posts(self) -> None:
        assert(calculate_page_count(0, 8) == 0)

    def test_zero_per_page(self) -> None:
        assert(calculate_page_count(10, 0) == 1)

class TestPageUrl:
    def test_page_one_returns_base(self) -> None:
        assert(_page_url("/writings", 1) == "/writings")

    def test_page_two_returns_page_path(self) -> None:
        assert(_page_url("/writings", 2) == "/writings/pages/2")

    def test_page_zero_returns_base(self) -> None:
        assert(_page_url("/writings", 0) == "/writings")

class TestGeneratePaginationLinks:
    def test_single_page(self) -> None:
        links = generate_pagination_links("/pages/", 1, 1)
        assert len(links) == 1
        assert links[0]["page"] == 1

    def test_two_pages(self) -> None:
        links = generate_pagination_links("/pages/", 1, 2)
        assert any(link["page"] == 1 for link in links)
        assert any(link["page"] == 2 for link in links)

    def test_many_pages_has_dots(self) -> None:
        links = generate_pagination_links("/pages/", 1, 10)
        has_dots = any(link["has_dots"] for link in links)
        assert has_dots

    def test_first_page_url_is_base_directory(self) -> None:
        links = generate_pagination_links("/writings/pages/", 1, 5)
        first = next(link for link in links if link["page"] == 1)
        assert first["url"] == "/writings/"