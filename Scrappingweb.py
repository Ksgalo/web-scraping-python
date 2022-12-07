from bs4 import BeautifulSoup
import requests

with open("venv/qa.txt", "r") as f, open("D:/qa.txt", "w") as f_out:
    x = (list(map(str.strip, f.readlines())))
    try:
        for i in x:
            page = requests.get(i)
            soup = BeautifulSoup(page.content, 'html.parser')
            nom = soup.find_all('span', class_='iceOutTxt')
            lines = ("{}. {}\n".format(ind, span.get_text(strip=True).rstrip("+"))
                     for ind, span in enumerate(nom, 1))
            f_out.write('Dominio' + repr(i) + 'Version' + "".join(lines) + "\n")
    except Exception:
        pass

    print("ignored the exception")

with open("venv/lista.txt", "r") as h, open("D:/file.txt", "w") as f_outi:
    k = (list(map(str.strip, h.readlines())))
    try:
        for j in k:
            page = requests.get(j)
            soup = BeautifulSoup(page.content, 'html.parser')
            nom = soup.find_all('span', class_='iceOutTxt')
            lines = ("{}. {}\n".format(ind, span.get_text(strip=True).rstrip("+"))
                     for ind, span in enumerate(nom, 1))
            f_outi.write('Dominio' + repr(j) + 'Version' + "".join(lines) + "\n")
    except Exception:
        pass

    print("ignored the exception")
