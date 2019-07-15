#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/OrganizationAffiliation) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import contactpoint
from . import domainresource
from . import fhirreference
from . import identifier
from . import period

from . import domainresource

@dataclass
class OrganizationAffiliation(domainresource.DomainResource):
    """ Defines an affiliation/assotiation/relationship between 2 distinct
    oganizations, that is not a part-of relationship/sub-division relationship.
    """
    resource_type: ClassVar[str] = "OrganizationAffiliation"
    active: Optional[bool] = None
    code: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    endpoint: Optional[List[fhirreference.FHIRReference]] = empty_list()
    healthcareService: Optional[List[fhirreference.FHIRReference]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    location: Optional[List[fhirreference.FHIRReference]] = empty_list()
    network: Optional[List[fhirreference.FHIRReference]] = empty_list()
    organization: Optional[fhirreference.FHIRReference] = None
    participatingOrganization: Optional[fhirreference.FHIRReference] = None
    period: Optional[period.Period] = None
    specialty: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    telecom: Optional[List[contactpoint.ContactPoint]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(OrganizationAffiliation, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("healthcareService", "healthcareService", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, True, None, False),
            ("network", "network", fhirreference.FHIRReference, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("participatingOrganization", "participatingOrganization", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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