#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/EnrollmentResponse) on 2019-07-15.
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
class EnrollmentResponse(domainresource.DomainResource):
    """ EnrollmentResponse resource.

    This resource provides enrollment and plan details from the processing of
    an EnrollmentRequest resource.
    """
    resource_type: ClassVar[str] = "EnrollmentResponse"
    created: Optional[fhirdate.FHIRDate] = None
    disposition: Optional[str] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    organization: Optional[fhirreference.FHIRReference] = None
    outcome: Optional[str] = None
    request: Optional[fhirreference.FHIRReference] = None
    requestProvider: Optional[fhirreference.FHIRReference] = None
    status: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(EnrollmentResponse, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False, None, False),
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