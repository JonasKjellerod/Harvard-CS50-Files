import pytest
from unittest.mock import patch
import project

# Test clean_title
def test_clean_title():
    # Test cases for clean_title
    assert project.clean_title("Breaking News - Source") == "Breaking News"
    assert project.clean_title("Just Another News Title") == "Just Another News Title"
    assert project.clean_title("Complex Title - With Multiple - Hyphens") == "Complex Title - With Multiple"
    assert project.clean_title("") == ""  # Empty string case
    assert project.clean_title("Normal Title") == "Normal Title"  # Title without hyphen

# Test choose_category using mock input
def test_choose_category():
    with patch("builtins.input", side_effect=["1"]):
        assert project.choose_category() == "general"
    with patch("builtins.input", side_effect=["2"]):
        assert project.choose_category() == "business"
    with patch("builtins.input", side_effect=["7"]):  # Invalid input
        assert project.choose_category() == "general"  # Default fallback

# Test get_news with mocked API response
def test_get_news():
    mock_response = {
        "status": "ok",
        "totalResults": 1,
        "articles": [
            {
                "source": {"name": "Mock Source"},
                "title": "Mock Title - Source",
                "description": "Mock Description",
                "url": "http://mock.url",
            }
        ],
    }

    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        articles = project.get_news(category="general", country="us")

        assert len(articles) == 1
        assert articles[0]["title"] == "Mock Title - Source"
        assert articles[0]["description"] == "Mock Description"
        assert articles[0]["source"]["name"] == "Mock Source"
        assert articles[0]["url"] == "http://mock.url"

if __name__ == "__main__":
    pytest.main()
