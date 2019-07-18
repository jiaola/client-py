#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/PractitionerRole) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period

from . import backboneelement

@dataclass
class PractitionerRoleNotAvailable(backboneelement.BackboneElement):
    """ Not available during this time due to provided reason.

    The practitioner is not available or performing this role during this
    period of time due to the provided reason.
    """
    resource_type: ClassVar[str] = "PractitionerRoleNotAvailable"
    description: str = None
    during: Optional[period.Period] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(PractitionerRoleNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("during", "during", period.Period, False, None, False),
        ])
        return js

@dataclass
class PractitionerRoleAvailableTime(backboneelement.BackboneElement):
    """ Times the Service Site is available.

    A collection of times the practitioner is available or performing this role
    at the location and/or healthcareservice.
    """
    resource_type: ClassVar[str] = "PractitionerRoleAvailableTime"
    allDay: Optional[bool] = None
    availableEndTime: Optional[fhirdate.FHIRDate] = None
    availableStartTime: Optional[fhirdate.FHIRDate] = None
    daysOfWeek: Optional[List[str]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(PractitionerRoleAvailableTime, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, False, None, False),
            ("availableEndTime", "availableEndTime", fhirdate.FHIRDate, False, None, False),
            ("availableStartTime", "availableStartTime", fhirdate.FHIRDate, False, None, False),
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
        ])
        return js

from . import domainresource

@dataclass
class PractitionerRole(domainresource.DomainResource):
    """ Roles/organizations the practitioner is associated with.

    A specific set of Roles/Locations/specialties/services that a practitioner
    may perform at an organization for a period of time.
    """
    resource_type: ClassVar[str] = "PractitionerRole"
    active: Optional[bool] = None
    availabilityExceptions: Optional[str] = None
    availableTime: Optional[List[PractitionerRoleAvailableTime]] = empty_list()
    code: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    endpoint: Optional[List[fhirreference.FHIRReference]] = empty_list()
    healthcareService: Optional[List[fhirreference.FHIRReference]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    location: Optional[List[fhirreference.FHIRReference]] = empty_list()
    notAvailable: Optional[List[PractitionerRoleNotAvailable]] = empty_list()
    organization: Optional[fhirreference.FHIRReference] = None
    period: Optional[period.Period] = None
    practitioner: Optional[fhirreference.FHIRReference] = None
    specialty: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    telecom: Optional[List[contactpoint.ContactPoint]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(PractitionerRole, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("availableTime", "availableTime", PractitionerRoleAvailableTime, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("healthcareService", "healthcareService", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, True, None, False),
            ("notAvailable", "notAvailable", PractitionerRoleNotAvailable, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("practitioner", "practitioner", fhirreference.FHIRReference, False, None, False),
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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']