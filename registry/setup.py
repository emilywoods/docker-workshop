from setuptools import setup

setup(
    name="pyladies-devops-workshop",
    install_requires=["apscheduler==3.6.1", "flask==1.1.1", "requests==2.22.0"],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 1 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
