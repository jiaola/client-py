#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/EnrollmentRequest) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier

from . import domainresource

@dataclass
class EnrollmentRequest(domainresource.DomainResource):
    """ Enroll in coverage.

    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """
    resource_type: ClassVar[str] = "EnrollmentRequest"
    candidate: Optional[fhirreference.FHIRReference] = None
    coverage: Optional[fhirreference.FHIRReference] = None
    created: Optional[fhirdate.FHIRDate] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    insurer: Optional[fhirreference.FHIRReference] = None
    provider: Optional[fhirreference.FHIRReference] = None
    status: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(EnrollmentRequest, self).elementProperties()
        js.extend([
            ("candidate", "candidate", fhirreference.FHIRReference, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
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
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']