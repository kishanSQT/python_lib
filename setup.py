from setuptools import setup, find_packages

setup(
    name="qt",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,  # Include all data files (important for including pytransform)
    package_data={
        "qt": ["pytransform/*"],  # Include all files in the pytransform directory
    },
    install_requires=[  # List of dependencies
        "requests==2.31.0",
        "psutil==6.0.0",
        "GPUtil==1.4.0",
        "boto3==1.34.4",
        "cryptography==43.0.1"
    ],
    description="Helping Package for QuantumDataLytica Machine",
    author="Switchboard LLC",
    author_email="hardik.kanak@softqubes.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)