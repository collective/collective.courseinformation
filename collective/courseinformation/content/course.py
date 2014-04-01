"""Definition of the Course content type
"""

from zope.interface import implements, directlyProvides
from AccessControl import ClassSecurityInfo

from Products.Archetypes import atapi
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from collective.courseinformation import courseinformationMessageFactory as _
from collective.courseinformation.interfaces import ICourse
from collective.courseinformation.config import PROJECTNAME

CourseSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.ReferenceField(
        'testimonial',
        storage=atapi.AnnotationStorage(),
        widget=ReferenceBrowserWidget(
            label=_(u"Testimonial"),
            description=_(u"Testimonials associated with this course"),
        ),
        relationship='course_testimonial',
        allowed_types=('Testimonial'), # specify portal type names here ('Example Type',)
        multiValued=True,
    ),


    atapi.ReferenceField(
        'instructor',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ReferenceWidget(
            label=_(u"Instructor"),
            description=_(u"The course instructor"),
        ),
        relationship='course_instructor',
        allowed_types=('Instructor',), # specify portal type names here ('Example Type',)
        multiValued=False,
    ),


    atapi.FixedPointField(
        'price_jm',
        storage=atapi.AnnotationStorage(),
        widget=atapi.DecimalWidget(
            label=_(u"Price JMD"),
            description=_(u"Price in Jamaican Dollars"),
            dollars_and_cents=True,
            size=10,
            thousands_commas=True,
        ),
        required=True,
        validators=('isDecimal'),
    ),


    atapi.FixedPointField(
        'price_us',
        storage=atapi.AnnotationStorage(),
        widget=atapi.DecimalWidget(
            label=_(u"Price - USD"),
            description=_(u"Price in USD"),
            dollars_and_cents=True,
            size=10,
            thousands_commas=True,
        ),
        required=True,
        validators=('isDecimal'),
    ),

    atapi.DateTimeField( 'startDate',
        storage=atapi.AnnotationStorage(),
        accessor='start',
        widget=atapi.CalendarWidget(
            label=_(u"Starting Date"),
            description=_(u"The starting date"),
            show_hm = 0,
            future_years = 3,
            starting_year = 2007,
            format = '%B %d, %Y',
        ),
        required=True,
        validators=('isValidDate'),
    ),


    atapi.DateTimeField(
        'endDate',
        storage=atapi.AnnotationStorage(),
        accessor='end',
        widget=atapi.CalendarWidget(
            label=_(u"Ending Date"),
            description=_(u"Ending date for the course"),
            show_hm = 0,
            future_years = 3,
            starting_year = 2007,
            format = '%B %d, %Y',
        ),
        required=True,
        validators=('isValidDate'),
    ),


    atapi.TextField(
        'schedule',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"Schedule and Additional Information"),
            description=_(u"Schedule and other course information"),
        ),
        required=True,
        default_output_type = "text/html",
        default_content_type="text/html",
    ),

    atapi.StringField(
        'time',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            populate=1,
            label=_(u"Time"),
            description=_(u"Times for the course"),
        ),
        required=False,
    ),

    atapi.StringField(
        'hours',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            populate=1,
            label=_(u"Hours"),
            description=_(u"Hours for the course"),
        ),
        required=False,
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

CourseSchema['title'].storage = atapi.AnnotationStorage()
CourseSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(CourseSchema, moveDiscussion=False)

class Course(base.ATCTContent):
    """A Course Description"""
    implements(ICourse)

    meta_type = "Course"
    schema = CourseSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    testimonial = atapi.ATReferenceFieldProperty('testimonial')

    instructor = atapi.ATReferenceFieldProperty('instructor')

    price_jm = atapi.ATFieldProperty('price_jm')

    price_us = atapi.ATFieldProperty('price_us')

    endDate = atapi.ATFieldProperty('endDate')

    startDate = atapi.ATFieldProperty('startDate')

    schedule = atapi.ATFieldProperty('schedule')

    hours = atapi.ATFieldProperty('hours')

    time = atapi.ATFieldProperty('time')

    security = ClassSecurityInfo()

    VIEW_CONTENTS_PERMISSION = 'View'

    #security.declareProtected(VIEW_CONTENTS_PERMISSION, 'start')
    def start(self):
        "Same as start() method"
        start = getattr(self.aq_base, 'startDate', None)
        return start



    #security.declareProtected(VIEW_CONTENTS_PERMISSION, 'end')
    def end(self):
        "Same as start() method"
        end = getattr(self.aq_base, 'endDate', None)
        return end




atapi.registerType(Course, PROJECTNAME)
