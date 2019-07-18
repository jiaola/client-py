#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/BodyStructure) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import codeableconcept
from . import domainresource
from . import fhirreference
from . import identifier

from . import domainresource

@dataclass
class BodyStructure(domainresource.DomainResource):
    """ Specific and identified anatomical structure.

    Record details about an anatomical structure.  This resource may be used
    when a coded concept does not provide the necessary detail needed for the
    use case.
    """
    resource_type: ClassVar[str] = "BodyStructure"
    active: Optional[bool] = None
    description: Optional[str] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    image: Optional[List[attachment.Attachment]] = empty_list()
    location: Optional[codeableconcept.CodeableConcept] = None
    locationQualifier: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    morphology: Optional[codeableconcept.CodeableConcept] = None
    patient:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(BodyStructure, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("image", "image", attachment.Attachment, True, None, False),
            ("location", "location", codeableconcept.CodeableConcept, False, None, False),
            ("locationQualifier", "locationQualifier", codeableconcept.CodeableConcept, True, None, False),
            ("morphology", "morphology", codeableconcept.CodeableConcept, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']