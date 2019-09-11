#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Lista Asistencia",
    version="0.0.1",
    author="Raul de Arriba",
    author_email="rauldearriba@gmail.com",
    description="Bot para pasar lista de un grupo.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Radega1993/ListaAsistencia_bot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
