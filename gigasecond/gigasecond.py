""" Exercism awnser"""
import datetime


def add(moment):
    """ Adds a gigasecond """
    return moment + datetime.timedelta(0, pow(10, 9))
