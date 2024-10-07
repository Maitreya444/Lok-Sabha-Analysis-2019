from selenium import webdriver
from bs4 import BeautifulSoup
import csv

def scrape_myneta_info(url):
    # Starting a new browser session
    driver = webdriver.Chrome()
    driver.get(url)

    # Waiting for the page to fully render
    driver.implicitly_wait(10)

    # Getting the page source after rendering
    page_source = driver.page_source

    # Closing the browser
    driver.quit()

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Finding all tables with the class "w3-table w3-bordered"
    tables = soup.find_all("table", class_="w3-table w3-bordered")

    scraped_data = []

    for table in tables:
        for row in table.find_all('tr'):
            # Initialize a dictionary to store the data for each row
            row_data = {}
            cells = row.find_all('td')
            if len(cells) > 0:  # To skip rows without data
                row_data['Sno'] = cells[0].text.strip()
                row_data['Candidate'] = cells[1].text.strip()
                row_data['Constituency'] = cells[2].text.strip()
                row_data['Party'] = cells[3].text.strip()
                row_data['Criminal Case'] = cells[4].text.strip()
                row_data['Education'] = cells[5].text.strip()
                row_data['Total Assets'] = cells[6].text.strip()
                row_data['Liabilities'] = cells[7].text.strip()
                scraped_data.append(row_data)
    
    return scraped_data

def main():
    base_url = "https://www.myneta.info/LokSabha2024/index.php?action=summary&subAction=candidates_analyzed&sort=candidate&page="
    total_pages = 84
    all_data = []

    for page in range(1, total_pages + 1):
        url = base_url + str(page)
        print("Scraping page:", page)
        data = scrape_myneta_info(url)
        all_data.extend(data)  # Extend the list with data from the current page

    csv_file = "neta2.csv"
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['Sno', 'Candidate', 'Constituency', 'Party', 'Criminal Case', 'Education', 'Total Assets', 'Liabilities']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_data)

if __name__ == "__main__":
    main()
