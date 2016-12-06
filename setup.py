import setuptools

setuptools.setup(
    author_email="allen.goodman@icloud.com",
    author="Allen Goodman",
    description="Broad Institute Imaging Benchmark",
    license="MIT",
    name="bib",
    packages=setuptools.find_packages(
        exclude=[
            "tests"
        ]
    ),
    url="https://github.com/0x00B1/bib",
    version="0.0.0"
)
