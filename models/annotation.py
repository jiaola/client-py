#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Annotation) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import element
from . import fhirdate
from . import fhirreference


from . import element

@dataclass
class Annotation(element.Element):
    """ Text node with attribution.

    A  text note which also  contains information about who made the statement
    and when.
    """
    resource_type: ClassVar[str] = "Annotation"
    authorReference: Optional[fhirreference.FHIRReference] = None
    authorString: Optional[str] = None
    text: str = None
    time: Optional[fhirdate.FHIRDate] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.authorReference = None
#        """ Individual responsible for the annotation.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.authorString = None
#        """ Individual responsible for the annotation.
#        Type `str`
#
#. """
#
#
#        self.text = None
#        """ The annotation  - text content (as markdown).
#        Type `str`
#
#. """
#
#
#        self.time = None
#        """ When the annotation was made.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#

#        super(Annotation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Annotation, self).elementProperties()
        js.extend([
            ("authorReference", "authorReference", fhirreference.FHIRReference, {  # #}False, "author", {  # #}False),
            ("authorString", "authorString", str, {  # #}False, "author", {  # #}False),
            ("text", "text", str, {  # #}False, None, {  # #}True),
            ("time", "time", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
        ])
        return js