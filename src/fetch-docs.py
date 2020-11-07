#!/usr/bin/env python
import subprocess

edit_warning = '<!-- DONT EDIT THIS FILE OR YOU WILL LOSE YOUR CHANGES -->'

augur_branch = 'migrate-docs'
augur_url = f'https://raw.githubusercontent.com/nextstrain/augur/{augur_branch}/docs/'

auspice_branch = 'migrate-docs'
auspice_url = f'https://raw.githubusercontent.com/nextstrain/auspice/{auspice_branch}/docs/'

docs = {
    f'{auspice_url}narratives/create-pdf.md': 'guides/communicate/create-pdf.md',
    f'{augur_url}usage/augur_snakemake.md': 'guides/bioinformatics/augur_snakemake.md',
    f'{augur_url}faq/translate_ref.md': 'guides/bioinformatics/translate_ref.md',
    f'{augur_url}faq/import-beast.md': 'guides/bioinformatics/beast.md',
    f'{augur_url}faq/colors.md': 'guides/bioinformatics/colors.md',
    f'{augur_url}faq/lat_longs.md': 'guides/bioinformatics/lat_longs.md',
    f'{augur_url}faq/vcf_input.md': 'guides/bioinformatics/vcf_input.md',
    f'{augur_url}faq/fasta_input.md': 'guides/bioinformatics/fasta_input.md',
    f'{augur_url}faq/seq_traits.md': 'guides/bioinformatics/seq_traits.md',
    f'{augur_url}examples/examples.rst': 'guides/bioinformatics/examples.rst',
}

if __name__ == '__main__':
    for source_url, dest_path in docs.items():
        subprocess.check_call(['curl', source_url, '--compressed', '-o', dest_path])
