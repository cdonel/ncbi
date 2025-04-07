import sys
from SearchPrimaryID import SearchPrimaryID
from FetchRecords import FetchRecords
from Bio import Entrez
import config
import argparse

def main():

    """
    Main function that retrieves research articles from NCBI pubmed.

    Set Entrez.email to personal NCBI email address.
    Set Entrex.api to api key found in NCBI account.
    """

    Entrez.email = config.email
    Entrez.api_key = config.apikey
    parser = argparse.ArgumentParser(prog='pubmed', description='Retrieves articles from ncbi pubmed databases')
    parser.add_argument('-s', '--search')
    parser.add_argument('-n', '--retmax')
    args = parser.parse_args()

    primary_ids = SearchPrimaryID(db='pubmed', term=args.search, retmax=args.retmax)
    records = FetchRecords(primary_ids=primary_ids, db='pubmed', rettype='medline', retmode='text', filename='pubmed_test.txt')

if __name__ == '__main__':
    main()