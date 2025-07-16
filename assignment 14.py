import requests
from lxml import html
import pandas as pd


def scrape_country_data(url):
    """
    Scrapes country data from the given URL.
    Returns a list of dictionaries with keys: Country, Capital, Population, Area (km2)
    """
    response = requests.get(url)
    tree = html.fromstring(response.content)

    countries = []

    # Loop through each country section on the page
    rows = tree.xpath('//div[@class="col-md-4 country"]')
    for row in rows:
        country_name = row.xpath('.//h3[@class="country-name"]')[0].text_content().strip()
        capital = row.xpath('.//span[@class="country-capital"]/text()')[0].strip()
        population = row.xpath('.//span[@class="country-population"]/text()')[0].strip().replace(',', '')
        area = row.xpath('.//span[@class="country-area"]/text()')[0].strip().replace(',', '')

        countries.append({
            "Country": country_name,
            "Capital": capital,
            "Population": int(population),
            "Area (km2)": float(area)
        })

    return countries


def export_data(data, file_type='csv', filename='countries'):
    """
    Exports country data to CSV
    """
    df = pd.DataFrame(data)

    if file_type == 'csv':
        df.to_csv(f'{filename}.csv', index=False)
        print(f"Data saved as {filename}.csv")




if __name__ == "__main__":
    url = "https://www.scrapethissite.com/pages/simple/"
    country_data = scrape_country_data(url)

    for item in country_data[:3]:
        print(item)

    # Export to CSV and Excel
    export_data(country_data, file_type='csv', filename='country_data')

