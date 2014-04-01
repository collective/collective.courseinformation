"""Definition of the Instructor content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from collective.courseinformation import courseinformationMessageFactory as _
from collective.courseinformation.interfaces import IInstructor
from collective.courseinformation.config import PROJECTNAME

InstructorSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.TextField(
        'bio',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"Biography"),
            description=_(u"Instructor Biography"),
        ),
        required=True,
        default_output_type = "text/html",
        default_content_type="text/html",
    ),
    atapi.ImageField(
        'image',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Photo"),
            description=_(u"picture associated with instructor"),
        ),
         max_size=(700,550),
         sizes={ 'thumb' : (64,64), 
                    'preview' : (200,200), 
                    'medium' : (300,300), 
                    'large' : (500,500)},
        validators=('isNonEmptyFile'),
    ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

InstructorSchema['title'].storage = atapi.AnnotationStorage()
InstructorSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(InstructorSchema, moveDiscussion=False)

class Instructor(base.ATCTContent):
    """A profile of an instructor"""
    implements(IInstructor)

    meta_type = "Instructor"
    schema = InstructorSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    bio = atapi.ATFieldProperty('bio')


atapi.registerType(Instructor, PROJECTNAME)
