from bs4 import BeautifulSoup
import requests


def parser_sitemap_xml(site):
    response = requests.get(site).text
    soup = BeautifulSoup(response, 'html.parser')
    urls = soup.find_all('loc')
    list = []
    for url in urls:
        url = str(url)
        url = url.replace("<loc>", "").replace("</loc>", "")
        list.append(url)
    return list


if __name__ == '__main__':
    site = 'https://pypi.org/sitemap.xml'
    urls = parser_sitemap_xml(site)
    result = []
    for url in urls:
        result.append(parser_sitemap_xml(url))
        f = open('urls.txt', 'w')
        for index in result:
            index = str(index).replace("\\", "")
            f.write(index + '\n')
