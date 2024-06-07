from setuptools import setup, find_packages

setup(
    name='easy-nlp',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'nltk',
        'transformers',
        'torch',
        'numpy',
        'scikit-learn'
    ],
    description='A simple NLP library for preprocessing, sentiment analysis, text generation, translation, and summarization.',
    author='Masaki Shito',
    author_email='happy.engineer.life@gmail.com',
    url='https://github.com/masakiShito/easy-nlp',
)
