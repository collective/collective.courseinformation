from zope.interface import implements, Interface
from plone.memoize.view import memoize

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from collective.courseinformation import courseinformationMessageFactory as _


class Iinstructor_view(Interface):
    """
    instructor_view interface
    """

    def test():
        """ test method"""


class methods(BrowserView):
    """
    instructor_view browser view
    """
    implements(Iinstructor_view)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    @memoize
    def instructor_courses(self):
        """ get instructor courses """
        courses = self.context.getBRefs(relationship="course_instructor")
        return courses

    @memoize
    def instructor_has_image(self):
        """ get instructor courses """
        return len(self.context.getImage()) > 0


