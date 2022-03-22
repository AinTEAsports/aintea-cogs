import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def getASCII(siteURL : str):
    """Function to get ASCII art from a link

    Args:
        siteURL (str): the link where the function will take
                        the ASCII art

    Returns:
        str: the ASCII art the program got from the website
    """

    # Setting headless mode
    driverOptions = webdriver.FirefoxOptions()
    driverOptions.headless = True
    
    driver = webdriver.Firefox(options=driverOptions)
    driver.get(siteURL)
    
    # Getting the ASCII art
    asciiArt = driver.find_element("taag_output_text")

    # If no ASCII art has been got, the program will return an empty
    # string
    if not asciiArt:
        return ""
        
    # Returns ASCII art without HTML balises
    return asciiArt.text


def getFontList() -> str():
    response = requests.get("https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something", headers={"User-Agent" : "XY"})
    soup = BeautifulSoup(response.text, 'lxml')

    fontList = soup.findAll(name='optgroup')
    fontStr = ""
    
    for font in fontList:
        fontStr += font.text
    
    return fontStr


if __name__ == "__main__":
    asciiArt = getASCII("https://patorjk.com/software/taag/#p=display&f=Big&t=PyScii")
    print(asciiArt)
    print(getFontList())
