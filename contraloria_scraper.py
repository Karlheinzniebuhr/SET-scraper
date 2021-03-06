# autores: @quanturtle, @karlpy

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import lxml.html as lh

controlaria_urls = open('contraloria_urls.txt', 'r')
URLS = controlaria_urls.readlines()
session = requests.Session()

for index, url in enumerate(URLS):
    try:
        url = url.strip()
        print(f'Downloading URL {index+1}: {url}')

        # getting session cookie
        get_response = session.get(url, verify=False)

        # getting token from html form
        doc = lh.fromstring(get_response.content)
        token = doc.xpath('//*[@id="phocadownloadform"]/input[4]')[0].name
        file_ref = url.split('/')[-1].split('-')[0]

        payload = {
            'submit': 'Descarga',
            'license_agree': '1',
            'download': file_ref,
            token: '1'
        }

        # make POST request with session cookie
        post_response = session.post(url, data=payload)

        filename = f"contraloria/{url.split('/')[-1].replace('-pdf','')}.pdf"
        with open(filename, 'wb') as outfile:
            outfile.write(post_response.content)
    except Exception as ex:
        print(ex)
        continue