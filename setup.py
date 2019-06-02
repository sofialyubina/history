from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hisory',
    version='0.0.1',
    description='AI history project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='The MIT License',
    author='Sonya and Dima',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
    ],

    packages=find_packages(),

    keywords='nlp',
    install_requires=["gensim", "sklearn", "numpy",
                      "editdistance", "tqdm", "nltk"],
)
