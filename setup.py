import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django_randomprimary",
    version = "0.0.1",
    author = "Juergen Brendel",
    author_email = "",
    description = ("An abstract base class which provides a random looking primary key for Django models"),
    url = "https://github.com/jbrendel/django-randomprimary",
    packages=['django_randomprimary'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
)
