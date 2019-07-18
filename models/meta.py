#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Meta) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import coding
from . import element
from . import fhirdate

from . import element

@dataclass
class Meta(element.Element):
    """ Metadata about a resource.

    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content might not always
    be associated with version changes to the resource.
    """
    resource_type: ClassVar[str] = "Meta"
    lastUpdated: Optional[fhirdate.FHIRDate] = None
    profile: Optional[List[str]] = empty_list()
    security: Optional[List[coding.Coding]] = empty_list()
    source: Optional[str] = None
    tag: Optional[List[coding.Coding]] = empty_list()
    versionId: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Meta, self).elementProperties()
        js.extend([
            ("lastUpdated", "lastUpdated", fhirdate.FHIRDate, False, None, False),
            ("profile", "profile", str, True, None, False),
            ("security", "security", coding.Coding, True, None, False),
            ("source", "source", str, False, None, False),
            ("tag", "tag", coding.Coding, True, None, False),
            ("versionId", "versionId", str, False, None, False),
        ])
        return js


import sys
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']