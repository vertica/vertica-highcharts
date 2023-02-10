import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

ns = {}
with open(os.path.join(here, 'vertica_highcharts', 'version.py')) as f:
   exec(f.read(), {}, ns)

setup(
    name='vertica-highcharts',
    version=ns['__version__'],
    author='Kyper Developers',
    author_email='developers@kyperdata.com',
    packages=find_packages(),
    package_data={
        'vertica_highcharts.highcharts': ['templates/*.html'],
        'vertica_highcharts.highmaps': ['templates/*.html'],
        'vertica_highcharts.highstock': ['templates/*.html']
    },
    url='https://github.com/vertica/vertica-highcharts',
    download_url='https://github.com/vertica/vertica-highcharts/releases/tag/' + ns['__version__'],
    description='Python Highcharts wrapper',
    install_requires=[
        "Jinja2",
        "future"
    ],
    keywords = ['python', 'ipython', 'highcharts', 'chart', 'visualization', 'graph', 'javascript', 'html'],
    classifiers         = [
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
