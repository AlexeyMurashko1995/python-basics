import requests
from bs4 import BeautifulSoup

target_url = 'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/mazowieckie/warszawa/warszawa/warszawa?limit=36&ownerTypeSingleSelect=ALL&by=DEFAULT&direction=DESC'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

try:
    response = requests.get(target_url, headers=headers, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    area_labels = soup.find_all('dt', string='Cena za metr kwadratowy')
    apartments_data = []

    for label in area_labels:
        clean_area = None
        value_tag = label.find_next_sibling('dd')

        if value_tag:
            try:
                raw_text = value_tag.text

                if '-' in raw_text:
                    raw_text = raw_text.split('-')[0]

                clean_text = raw_text.replace('m²', '').replace(',', '.').strip()
                clean_area = float(clean_text)

                apartments_data.append({
                    'area': clean_area,
                    'price': None
                })
            except (ValueError, IndexError):
                continue

    print(f"Total records extracted: {len(apartments_data)}")
    for apt in apartments_data[:5]:
        print(apt)

except Exception as e:
    print(f"Execution error: {e}")