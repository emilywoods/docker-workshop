from setuptools import setup

setup(
    name="workshop-client",
    install_requires=["flask==1.1.1", "requests==2.22.0"],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 1 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
