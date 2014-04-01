from zope.interface import implements, Interface
from plone.memoize.view import memoize

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from collective.courseinformation import courseinformationMessageFactory as _


class Iinstructor_listing(Interface):
    """
    instructor_listing interface
    """

    def test():
        """ test method"""


class methods(BrowserView):
    """
    instructor_listing browser view
    """
    implements(Iinstructor_listing)

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
    def instructors(self):
        """ get the instructors """
        query = {}
        query["Type"] = "Instructor"
        query["review_state"] = "published"
        # Return brain objects for instructors
        instructors = self.portal_catalog.searchResults(**query)
        return instructors

    @memoize
    def testimonials(self):
        """ get testimonials abaout this course """
        query = {}
        query["Type"] = "Testimonial"
        # Return brain objects for testimonial
        testimonials = self.portal_catalog.searchResults(**query)
        return testimonials

    @memoize
    def instructor_courses(self,instructor):
        """ get instructor courses """
        courses = instructor.getObject().getBRefs()
        return courses

