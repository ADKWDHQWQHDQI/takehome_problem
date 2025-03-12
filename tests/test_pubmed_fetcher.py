import unittest
from src.pubmed_fetcher import PubMedFetcher

class TestPubMedFetcher(unittest.TestCase):

    def setUp(self):
        self.fetcher = PubMedFetcher(email='your_email@example.com')

    def test_fetch_papers(self):
        papers = self.fetcher.fetch_papers('cancer')
        self.assertIsInstance(papers, list)
        self.assertGreater(len(papers), 0)

    def test_filter_non_academic_authors(self):
        papers = [
            {
                'PubmedID': '12345',
                'Title': 'Research Paper 1',
                'Publication Date': '2025-01-01',
                'Authors': ['John Doe', 'Jane Smith University'],
                'Corresponding Author Email': 'john.doe@example.com'
            }
        ]
        filtered_papers = self.fetcher.filter_non_academic_authors(papers)
        self.assertEqual(len(filtered_papers), 1)
        self.assertEqual(filtered_papers[0]['Non-academic Author(s)'], ['John Doe'])

if __name__ == '__main__':
    unittest.main()