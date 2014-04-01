from zope.interface import implements, Interface
from plone.memoize.view import memoize

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from collective.courseinformation import courseinformationMessageFactory as _


class Icourse_listing(Interface):
    """
    course_listing interface
    """

    def test():
        """ test method"""


class methods(BrowserView):
    """
    course_listing browser view
    """
    implements(Icourse_listing)

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
    def courses(self):
        """ get the courses """
        query = {}
        query["Type"] = "Course"
        query["review_state"] = "published"
        # Return brain objects for instructors
        courses = self.portal_catalog.searchResults(**query)
        return courses 

    @memoize
    def course_testimonials(self,course):
        """ get testimonials for course """
        testimonials = course.getObject().getRefs(relationship="course_testimonial")
        return testimonials 

    @memoize
    def course_instructors(self,course):
        """ get instructor courses """
        instructors = course.getObject().getRefs(relationship="course_instructor")
        return instructors

