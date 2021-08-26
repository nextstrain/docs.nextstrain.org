#!/usr/bin/env python
import concurrent.futures
import requests
from pathlib import Path

augur_branch = 'master'
augur_url = f'https://raw.githubusercontent.com/nextstrain/augur/{augur_branch}/docs/'

auspice_branch = 'master'
auspice_base_url = f'https://raw.githubusercontent.com/nextstrain/auspice/{auspice_branch}/'
auspice_url = f'{auspice_base_url}docs/'

cli_branch = 'master'
cli_url = f'https://raw.githubusercontent.com/nextstrain/cli/{cli_branch}/doc/'

docs = {
    f'{auspice_url}narratives/create-pdf.md': 'guides/communicate/create-pdf.md',
    f'{auspice_url}narratives/introduction.md': 'guides/communicate/narratives-intro.md',
    f'{auspice_base_url}DEV_DOCS.md': 'guides/contribute/auspice-develop.md',
    f'{auspice_url}narratives/how-to-write.md': 'tutorials/narratives-how-to-write.md',
    f'{augur_url}usage/augur_snakemake.md': 'guides/bioinformatics/augur_snakemake.md',
    f'{augur_url}faq/translate_ref.md': 'guides/bioinformatics/translate_ref.md',
    f'{augur_url}faq/import-beast.md': 'guides/bioinformatics/import-beast.md',
    f'{augur_url}faq/colors.md': 'guides/bioinformatics/colors.md',
    f'{augur_url}faq/lat_longs.md': 'guides/bioinformatics/lat_longs.md',
    f'{augur_url}faq/vcf_input.md': 'guides/bioinformatics/vcf_input.md',
    f'{augur_url}faq/fasta_input.md': 'guides/bioinformatics/fasta_input.md',
    f'{augur_url}faq/seq_traits.md': 'guides/bioinformatics/seq_traits.md',
    f'{augur_url}examples/examples.rst': 'guides/bioinformatics/examples.rst',
    f'{augur_url}contribute/DEV_DOCS.md':   'guides/contribute/augur_develop.md',
    f'{cli_url}development.md': 'guides/contribute/cli-develop.md'
}

if __name__ == '__main__':
    # Use a Session for connection pooling
    session = requests.Session()

    class RemoteDoc:
        def __init__(self, source_url, dest_path):
            self.source_url = source_url
            self.dest_path  = Path(dest_path)

        def __call__(self):
            response = session.get(self.source_url)
            response.raise_for_status()

            self.dest_path.parent.mkdir(exist_ok=True)
            self.dest_path.write_bytes(response.content)

            return self

    # Fetch up to 5 docs at a time.  Thread-based concurrency (as opposed to
    # process-based) is appropriate because this is an I/O-bound operation.
    with concurrent.futures.ThreadPoolExecutor(5) as pool:
        futures = [
            pool.submit(RemoteDoc(src, dst))
                for src, dst in docs.items()
        ]

        for future in concurrent.futures.as_completed(futures):
            doc = future.result()
            print(f"Fetched {doc.dest_path} from {doc.source_url}")
