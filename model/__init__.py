import random
import requests
import wikipedia
from model.file_export import Export
from model.body_txt import TxtGeneration
from model.body_pdf import PdfGeneration


class Models:

    def __init__(self):

        self.keyword = None
        self.query_count = None

    def all_inputs(self, keyword, query_count):
        self.keyword = keyword
        self.query_count = query_count
    
    def generate_file_and_export(self):
        self._try_generate_file()
        Export()    

    def _try_generate_file(self):
        try:
            self._write_pages()
        except requests.exceptions.ConnectionError:
            self._error_message('ConnectionError: Please check your network connection', 'Press Enter to exit')

    def _error_message(message, enter):
        print(f'{message}')
        input(enter) 

    def _write_pages(self):
        self._create_body_file()  
        self._create_pdf_file()

    def _create_body_file(self):
        TxtGeneration(self._available_articles())

    def _available_articles(self):
        fetched = [i.replace(' ','_')for i in self._find_articles()]
        return fetched

    def _find_articles(self):
        titles = wikipedia.search(self.keyword, results=1000000)
        rand_titles = random.sample(titles, self.query_count)
        return rand_titles

    def _create_pdf_file(self):
        self._find_articles()
        PdfGeneration(self._find_articles())