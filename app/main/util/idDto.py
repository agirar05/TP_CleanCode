"""idDto.py: Dto to generate doc at the endpoint"""
__author__ = "Girard Alexandre"

from flask_restx import Namespace


class IDDto:
    api = Namespace('id', description='id related operations')
