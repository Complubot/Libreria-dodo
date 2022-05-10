import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="libreria dodo",
    version="0.0.8",
    author="Complubot",
    author_email="info@complubot.com",
    description="Libreria para la placa dodo y dodo lite",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Complubot/Libreria-dodo",
    project_urls={
        "Bug Tracker": "https://github.com/Complubot/Libreria-dodo/issues",
    },
    classifiers=[
        "Programming Language :: Python :: Implementation :: MicroPython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)