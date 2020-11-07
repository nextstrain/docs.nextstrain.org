#!/usr/bin/env python
import subprocess

edit_warning = '<!-- DONT EDIT THIS FILE OR YOU WILL LOSE YOUR CHANGES -->'

augur_branch = 'migrate-docs'
augur_url = f'https://raw.githubusercontent.com/nextstrain/augur/{augur_branch}/docs/'

auspice_branch = 'migrate-docs'
auspice_url = f'https://raw.githubusercontent.com/nextstrain/auspice/{auspice_branch}/docs/'

cli_branch = 'migrate-docs'
cli_url = f'https://raw.githubusercontent.com/nextstrain/cli/{cli_branch}/doc/'

ncov_branch = 'master'
ncov_url = f'https://raw.githubusercontent.com/nextstrain/ncov/{ncov_branch}/docs/'

docs = {
    f'{auspice_url}narratives/create-pdf.md': 'guides/communicate/create-pdf.md',
    f'{auspice_url}narratives/introduction.md': 'guides/communicate/narratives-intro.md',
    f'{auspice_url}contributing/overview.md': 'guides/contribute/auspice-develop.md',
    f'{auspice_url}introduction/install.md': 'guides/install/auspice-install.md',
    f'{auspice_url}narratives/how-to-write.md': 'tutorials/narratives-how-to-write.md',
    f'{augur_url}usage/augur_snakemake.md': 'guides/bioinformatics/augur_snakemake.md',
    f'{augur_url}faq/translate_ref.md': 'guides/bioinformatics/translate_ref.md',
    f'{augur_url}faq/import-beast.md': 'guides/bioinformatics/beast.md',
    f'{augur_url}faq/colors.md': 'guides/bioinformatics/colors.md',
    f'{augur_url}faq/lat_longs.md': 'guides/bioinformatics/lat_longs.md',
    f'{augur_url}faq/vcf_input.md': 'guides/bioinformatics/vcf_input.md',
    f'{augur_url}faq/fasta_input.md': 'guides/bioinformatics/fasta_input.md',
    f'{augur_url}faq/seq_traits.md': 'guides/bioinformatics/seq_traits.md',
    f'{augur_url}examples/examples.rst': 'guides/bioinformatics/examples.rst',
    f'{augur_url}contribute/DEV_DOCS.md':   'guides/contribute/augur_develop.md',
    f'{augur_url}installation/installation.md': 'guides/install/augur_install.md',
    f'{augur_url}tutorials/zika_tutorial.md': 'tutorials/zika_tutorial.md',
    f'{augur_url}tutorials/tb_tutorial.md': 'tutorials/tb_tutorial.md',
    f'{cli_url}development.md': 'guides/contribute/cli-develop.md',
    f'{cli_url}installation.md': 'guides/install/cli-install.md',
    f'{ncov_url}index.md': 'tutorials/SARS-CoV-2/steps/index.md',
    f'{ncov_url}setup.md': 'tutorials/SARS-CoV-2/steps/setup.md',
    f'{ncov_url}data-prep.md': 'tutorials/SARS-CoV-2/steps/data-prep.md',
    f'{ncov_url}orientation-workflow.md': 'tutorials/SARS-CoV-2/steps/orientation-workflow.md',
    f'{ncov_url}orientation-files.md': 'tutorials/SARS-CoV-2/steps/orientation-files.md',
    f'{ncov_url}running.md': 'tutorials/SARS-CoV-2/steps/running.md',
    f'{ncov_url}customizing-analysis.md': 'tutorials/SARS-CoV-2/steps/customizing-analysis.md',
    f'{ncov_url}customizing-visualization.md': 'tutorials/SARS-CoV-2/steps/customizing-visualization.md',
    f'{ncov_url}sharing.md': 'tutorials/SARS-CoV-2/steps/sharing.md',
    f'{ncov_url}interpretation.md': 'tutorials/SARS-CoV-2/steps/interpretation.md',
    f'{ncov_url}narratives.md': 'tutorials/SARS-CoV-2/steps/narratives.md',
}

if __name__ == '__main__':
    for source_url, dest_path in docs.items():
        subprocess.check_call(['curl', source_url, '--compressed', '-o', dest_path])
