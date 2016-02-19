from setuptools import setup, find_packages

VERSION = '0.0.1'


setup(
    name="{{cookiecutter.repo_name}}",
    version=VERSION,
    url='{{cookiecutter.repo_url}}',
    license='BSD',
    description='Minimal theme for MkDocs',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            '{{cookiecutter.repo_name}} = {{cookiecutter.repo_name}}',
        ]
    },
    zip_safe=False
)
