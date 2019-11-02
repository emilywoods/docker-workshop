from setuptools import setup

setup(
    name="pyladies-devops-workshop",
    python_requires=">=3.7",
    install_requires=[
        "apscheduler==3.6.1",
        "flask==1.1.1",
        "requests==2.22.0",
        "flask-expects-json==1.4.0",
    ],
    classifiers=[
        "Development Status :: 1 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
