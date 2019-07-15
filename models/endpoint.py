#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Endpoint) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import coding
from . import contactpoint
from . import domainresource
from . import fhirreference
from . import identifier
from . import period

from . import domainresource

@dataclass
class Endpoint(domainresource.DomainResource):
    """ The technical details of an endpoint that can be used for electronic
    services.

    The technical details of an endpoint that can be used for electronic
    services, such as for web services providing XDS.b or a REST endpoint for
    another FHIR server. This may include any security context information.
    """
    resource_type: ClassVar[str] = "Endpoint"
    address: str = None
    connectionType:coding.Coding = None
    contact: Optional[List[contactpoint.ContactPoint]] = empty_list()
    header: Optional[List[str]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    managingOrganization: Optional[fhirreference.FHIRReference] = None
    name: Optional[str] = None
    payloadMimeType: Optional[List[str]] = empty_list()
    payloadType: List[codeableconcept.CodeableConcept] = empty_list()
    period: Optional[period.Period] = None
    status: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Endpoint, self).elementProperties()
        js.extend([
            ("address", "address", str, False, None, True),
            ("connectionType", "connectionType", coding.Coding, False, None, True),
            ("contact", "contact", contactpoint.ContactPoint, True, None, False),
            ("header", "header", str, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("name", "name", str, False, None, False),
            ("payloadMimeType", "payloadMimeType", str, True, None, False),
            ("payloadType", "payloadType", codeableconcept.CodeableConcept, True, None, True),
            ("period", "period", period.Period, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']