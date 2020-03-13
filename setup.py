import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ddodds", # Replace with your own username
    version="0.1.1",
    author="ddodds42",
    # author_email="author@example.com",
    description="MetricConvert",
    long_description=long_description,
    long_description_content_type="new class created to instantiate metric converters",
    url="https://github.com/ddodds42/lambdata_ddodds42",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)