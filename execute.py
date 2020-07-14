from pathlib import Path
import shutil
import mimetypes

import nbconvert
from jupytext import read
from traitlets.config import Config

from nbconvert_fix import ExtractOutputPreprocessor

mimetypes.add_type('application/vnd.plotly.v1+json', '.json')

src = Path('src')
target = Path('docs')
shutil.rmtree(target, ignore_errors=True)
target.mkdir(exist_ok=True)
shutil.copytree(src / 'figures', target / 'figures')
shutil.copytree(src / 'scripts', target / 'scripts')
shutil.copytree(src / 'styles', target / 'styles')
shutil.copytree(src / 'x3d', target / 'x3d')

output_extractor = ExtractOutputPreprocessor()
output_extractor.extract_output_types = (
    output_extractor.extract_output_types
    | {'application/vnd.plotly.v1+json'}
)

exporter = nbconvert.MarkdownExporter(
    config=Config(dict(
        MarkdownExporter=dict(
            preprocessors=[
                nbconvert.preprocessors.ExecutePreprocessor,
                output_extractor,
            ],
            exclude_input=False,
            template_file='extra_markdown.tpl',
        ),
        NbConvertBase=dict(
            display_data_priority=[
                'text/html',
                'text/markdown',
                'image/svg+xml',
                'text/latex',
                'image/png',
                'application/vnd.plotly.v1+json',
                'image/jpeg',
                'text/plain'
            ]
        ),
    ))
)

writer = nbconvert.writers.FilesWriter(build_directory=str(target))

for source_file in src.glob('*.md'):
    fname = source_file.stem
    notebook = read(source_file)

    output, resources = exporter.from_notebook_node(
        notebook,
        resources={
            'unique_key': fname,
            'output_files_dir': 'figures',
            'metadata': {'path': 'src/code'}
        }
    )

    writer.write(output, resources, fname)
