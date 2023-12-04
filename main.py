import requests
from bs4 import BeautifulSoup
import validators

# Czyszczenie pliku
with open('dane.txt', 'w') as plik:
            plik.write('')
            plik.close()
# Otwarcie pliku w trybie dodawania ('a')
with open('dane.txt', 'a') as file:
    # Otwarcie pliku z linkami i iteracja po każdej linii
    with open('url.txt', 'r') as data_url:
        for line in data_url:
            url = line.strip()

            response = requests.get(url)

            # Utworzenie obiektu BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # wydawca
            wydawca = soup.find('span', {'id': 'game-publisher-cnt'})
            if wydawca is None:
                wydawca = "None"
            else:
                wydawca = wydawca.find('a', {'class': 'un-link'})
                wydawca_text = wydawca.text
            #wydawca PL
            wydawcapl = soup.find('span', {'id': 'game-publisherpl-cnt'})
            if wydawcapl is None:
                wydawcapl = "None"
            else:
                wydawcapl = wydawcapl.find('a', {'class': 'un-link'})
                wydawcapl_text = wydawcapl.text
            #producent
            producent = soup.find('span', {'id': 'game-developer-cnt'})
            if producent is None:
                producent = "None"
            else:
                producent = producent.find('a', {'class': 'un-link'})
                producent_text = producent.text
            #pudełkoPL
            pudelkopl = soup.find('p', {'class': 'p4'})

            if pudelkopl is None:
                pudelkopl_text = "None"
            else:
                pudelkopl_text = pudelkopl.text
            #data wydania pudełkoPL
            data_pudelkopl = soup.find('p', {'class': 'p3'})

            if data_pudelkopl is None:
                data_pudelkopl_text = "None"
            else:
                data_pudelkopl_text = data_pudelkopl.text
            #czyPC
            pc = soup.find('meta', {'property': 'og:title'})

            # Sprawdzenie, czy meta tag istnieje i czy zawartość zawiera tekst "PC"
            if pc and 'PC' in pc.get('content', ''):           
                pc_text = "PC"
            else:           
                pc_text = "None"
            # Zapisanie danych do pliku
            file.write(f"{wydawca_text};{wydawcapl_text};{producent_text};{pudelkopl_text};{pc_text};{data_pudelkopl_text}\n")

print("Dane zostały dodane do pliku dane.txt.")
