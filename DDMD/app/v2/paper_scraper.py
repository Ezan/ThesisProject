# timeout = 20
# try:
#     WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="img"]')))
# except TimeoutException:
#     print('sorry...not opening')
#     browser.close()

def scrape(title):
    import requests, lxml
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.chrome.options import Options
    from fake_useragent import UserAgent

    import time
    import sys
    import os

    path_loc = "../datasets/papers/"

    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}')
    browser = webdriver.Chrome(chrome_options=options, executable_path='../chromedriver')
    keyword = title.replace(" ", "+")
    count = 0
    baseURL = "https://scholar.google.com/scholar?start={}&q={}&hl=en&as_sdt=0,28".format(0, keyword)
    browser.get(baseURL)
    print('Downloading page...')
    time.sleep(5)
    scroll_down = 5000
    count = 0
    hrefs = []
    # while True:
    browser.execute_script("window.scrollTo(0, {})".format(scroll_down))
    pages = browser.find_elements(By.CLASS_NAME, 'gs_nma')
    print(len(pages))
    i = 0

    while count < len(pages) * 10:
        time.sleep(5)
        url = "https://scholar.google.com/scholar?start={}&q={}&hl=en&as_sdt=0,28".format(count, keyword)
        count += 10
        browser.get(url)
        print('scraping page %2d of %2d' % (count // 10, 10))

        response = requests.get(url).text
        # soup = BeautifulSoup(response.text, 'html.parser')
        soup = BeautifulSoup(response, 'lxml')

        for result in soup.select('.gs_r.gs_or.gs_scl'):
            try:
                is_pdf_link = result.select_one('.gs_ctg2').getText() == "[PDF]"
                if is_pdf_link:
                    i += 1
                    title = result.select_one('.gs_rt').text
                    pdf_link = result.select_one('.gs_or_ggsm a:nth-child(1)').get('href')

                    response = requests.get(pdf_link)
                    # Write content in pdf file
                    with open(path_loc + str(i) + "_" + title.replace(" ", "_") + ".pdf", 'wb') as f:
                        f.write(response.content)
                        f.close()
                    # pdf = open("./papers/" + str(i) + "_" + title.replace(" ", "_") + ".pdf", 'wb')
                    # pdf.write(response.content)
                    # pdf.close()
            except:
                is_pdf_link = False
                continue

    print("All PDF files downloaded")
