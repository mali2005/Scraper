import  requests
from selenium import webdriver
import  time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import shutil
from webdriver_manager.chrome import ChromeDriverManager
import threading
import os
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install())


def find_links(inputs,iters):
    links = []
    word = inputs.replace(" ", "%20")
    url = 'https://www.bing.com/images/search?q={}'.format(word)
    driver.get(url)
    time.sleep(2)
    for i in range(iters):
        driver.execute_script("window.scrollTo(0, {})".format(str(i*1000)))
        elements = driver.find_elements(By.CLASS_NAME, "mimg")
        for element in elements:
            src = element.get_attribute("src")
            if src:
                if src[:4] == "http":
                    if src in links:
                        pass
                    else:
                        links.append(src)
    driver.close()
    return links


def download_images(urls, output_path, word):
    try:
        os.mkdir(output_path)
    except Exception:
        pass

    r = 0
    i = 0
    for url in urls:
        response = requests.get(url, stream=True, verify=False)
        with open('{}//{}_{}.png'.format(output_path, word, str(i)), 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        i += 1


        pass

    r = 0
    i = 0
    for url in urls:
        response = requests.get(url, stream=True, verify=False)
        with open('{}//{}_{}.png'.format(output_path, word, str(i)), 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        i += 1


def download(text,path,iter):
    t1 = threading.Thread(target=download_pre(text,path,iter))
    t1.start()

def download_pre(text,path,iter):
    linkler = find_links(text, iter)
    download_images(linkler,path,text)