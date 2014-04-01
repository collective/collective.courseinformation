from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from collective.courseinformation import courseinformationMessageFactory as _

class ITestimonial(Interface):
    """Feedback regarding a Course"""
    
    # -*- schema definition goes here -*-
