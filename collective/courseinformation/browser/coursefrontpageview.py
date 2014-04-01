from zope.interface import implements, Interface
from plone.memoize.view import memoize

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from collective.courseinformation import courseinformationMessageFactory as _


class ICourseFrontPageView(Interface):
    """
    CourseFrontPage view interface
    """

    def test():
        """ test method"""


class CourseFrontPageView(BrowserView):
    """
    CourseFrontPage browser view
    """
    implements(ICourseFrontPageView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    def test(self):
        """
        test method
        """
        dummy = _(u'a dummy string')

        return {'dummy': dummy}

    @memoize
    def courses(self):
        """ get the courses """
        limit = 7
        query = {}
        query["Type"] = "Course"
        query["review_state"] = "published"
        query["sort_on"] = "start"
        query["sort_limit"] = limit
        # Return brain objects for instructors
        courses = self.portal_catalog.searchResults(**query)[:limit]
        return courses 
