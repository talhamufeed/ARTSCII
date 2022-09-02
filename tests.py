import argparse
from project import (
    get_args,
    image_to_html,
    image_to_terminal,
    link_to_html,
    link_to_terminal,
)
import pytest
import argparse

# tests for functions in project.py
def main():
    test_get_args()


def test_get_args():
    # test the arguments given in CLI
    assert get_args(
        ["--file", "image.jpg", "--columns", "200", "--mode", "h"]
    ) == argparse.Namespace(
        file="image.jpg", link=None, columns=200, mode="h", output="output.html"
    )
    # check if raises Error on no args passed
    with pytest.raises(SystemExit):
        get_args(["--file"])


def test_image_to_html():
    # check if image_to_html returns a type str containing html
    assert type(image_to_html("image.jpg", 200)) == str
    # check if the html file contains come html code
    assert "color" in image_to_html("image.jpg", 200)
    assert "span" in image_to_html("image.jpg", 200)
    # check that system exits upon invalid files
    with pytest.raises(SystemExit):
        image_to_html("unknownfile.jpg", 124)
        image_to_html("haha.html", 200)


def test_image_to_terminal():
    # check if image_to_terminal returns a type str
    assert type(image_to_terminal("image.jpg", 200)) == str
    # check if the the return of image_to_terminal has ASCII characters in it
    assert "*" in image_to_terminal("image.jpg", 200)
    assert "$" in image_to_terminal("image.jpg", 200)
    # check that system exits upon invalid files
    with pytest.raises(SystemExit):
        image_to_terminal("unknownfile.jpg", 124)
        image_to_terminal("unknown.html", 200)


def test_link_to_html():
    # check if link_to_html returns a type str containing html
    link = "https://cdn.britannica.com/89/149189-050-68D7613E/Bengal-tiger.jpg"
    assert type(link_to_html(link, 200)) == str
    # check if the html file contains come html code
    assert "color" in link_to_html(link, 200)
    assert "span" in link_to_html(link, 200)
    # check that system exits upon invalid urls or no internet connection
    with pytest.raises(SystemExit):
        link_to_html("www.google.com", 124)
        link_to_html("nourl", 200)


def test_link_to_termianl():
    # check if link_to_terminal returns a type str containing html
    link = "https://cdn.britannica.com/89/149189-050-68D7613E/Bengal-tiger.jpg"
    assert type(link_to_terminal(link, 200)) == str
    # check if the terminal output  contains some ASCII Chars
    assert "$" in link_to_terminal(link, 200)
    assert "%" in link_to_terminal(link, 200)
    # check that system exits upon invalid urls or no internet connection
    with pytest.raises(SystemExit):
        link_to_terminal("www.google.com", 124)
        link_to_terminal("nourl", 200)


if __name__ == "__main__":
    main()
