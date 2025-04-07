import sys
from SearchPrimaryID import SearchPrimaryID
from FetchRecords import FetchRecords
from Bio import Entrez
import config
import argparse
                
def main():

    """
    Main function that executes SearchPrimaryIDs and FetchRecords to get primary IDs from NCBI nucleotide database to retrieve records.
    Suitable for large queries.
    
    Set Entrez.email to personal NCBI email address.
    Set Entrex.api to api key found in NCBI account.
    """
    
    parser = argparse.ArgumentParser(prog='nucleotide', description='Retrieves records from ncbi nucleotide databases')
    parser.add_argument('-s', '--search')
    parser.add_argument('-t', '--rettype')
    parser.add_argument('-n', '--retmax')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()

    Entrez.email = config.email
    Entrez.api_key = config.apikey
    primary_ids = SearchPrimaryID(db='nucleotide', idtype='acc', term=args.search, retmax=args.retmax, retmode='text')
    records = FetchRecords(primary_ids=primary_ids, db='nucleotide', idtype='acc', rettype=args.rettype, filename=args.output)
    sys.exit()

if __name__ == '__main__':
    main()