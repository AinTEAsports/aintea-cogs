import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def get_ascii(site_url : str) -> str :
    """Function to get ASCII art from a link

    Args:
        siteURL (str): the link where the function will take
                        the ASCII art

    Returns:
        str: the ASCII art the program got from the website
    """

    # Setting headless mode
    driver_options = webdriver.FirefoxOptions()
    driver_options.headless = True
    
    driver = webdriver.Firefox(options=driver_options)
    driver.get(site_url)
    
    # Getting the ASCII art
    ascii_art = driver.find_element_by_id("taag_output_text")

    # If no ASCII art has been got, the program will return an empty
    # string
    if not ascii_art:
        return ""
        
    # Returns ASCII art without HTML balises
    return ascii_art.text


def get_font_list() -> str :
    response = requests.get("https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something", headers={"User-Agent" : "XY"})
    soup = BeautifulSoup(response.text, 'lxml')

    font_list = soup.findAll(name='optgroup')
    fontStr = ""
    
    for font in font_list:
        fontStr += font.text
    
    return fontStr


if __name__ == "__main__":
    ascii_art = get_ascii("https://patorjk.com/software/taag/#p=display&f=Big&t=PyScii")
    print(ascii_art)
    print(get_font_list())
