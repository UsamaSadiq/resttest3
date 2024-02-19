from setuptools import setup, find_packages
with open("requirements.txt") as fp:
    install_requires = [lib_str.strip() for lib_str in fp.read().split("\n") if not lib_str.startswith("#")]

with open('README.md') as fp:
    readme = fp.read()

setup(
    name='pythonresttest',
    version="1.1.0",
    description='Python RESTful API Testing & Micro benchmarking Tool',
    long_description=readme,
    author="Abhilash Joseph C",
    author_email='abhilash@softlinkweb.com',
    url='https://github.com/abhijo89-to/resttest3',
    keywords=['rest', 'web', 'http', 'testing', 'api'],
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Utilities'
    ],
    packages=find_packages(),
    python_requires='>=3.5',
    license='Apache License, Version 2.0',
    install_requires=install_requires,
    tests_require=install_requires,
    include_package_data=True,
    package_data={'report': ['reports/template/*.html']},
    test_suite="pythonresttest.tests",
    entry_points={
        'console_scripts': ['resttest3=pythonresttest.runner:main'],
    }

)
