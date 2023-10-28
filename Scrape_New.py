from bs4 import BeautifulSoup
import requests

def scrape_and_write_data(input_file, output_file):
    with open(input_file, "r") as f, open(output_file, "w") as f_out:
        urls = [line.strip() for line in f.readlines()]

        for url in urls:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, 'html.parser')
                nom = soup.find_all('span', class_='iceOutTxt')
                lines = ("{}. {}\n".format(ind, span.get_text(strip=True).rstrip("+"))
                         for ind, span in enumerate(nom, 1))
                f_out.write(f'Dominio: {url}, Versión: {"".join(lines)}\n')
            except Exception as e:
                print(f"Ignorando la excepción al procesar {url}: {str(e)}")

if __name__ == "__main":
    scrape_and_write_data("venv/qa.txt", "D:/qa.txt")
    scrape_and_write_data("venv/lista.txt", "D:/file.txt")
