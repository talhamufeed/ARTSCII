import argparse
import sys
import ascii_magic
from PIL import UnidentifiedImageError

# this function takes arguments from user
def get_args(argv: list = None) -> argparse.Namespace:
    """This function takes the arguments from the terminal. Run --help to view all possible commands"""
    # description
    parser = argparse.ArgumentParser(
        description="This program will take an image and convert it to ASCII, use --help to view all possible commands"
    )
    # add mutually exclusive argument for location of image or url
    link_or_file = parser.add_mutually_exclusive_group(required=True)
    link_or_file.add_argument(
        "-f", "--file", help="convert an image from file", type=str
    )
    link_or_file.add_argument(
        "-l", "--link", help="convert an image from web", type=str
    )
    # add argument for columns(optional)
    parser.add_argument(
        "-c",
        "--columns",
        help="Enter number of columns(more columns more wide)",
        required=False,
        default=120,
        type=int,
    )
    # add argument for printing to terminal or html file
    parser.add_argument(
        "-m",
        "--mode",
        help="Select mode between terminal(t) or html(h)",
        required=False,
        default="t",
        type=str,
        choices=["t", "h"],
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Rename output file",
        default="output.html",
        required=False,
    )
    args = parser.parse_args(argv)
    # return args to use in main()
    return args


# this function will return an html page with the ascii image
def image_to_html(location: str, cols: int) -> str:
    """This takes the location of the file and columns provided and converts it tO ASCII art in form of HTML script"""
    # handle exceptions
    try:
        ascii_converted = ascii_magic.from_image_file(
            location, columns=cols, mode=ascii_magic.Modes.HTML
        )
    except (FileNotFoundError, UnidentifiedImageError):
        sys.exit(
            """
        ----------------------------------------------------------------------
        The file does not exist on the specified location. Kindly double check.
        ----------------------------------------------------------------------
        """
        )
    else:
        return ascii_converted


def image_to_terminal(location: str, cols: int) -> str:
    """This takes the location of the file and columns provided and converts it tO ASCII art in form of Terminal Output"""
    # handle exceptions
    try:
        ascii_converted = ascii_magic.from_image_file(
            location, columns=cols, mode=ascii_magic.Modes.TERMINAL
        )
    except (FileNotFoundError, UnidentifiedImageError):
        sys.exit(
            """
        ----------------------------------------------------------------------
        The file does not exist on the specified location. Kindly double check.
        ----------------------------------------------------------------------
        """
        )
    else:
        return ascii_converted


def link_to_html(url: str, cols: int) -> str:
    """This takes the url of the image and columns provided and converts it tO ASCII art in form of HTML script"""
    # handle exceptions
    try:
        ascii_converted = ascii_magic.from_url(
            url, columns=cols, mode=ascii_magic.Modes.HTML
        )
    except (OSError, ValueError):
        sys.exit(
            f"""
        -------------------------------------------------------
        Could not load the image, Double check the url and your internet connection
        -------------------------------------------------------
        """
        )
    else:
        return ascii_converted


def link_to_terminal(url: str, cols: int) -> str:
    """This takes the url of the image and columns provided and converts it tO ASCII art in form of Terminal output"""
    # handle exceptions
    try:
        ascii_converted = ascii_magic.from_url(
            url, columns=cols, mode=ascii_magic.Modes.TERMINAL
        )
    except (OSError, ValueError):
        sys.exit(
            f"""
        -------------------------------------------------------
        Could not load the image, double check the url and internet connection
        -------------------------------------------------------
        """
        )
    else:
        return ascii_converted


# Title: ARTSCII
# import libraries
# then add main function which will be executed when the program starts and will call other functions according to argparse args
def main():
    """
    This function is the main function that calls other functions
    """
    # get args from get_args function and use to them to call other functions
    location = get_args().file
    url = get_args().link
    columns = get_args().columns
    mode = get_args().mode
    output_name = get_args().output
    # rule out exceptions and limit the number of columns to prevent program from crashing
    if output_name.endswith("html"):
        pass
    else:
        sys.exit(
            """
        ----------------------------------------------------
        Please enter a valid html file name ending in .html
        ----------------------------------------------------
        """
        )
    # reset columns to 1500 if it's more than 1500 to avoid crashes
    if columns > 1500 and mode == "h":
        columns = 1500
    elif columns > 180 and mode == "t":
        columns = 180
    else:
        pass
    # if file  is selected and html mode is selected
    if url == None and mode == "h":
        # take the provided artwork from the image_to_html() and convert it to html
        ascii_magic.to_html_file(output_name, (image_to_html(location, columns)))
    # if file mode is selected and terminal mode is selected
    elif url == None and mode == "t":
        ascii_magic.to_terminal((image_to_terminal(location, columns)))
    # if url is selected and html mode is selected
    elif location == None and mode == "h":
        ascii_magic.to_html_file(output_name, (link_to_html(url, columns)))
    # else the url and terminal mode remains
    else:
        ascii_magic.to_terminal(link_to_terminal(url, columns))


# this will return ascii to terminal
if __name__ == "__main__":
    main()
