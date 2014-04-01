from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from collective.courseinformation import courseinformationMessageFactory as _

class ICourse(Interface):
    """A Short Course Description"""
    
    # -*- schema definition goes here -*-
