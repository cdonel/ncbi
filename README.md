# NCBI record retrieval

For downloading records from various NCBI databases.

## REQUIRED
A config.py file needs to be added to the working directory contain:

    email="ncbi_account_email"
    apikey="ncbi_account_apikey"

## Retrieving Nucleotide records via command line using nucleotide.py

python nucleotide.py **-s** [search phrase] **-t** [return type] **-n** [number of sequences] **-o** [output file] 

**Example**: Retrieves 100 FASTA sequences for organism *Homo sapiens*

python nucleotide.py -s "Homo sapiens[organism]" -t fasta -n 100 -o test.fasta