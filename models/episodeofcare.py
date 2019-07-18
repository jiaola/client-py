#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/EpisodeOfCare) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirreference
from . import identifier
from . import period

from . import backboneelement

@dataclass
class EpisodeOfCareStatusHistory(backboneelement.BackboneElement):
    """ Past list of status codes (the current status may be included to cover the
    start date of the status).

    The history of statuses that the EpisodeOfCare has been through (without
    requiring processing the history of the resource).
    """
    resource_type: ClassVar[str] = "EpisodeOfCareStatusHistory"
    period:period.Period = None
    status: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(EpisodeOfCareStatusHistory, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, True),
            ("status", "status", str, False, None, True),
        ])
        return js

@dataclass
class EpisodeOfCareDiagnosis(backboneelement.BackboneElement):
    """ The list of diagnosis relevant to this episode of care.
    """
    resource_type: ClassVar[str] = "EpisodeOfCareDiagnosis"
    condition:fhirreference.FHIRReference = None
    rank: Optional[int] = None
    role: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(EpisodeOfCareDiagnosis, self).elementProperties()
        js.extend([
            ("condition", "condition", fhirreference.FHIRReference, False, None, True),
            ("rank", "rank", int, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

from . import domainresource

@dataclass
class EpisodeOfCare(domainresource.DomainResource):
    """ An association of a Patient with an Organization and  Healthcare
    Provider(s) for a period of time that the Organization assumes some level
    of responsibility.

    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during this
    time.
    """
    resource_type: ClassVar[str] = "EpisodeOfCare"
    account: Optional[List[fhirreference.FHIRReference]] = empty_list()
    careManager: Optional[fhirreference.FHIRReference] = None
    diagnosis: Optional[List[EpisodeOfCareDiagnosis]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    managingOrganization: Optional[fhirreference.FHIRReference] = None
    patient:fhirreference.FHIRReference = None
    period: Optional[period.Period] = None
    referralRequest: Optional[List[fhirreference.FHIRReference]] = empty_list()
    status: str = None
    statusHistory: Optional[List[EpisodeOfCareStatusHistory]] = empty_list()
    team: Optional[List[fhirreference.FHIRReference]] = empty_list()
    type: Optional[List[codeableconcept.CodeableConcept]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(EpisodeOfCare, self).elementProperties()
        js.extend([
            ("account", "account", fhirreference.FHIRReference, True, None, False),
            ("careManager", "careManager", fhirreference.FHIRReference, False, None, False),
            ("diagnosis", "diagnosis", EpisodeOfCareDiagnosis, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("period", "period", period.Period, False, None, False),
            ("referralRequest", "referralRequest", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusHistory", "statusHistory", EpisodeOfCareStatusHistory, True, None, False),
            ("team", "team", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


import sys
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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']