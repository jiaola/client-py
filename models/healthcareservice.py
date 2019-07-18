#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/HealthcareService) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
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
class HealthcareServiceNotAvailable(backboneelement.BackboneElement):
    """ Not available during this time due to provided reason.

    The HealthcareService is not available during this period of time due to
    the provided reason.
    """
    resource_type: ClassVar[str] = "HealthcareServiceNotAvailable"
    description: str = None
    during: Optional[period.Period] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(HealthcareServiceNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("during", "during", period.Period, False, None, False),
        ])
        return js

@dataclass
class HealthcareServiceEligibility(backboneelement.BackboneElement):
    """ Specific eligibility requirements required to use the service.

    Does this service have specific eligibility requirements that need to be
    met in order to use the service?
    """
    resource_type: ClassVar[str] = "HealthcareServiceEligibility"
    code: Optional[codeableconcept.CodeableConcept] = None
    comment: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(HealthcareServiceEligibility, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("comment", "comment", str, False, None, False),
        ])
        return js

@dataclass
class HealthcareServiceAvailableTime(backboneelement.BackboneElement):
    """ Times the Service Site is available.

    A collection of times that the Service Site is available.
    """
    resource_type: ClassVar[str] = "HealthcareServiceAvailableTime"
    allDay: Optional[bool] = None
    availableEndTime: Optional[fhirdate.FHIRDate] = None
    availableStartTime: Optional[fhirdate.FHIRDate] = None
    daysOfWeek: Optional[List[str]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(HealthcareServiceAvailableTime, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, False, None, False),
            ("availableEndTime", "availableEndTime", fhirdate.FHIRDate, False, None, False),
            ("availableStartTime", "availableStartTime", fhirdate.FHIRDate, False, None, False),
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
        ])
        return js

from . import domainresource

@dataclass
class HealthcareService(domainresource.DomainResource):
    """ The details of a healthcare service available at a location.
    """
    resource_type: ClassVar[str] = "HealthcareService"
    active: Optional[bool] = None
    appointmentRequired: Optional[bool] = None
    availabilityExceptions: Optional[str] = None
    availableTime: Optional[List[HealthcareServiceAvailableTime]] = empty_list()
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    characteristic: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    comment: Optional[str] = None
    communication: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    coverageArea: Optional[List[fhirreference.FHIRReference]] = empty_list()
    eligibility: Optional[List[HealthcareServiceEligibility]] = empty_list()
    endpoint: Optional[List[fhirreference.FHIRReference]] = empty_list()
    extraDetails: Optional[str] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    location: Optional[List[fhirreference.FHIRReference]] = empty_list()
    name: Optional[str] = None
    notAvailable: Optional[List[HealthcareServiceNotAvailable]] = empty_list()
    photo: Optional[attachment.Attachment] = None
    program: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    providedBy: Optional[fhirreference.FHIRReference] = None
    referralMethod: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    serviceProvisionCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    specialty: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    telecom: Optional[List[contactpoint.ContactPoint]] = empty_list()
    type: Optional[List[codeableconcept.CodeableConcept]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(HealthcareService, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("appointmentRequired", "appointmentRequired", bool, False, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("availableTime", "availableTime", HealthcareServiceAvailableTime, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("characteristic", "characteristic", codeableconcept.CodeableConcept, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("communication", "communication", codeableconcept.CodeableConcept, True, None, False),
            ("coverageArea", "coverageArea", fhirreference.FHIRReference, True, None, False),
            ("eligibility", "eligibility", HealthcareServiceEligibility, True, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("extraDetails", "extraDetails", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, True, None, False),
            ("name", "name", str, False, None, False),
            ("notAvailable", "notAvailable", HealthcareServiceNotAvailable, True, None, False),
            ("photo", "photo", attachment.Attachment, False, None, False),
            ("program", "program", codeableconcept.CodeableConcept, True, None, False),
            ("providedBy", "providedBy", fhirreference.FHIRReference, False, None, False),
            ("referralMethod", "referralMethod", codeableconcept.CodeableConcept, True, None, False),
            ("serviceProvisionCode", "serviceProvisionCode", codeableconcept.CodeableConcept, True, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
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