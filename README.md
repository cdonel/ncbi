# ncbi package

For downloading records from various NCBI databases.

## REQUIRED
A config.py file needs to be added to the working directory contain:
    1. NCBI email address.
    2. OPTIONAL NCBI api key obtained through NCBI account. Allows for more API requests per second.

## Retrieving Nucleotide records via command line using nucleotide.py

python nucleotide.py **-s** [search phrase] **-t** [return type] **-n** [number of sequences] **-o** [output file] 

**Example**: Retrieves 100 FASTA sequences for organism *Homo sapiens*

python nucleotide.py -s "Homo sapiens[organism]" -t fasta -n 100 -o test.fasta