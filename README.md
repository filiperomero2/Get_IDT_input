# Get_IDT_input

This repo contains a simple python script to generate fasta files with a specific format required by IDT to perform primer design with rhAmp technology. It has been released as part of a protocol for SARS-CoV-2 variants detection, but can be used for other models. The full protocol is available at: https://dx.doi.org/10.17504/protocols.io.buf2ntqe​

The script is easy to use and require only three arguments: the path for the reference genome fasta file, the genome target site and the possible alleles at this position. For example:
    
    python Get_Sequence_Input_for_IDT_RhAmp_Design.py SARS-CoV-2.fasta 23012 AG

This command would create a fasta file with a excerpt of 200 nucleotides fragment of the SARS-CoV-2 genome, with the possible alleles (A or G) marked within square brackets in the position 23,012. This file may be used as input for the IDT primer design software to promptly generate candidate genotyping  primer sets. 


