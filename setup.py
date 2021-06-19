import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="csv-mqtt",
    version="1.0.2",
    author="srijan-sivakumar",
    author_email="sivakumarsrijan@gmail.com",
    description="CSV parser meets MQTT Publisher",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/srijan-sivakumar/CSV-MQTT/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'paho-mqtt'
    ],
)
