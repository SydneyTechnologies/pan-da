from . watchable import Watchable
import re
# a custom class that holds the search results, the links, images and description
# gotten from a movie or series search
import mechanicalsoup
import mechanicalsoup.browser
# the two imports above are essentially what we would need to scrape the website
# beautiful soup known as the import bs4 will be used to navigate through the html tree
# and search for different elements and hence store or interact with them
# however mechanical soup on the other hand will be used to interact with forms within the
# web application
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
# we have to make use of selenium since we will be working with some javascript
# code on the tfpdl website
chrome_options = Options()
prefs = {"profile.managed_default_content_settings.images": 2}
# to run the selenium driver efficiently, we need to set some options
chrome_options.add_argument("--silent")
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_extension('C:\\Users\\sydne\\Desktop\\panda\\ublock.crx')
#chrome_options.add_experimental_option("prefs", prefs)
# the target url is tfpdl.is
search = "doctor strange 2022"
URL = "https://tfpdl.se/?s="+search
# the browser is a class provided by mechanical soup that would allow for requests to be
# made through python code, however it is unable to do javascript operations
browser = mechanicalsoup.StatefulBrowser()
page = browser.get(URL)
# the page is the object that contains the website result for the given search


def startSearch(search):
    URL = "https://tfpdl.se/?s="+search
    searchResultPage = browser.get(URL)
    if searchResultPage.status_code != 200:
        return False
    else:
        results = searchResultPage.soup.find_all("article")
        return ExtractSearchAsWatchable(results)


def Start():
    results = []
    print(page.url)
    if page.status_code != 200:
        print("could not find item")
    else:
        result_page = page.soup
        results = result_page.find_all("article")
        getDownloadLink(ExtractSearchAsWatchable(results)[0])


def ExtractSearchAsWatchable(Articles):
    # this is a method that is responsible for
    # creating new watchable items
    watchableList = []
    for article in Articles:
        link_tag = article.find("h2").find("a")
        print(link_tag)
        title = link_tag.contents
        link = link_tag["href"]
        image = article.find("img")["src"]
        description = article.find("br").contents
        searchResultItem = Watchable(title, link, description, image)
        watchableList.append(searchResultItem)
    return watchableList


def getDownloadLink(watchable):
    page_two = browser.get(watchable.getLink()).soup
    download_div = page_two.find("div", attrs={"class": "entry"})
    link = download_div.find(
        "a", attrs={"target": "_blank", "class": "button"})["href"]
    # at this point there is a form we need to submit
    # but the submission code requires javascript to be used
    driver = webdriver.Chrome(options=chrome_options,
                              service=Service(ChromeDriverManager().install()))
    driver.get(link)
    # we have to find the first element which is an image tag
    # with an onclick event attached to it
    wait = WebDriverWait(driver, 15)
    image_button_one = wait.until(findElement(
        By.XPATH, '//*[@id="landing"]/div[2]/center/img'))
    driver.execute_script(
        "arguments[0].scrollIntoView(true);", image_button_one)
    image_button_one.click()
    image_button_two = wait.until(findElement(
        By.XPATH, '//*[@id="generater"]/img'))
    driver.execute_script(
        "arguments[0].scrollIntoView(true);", image_button_two)
    image_button_two.click()
    image_button_three = wait.until(
        findElement(By.XPATH, '//*[@id="showlink"]'))
    driver.execute_script(
        "arguments[0].scrollIntoView(true);", image_button_three)
    image_button_three.click()
    driver.switch_to.window(driver.window_handles[1])
    # now we must check if the website has a input field
    password_field = wait.until(findElement(By.XPATH, '//*[@id="password"]'))
    password_field.send_keys("tfpdl")
    submit_button = wait.until(findElement(By.XPATH, '//*[@id="passwordBtn"]'))
    submit_button.submit()
    download_link_tag = wait.until(
        findElement(By.XPATH, '//*[@id="pre"]/a[1]'))
    driver.get(download_link_tag.get_attribute('href'))
    entry_captcha = wait.until(findElement(
        By.XPATH, '//*[@id="commonId"]/center/table/tbody/tr[2]/td[2]/input'))
    entry_captcha.send_keys(defeatCaptcha(driver))
    entry_captcha.submit()
    download_button = wait.until(findElement(
        By.XPATH, '//*[@id="downloadbtn"]'))
    regex_pattern = r"https:\/\/.*?'"
    onclick_text = download_button.get_attribute('onclick')
    download_link = re.search(
        regex_pattern, onclick_text, re.MULTILINE).group()
    print(download_link)
    watchable.updateDownloadLink(str(download_link))
    return watchable


def defeatCaptcha(driver):
    captcha_list = driver.find_elements(
        By.XPATH, '//*[@id="commonId"]/center/table/tbody/tr[2]/td[1]/div/span')
    values = []
    positions = []
    for character in captcha_list:
        value = character.text
        style = character.get_attribute("style")
        regex_syntax = r'(left.*?;)'
        position = re.search(regex_syntax, style, re.MULTILINE).group()
        position_value = str(position[6:]).replace('px;', '', 1)
        values.append(int(value))
        positions.append(int(position_value))

    return linkedListAlgo(values=values, position=positions)


def linkedListAlgo(values, position):
    new_list = []
    for i in range(4):
        new_list.append([values[i], position[i]])
    position.sort()
    result = ""
    for pos in position:
        for i in range(4):
            if new_list[i][1] == pos:
                result = result + str(new_list[i][0])
    print(result)
    return result


def findElement(by, path):
    # this is a method that helps to locate elements
    # within a html dom tree
    # it is called repeatedly until the element is found
    # however if the timeout is exceeded then the recursion stops
    return EC.element_to_be_clickable((by, path))


# Start()
# driver.quit()
