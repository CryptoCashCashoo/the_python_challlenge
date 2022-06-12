import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

install_requires = []
with open(os.path.join("installation/requirements.txt")) as f:
    install_requires = f.read().splitlines()
print(install_requires)

setuptools.setup(
    name="TEMPLATE",
    version="1.0.0",
    author="TEMPLATE",
    description="TEMPLATE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CryptoCashCashoo/TEMPLATE",
    install_requires=install_requires,
    packages=setuptools.find_packages(),
    # package_data={"random": ["Random.txt"]},
    # include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
)
