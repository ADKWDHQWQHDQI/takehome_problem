import requests
import csv
from typing import List, Dict, Any

class PubMedFetcher:
    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

    def __init__(self, email: str):
        self.email = email

    def fetch_papers(self, query: str) -> List[Dict[str, Any]]:
        params = {
            'db': 'pubmed',
            'term': query,
            'retmode': 'json',
            'retmax': '100',  # Limit the number of results to 100
            'email': self.email
        }
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        id_list = data['esearchresult']['idlist']
        
        papers = self.fetch_paper_details(id_list)
        return papers

    def fetch_paper_details(self, id_list: List[str]) -> List[Dict[str, Any]]:
        if not id_list:
            return []
        
        params = {
            'db': 'pubmed',
            'id': ','.join(id_list),
            'retmode': 'json',
            'email': self.email
        }
        response = requests.get(self.FETCH_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        papers = []
        for uid, paper in data['result'].items():
            if uid == 'uids':
                continue
            papers.append({
                'PubmedID': uid,
                'Title': paper.get('title', 'No title available'),
                'Publication Date': paper.get('pubdate', 'No date available'),
                'Authors': paper.get('authors', []),
                'Corresponding Author Email': paper.get('lastauthor', 'No email available')
            })
        return papers

    def filter_non_academic_authors(self, papers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        filtered_papers = []
        for paper in papers:
            non_academic_authors = [author for author in paper['Authors'] if 'university' not in author.lower()]
            if non_academic_authors:
                paper['Non-academic Author(s)'] = non_academic_authors
                paper['Company Affiliation(s)'] = 'Company names'  # Placeholder for actual company names
                filtered_papers.append(paper)
        return filtered_papers

    def save_to_csv(self, papers: List[Dict[str, Any]], filename: str):
        keys = ['PubmedID', 'Title', 'Publication Date', 'Non-academic Author(s)', 'Company Affiliation(s)', 'Corresponding Author Email']
        with open(filename, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(papers)