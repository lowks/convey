from setuptools import find_packages, setup

setup(
    name='convey',
    version='0.1.0',
    description='App to add descriptive context around tests',
    author='DISQUS',
    author_email='opensource@disqus.com',
    url='https://github.com/disqus/convey',
    packages=find_packages(),
    package_dir={'': 'src'},
    zip_safe=False,
    include_package_data=True,
)
