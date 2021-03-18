import requests
import re
from bs4 import BeautifulSoup
base_url='https://www.cai-fvg.it/sentieri-cai-fvg/'

class Sentiero:
    def __init__(self, code):
        self.code = code
        r = self.web_url()
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        dettagli=soup.find(class_="su-column-inner su-u-clearfix su-u-trim").find_all("p")
        lista_dettagli = [p.text.replace('\xa0',"").split("\n") for p in soup.find(class_="su-column-inner su-u-clearfix su-u-trim").find_all("p")]
        lista_link = [k.attrs['href'] for k in soup.find(class_="su-column-inner su-u-clearfix su-u-trim").find_all("a")]
        
        self.summary = summary_info(soup)
        self.desc = re.sub(r"\nDESCRIZIONE DEL PERCORSO:\n|FOTO","",soup.find(class_="su-column su-column-size-2-3").get_text())
        self.partenza = lista_dettagli[0][1]
        self.arrivo = lista_dettagli[1][1]
        self.dislivello = ' '.join(lista_dettagli[2]).replace('Dislivello: ',"")
        self.long = ' '.join(lista_dettagli[3]).replace('Lunghezza: ',"")
        self.time = ' '.join(lista_dettagli[4]).replace('Tempo di percorrenza: ',"")
        self.punti_app = ' '.join(lista_dettagli[5]).replace('Punti di appoggio: ',"")
        self.imm_url = imm_url(lista_link)
        self.alt_url = altitude_url(lista_link)
        self.gps = gpx_url(lista_link)
        
    def web_url(self):
        url_sector = web_url_sector(int(self.code[0]))
        url_trail = web_url_trail(self.code)
        if requests.get("{base_url}{url_sector}{url_trail}".format(base_url=base_url,url_sector=url_sector,url_trail=url_trail)).status_code != 404:
           return (requests.get("{base_url}{url_sector}{url_trail}".format(base_url=base_url,url_sector=url_sector,url_trail=url_trail)))
        else:
            return(requests.get("{base_url}{url_sector}{url_trail}s".format(base_url=base_url,url_sector=url_sector,url_trail=url_trail)))



def altitude_url(elenco_link):
    try:
        return(elenco_link[2])
    except:
        return('None')
    
def gpx_url(elenco_link):
    try:
        return(elenco_link[4])
    except:
        return('None')
    
def summary_info(sentiero_soup):
    try:
        return(sentiero_soup.find_all('h5')[1].get_text())
    except:
        try:
            return(sentiero_soup.find_all('h5')[0].get_text())
        except:
            return(sentiero_soup.find_all('h4')[0].get_text())

def imm_url(elenco_link):
      return (elenco_link[0])  

def web_url_sector(ini_code_trail):
    code_url=d = {0: 'sentieri-cai-fvg-settore-0-carso/', 1:'settore-1-alpi-carniche/', 2: 'settore-2-dolomiti-pesarine-monti-di-sauris/',
                3: 'settore-3-dolomiti-friulane-alpi-prealpi-carniche/',4: 'settore-4-alpi-carniche/', 5: 'settore-5-alpi-giulie/',
                6: 'settore-6-alpi-giulie/',7: 'settore-7-prealpi-giulie/',8: 'settore-8-prealpi-carniche/',9: 'settore-9-prealpi-carniche/'}
    return code_url[ini_code_trail]

def web_url_trail(code):
        return 's{sector}-{code_trail}'.format(sector=code[0],code_trail=code)
