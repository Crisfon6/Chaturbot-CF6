setup(
    name="Chaturbot-cf6",
    version="1.0.0",
    description="Bot for boost models of chaturbate",    
    url="https://github.com/Crisfon6/Chaturbot-CF6",
    author="Crisfon6",
    author_email="disruptivecrisfon6@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=[
        "selenium", "pandas", "tk", ""
    ],
    entry_points={"console_scripts": ["realpython=reader.__main__:main"]},
)