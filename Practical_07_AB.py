import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urlparse, urljoin
from urllib.robotparser import RobotFileParser

class WebCrawler:
    def __init__(self, seed_url, max_pages=100):
        self.seed_url = seed_url
        self.base_url = urlparse(seed_url).scheme + '://' + urlparse(seed_url).hostname
        self.visited_urls = set()
        self.queue = [seed_url]
        self.max_pages = max_pages
        self.pages_crawled = 0
        self.robot_parser = RobotFileParser()
        self.robot_parser.set_url(urljoin(self.base_url, '/robots.txt'))
        self.robot_parser.read()

    def is_allowed_by_robots(self, url):
        return self.robot_parser.can_fetch('*', url)

    def crawl(self):
        while self.queue and self.pages_crawled < self.max_pages:
            current_url = self.queue.pop(0)

            if current_url not in self.visited_urls and self.is_allowed_by_robots(current_url):
                try:
                    response = requests.get(current_url)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, 'html.parser')

                        # Here you can implement your indexing logic
                        # For example, extract text, store in a database, etc.

                        print(f"Crawled: {current_url}")

                        # Extract links from the page and add them to the queue
                        for link in soup.find_all('a', href=True):
                            new_url = urljoin(current_url, link['href'])
                            if new_url.startswith(self.base_url) and new_url not in self.visited_urls:
                                self.queue.append(new_url)

                        self.visited_urls.add(current_url)
                        self.pages_crawled += 1

                except Exception as e:
                    print(f"Error crawling {current_url}: {str(e)}")

                # Introduce a delay to avoid being too aggressive
                time.sleep(1)

if __name__ == "__main__":
    seed_url ="https://www.wikipedia.org/"
    max_pages_to_crawl = 50

    crawler = WebCrawler(seed_url, max_pages_to_crawl)
    crawler.crawl()
