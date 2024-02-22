from setuptools import setup, find_packages

setup(
    name='PyUpload',
    version='0.1.6',
    packages=find_packages(),
    author='yukinotenshi',
    author_email='gabriel.bentara@gmail.com',
    license='MIT',
    url='https://github.com/yukinotenshi/pyupload',
    install_requires=[
        'requests',
        'requests-toolbelt',
        'click'
    ],
    description='A simple CLI tool to upload file with direct link',
    keywords='direct upload cli',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': ['pyupload=pyupload.main:upload']
    }
)