#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Annotation) on 2019-07-15.
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

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Annotation, self).elementProperties()
        js.extend([
            ("authorReference", "authorReference", fhirreference.FHIRReference, False, "author", False),
            ("authorString", "authorString", str, False, "author", False),
            ("text", "text", str, False, None, True),
            ("time", "time", fhirdate.FHIRDate, False, None, False),
        ])
        return js


import sys
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']