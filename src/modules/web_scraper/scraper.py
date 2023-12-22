from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer

class Scraper:
    def __init__(self):
        pass

    def scrape(self, url):
        loader = AsyncChromiumLoader(urls=[url])
        html = loader.load()

        transformer = BeautifulSoupTransformer()
        docs_transformed = transformer.transform_documents(html, tags_to_extract=["span"])

        return docs_transformed[0].page_content


if __name__ == "__main__":
    scraper = Scraper()
    print(scraper.scrape("https://www.google.com/"))


