from setuptools import setup, find_packages

setup(
    name="oscat",
    version="0.1.0",
    description="A comprehensive library for managing directories and files.",
    author="Abbas Faramarzi Filabadi",
    author_email="abbasfaramarzi@068gmail.com",
    url="https://github.com/abbasfaramarzi/os_cat",  # آدرس مخزن گیت‌هاب یا وب‌سایت شما
    packages=find_packages(where='oscat'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'some_package',
    ],
    include_package_data=True,
    package_dir={'': 'os_cat'},
)
