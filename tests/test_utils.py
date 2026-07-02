"""Unit tests for utils"""
import os
import tempfile

import pytest

from inkflow.utils import (
    archive_posts,
    convert_to_raw_date,
    date_suffix,
    estimate_reading_time,
    generate_slug,
    get_file_index,
    write_to_file
)

class TestGenerateSlug:
    def test_simple_title(self) -> None:
        assert generate_slug("Hello World") == "hello-world"

    def test_special_characters(self) -> None:
        assert(generate_slug("What's this?") == "whats-this")

    def test_mixed_case(selfs) -> None:
        assert(generate_slug("My hello WORLD") == "my-hello-world")

    def test_numbers(self) -> None:
        assert(generate_slug("Top 10 Tips") == "top-10-tips")

    def test_preserves_hyphens(self) -> None:
        assert(generate_slug("hello-world") == "hello-world")

class TestDateSuffix:
    def test_first(self) -> None:
        assert date_suffix(1) == "1st"

    def test_second(self) -> None:
        assert date_suffix(2) == "2nd"

    def test_third(self) -> None:
        assert date_suffix(3) == "3rd"

    def test_fourth(self) -> None:
        assert date_suffix(4) == "4th"

    def test_eleventh(self) -> None:
        assert date_suffix(11) == "11th"

    def test_twelfth(self) -> None:
        assert date_suffix(12) == "12th"

    def test_thirteenth(self) -> None:
        assert date_suffix(13) == "13th"

    def test_twenty_first(self) -> None:
        assert date_suffix(21) == "21st"

    def test_thirty_first(self) -> None:
        assert date_suffix(31) == "31st"

class TestGetFileIndex:
    def test_normal_path(self) -> None:
        assert get_file_index("content/writings/01_2024_01_01_test.md") == 1

    def test_large_index(self) -> None:
        assert get_file_index("content/til/42_2024_06_15_something.md") == 42

    def test_invalid_path_raises(self) -> None:
        with pytest.raises(ValueError, match="Cannot extract file index"):
            get_file_index("some/random/path.md")


class TestConvertToRawDate:
    def test_human_date(self) -> None:
        assert convert_to_raw_date("January 1st, 2024") == "2024-01-01"

    def test_another_date(self) -> None:
        assert convert_to_raw_date("March 15, 2023") == "2023-03-15"


class TestEstimateReadingTime:
    def test_short_content(self) -> None:
        result = estimate_reading_time("<p>Short.</p>")
        assert result == "1 minute read"

    def test_long_content(self) -> None:
        long_text = "<p>" + " ".join(["word"] * 1500) + "</p>"
        result = estimate_reading_time(long_text)
        assert "minutes read" in result


class TestArchivePosts:
    def test_groups_by_year(self) -> None:
        posts = [
            {"date_raw": "2024-01-15", "title": "A"},
            {"date_raw": "2024-06-01", "title": "B"},
            {"date_raw": "2023-03-10", "title": "C"},
        ]
        result = archive_posts(posts)
        assert len(result) == 2
        # First group should be 2024 (most recent)
        assert all(p["date_raw"].startswith("2024") for p in result[0])
        assert all(p["date_raw"].startswith("2023") for p in result[1])


class TestWriteToFile:
    def test_writes_content(self) -> None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp:
            tmp_path = tmp.name

        try:
            write_to_file(tmp_path, b"<html>test</html>")
            with open(tmp_path, "rb") as f:
                assert f.read() == b"<html>test</html>"
        finally:
            os.unlink(tmp_path)