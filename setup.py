from setuptools import find_packages, setup

setup(
    name="MCQGenerator",
    version="0.0.0.1",
    author="Avnish Singh",
    author_email="chauhanavnish8587@gmail.com",
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()


)