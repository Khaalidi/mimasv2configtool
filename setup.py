from setuptools import setup

setup(
    name="mimasv2configtool",
    version="2025.0.1",
    description="Numato Lab Mimas V2 Configuration Tool",
    author="Habib Ullah",
    author_email="khaalidi@icloud.com",
    py_modules=["main"],
    install_requires=[
        "pyserial",
    ],
    entry_points={
        "console_scripts": [
            "mimasv2config=main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
