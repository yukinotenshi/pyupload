from setuptools import setup

setup(
    name='PyUpload',
    version='0.1',
    packages=['pyupload', ],
    author='yukinotenshi',
    author_email='gabriel.bentara@gmail.com',
    license='MIT',
    url='https://github.com/yukinotenshi/pyupload',
    install_requires=[
        'requests',
        'requests-toolbelt',
        'click'
    ],
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': ['pyupload=main:upload']
    }
)