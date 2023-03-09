from setuptools import find_packages, setup

setup(
    name="wheat-yield-prediction-toolkit",
    version="0.1.0",
    author="Noureddine Ech-chouky",
    author_email="noureddineechchouky@gmail.com",
    description="Wheat Yield Prediction Toolkit is a package that provides tools for predicting wheat yield at the county level in the main wheat-producing regions of the US using deep learning approaches. The package includes modules for data collection, preprocessing, modeling, and uncertainty analysis. It allows users to easily collect and preprocess soil, weather, yield, and remote sensing data, train deep learning models for yield prediction, and analyze the uncertainty of the predictions. The package is designed for researchers and practitioners in agriculture and data science who want to improve the accuracy and efficiency of wheat yield prediction.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nour3467/wheat-yield-prediction-toolkit",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.9",
    style_packages=["black==22.3.0", "flake8==3.9.2", "isort==5.10.1"],
    docs_packages=[
        "sphinx==4.2.0",
        "sphinx-rtd-theme==1.0.0",
    ],
    install_requires=[
        "tqdm",
        "geopandas",
        "pytest",
        "pandas",
        "python-dotenv",
        "pyarrow",
        "earthengine-api",
        "geemap",
        "rasterio",
        "owslib",
        "scienceplots",
        "meteostat",
        # add any other dependencies here
    ],
    extras_require={
        "dev": docs_packages + style_packages,
        "docs": docs_packages,
    },
)
