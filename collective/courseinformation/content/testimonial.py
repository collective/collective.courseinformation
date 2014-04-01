"""Definition of the Testimonial content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from collective.courseinformation import courseinformationMessageFactory as _
from collective.courseinformation.interfaces import ITestimonial
from collective.courseinformation.config import PROJECTNAME

TestimonialSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.ImageField(
        'image',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Picture"),
            description=_(u"picture associated with testimonial"),
        ),
         max_size=(700,550),
         sizes={ 'thumb' : (64,64), 
                    'preview' : (200,200), 
                    'medium' : (300,300), 
                    'large' : (500,500)},
          

        validators=('isNonEmptyFile'),
    ),


    atapi.TextField(
        'story',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"Story"),
            description=_(u"The story for this testimonial"),
        ),
        required=True,
        default_output_type = "text/html",
        default_content_type="text/html",
    ),


    atapi.StringField(
        'person',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Person or Group"),
            description=_(u"The person or group who submitted the testimonial"),
        ),
        required=False,
    ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

TestimonialSchema['title'].storage = atapi.AnnotationStorage()
TestimonialSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(TestimonialSchema, moveDiscussion=False)

class Testimonial(base.ATCTContent):
    """A testimonial with optional picture"""
    implements(ITestimonial)

    meta_type = "Testimonial"
    schema = TestimonialSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    image = atapi.ATFieldProperty('image')

    story = atapi.ATFieldProperty('story')

    person = atapi.ATFieldProperty('person')


atapi.registerType(Testimonial, PROJECTNAME)
