from zope.interface import implements, Interface
from plone.memoize.view import memoize

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from collective.courseinformation import courseinformationMessageFactory as _


class Icourse_summaryView(Interface):
    """
    course_summary view interface
    """

    def test():
        """ test method"""


class course_summaryView(BrowserView):
    """
    course_summary browser view
    """
    implements(Icourse_summaryView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    @property
    def workflowtool(self):
        return getToolByName(self.context, "portal_workflow")                

    @memoize
    def instructor(self):
        """ get the instructor """
        # there is only one instructor
        instructors = self.context.getRefs(relationship="course_instructor") 
        if len(instructors) > 0:
            state = self.workflowtool.getStatusOf("simple_publication_workflow",instructors[0])['review_state']
            if state == 'published':
                return instructors[0]
        return None

    @memoize
    def instructor_has_image(self):
        """ check if instructor has an image """
        return len(self.instructor().getImage()) > 0

    @memoize
    def testimonials(self):
        """ get testimonials abaout this course """
        testimonials = self.context.getRefs(relationship="course_testimonial") 
        return testimonials

    def test(self):
        """
        test method
        """
        dummy = _(u'a dummy string')

        return {'dummy': dummy}
