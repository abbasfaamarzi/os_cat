from setuptools import setup, find_packages

setup(
    name="oscat",
    version="0.1.0",
    description="A comprehensive library for managing directories and files.",
    author="Abbas Faramarzi Filabadi",
    author_email="abbasfaramarzi@068gmail.com",
    url="https://github.com/abbasfaramarzi/os_cat",  # آدرس مخزن گیت‌هاب یا وب‌سایت شما
    packages=find_packages(),
    install_requires=[
        # وابستگی‌های بسته شما
        # مثال: 'requests', 'numpy',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # یا هر لایسنس دیگری که استفاده می‌کنید
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # نسخه پایتون مورد نیاز
)
