from setuptools import setup, find_packages


setup(
    author="Hiroshi Matsuda",
    author_email="hmtd223@gmail.com",
    description="A command line tool for masking the content area in PDF",
    entry_points={
        "console_scripts": [
            "pdfmask = pdfmask.mask:main",
            "pdfmask_gen = pdfmask.mask_gen:main",
        ],
    },
    python_requires=">=3.6",
    install_requires=[
        "reportlab>=3.6.11,<3.7.0",
        "PyPDF2>=2.10.3,<2.11.0",
    ],
    license="BSD-3-Clause",
    name="pdfmask",
    packages=find_packages(include=["pdfmask"]),
    url="https://github.com/hiroshi-matsuda/pdfmask",
    version='0.1.0',
)
