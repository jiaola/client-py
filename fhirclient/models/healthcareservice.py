#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/HealthcareService) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class HealthcareServiceNotAvailable(BackboneElement):
    """ Not available during this time due to provided reason.

    The HealthcareService is not available during this period of time due to
    the provided reason.
    """
    resource_type: ClassVar[str] = "HealthcareServiceNotAvailable"
    description: str = None
    during: Optional[Period] = None

    def elementProperties(self):
        js = super(HealthcareServiceNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("during", "during", Period, False, None, False),
        ])
        return js


@dataclass
class HealthcareServiceEligibility(BackboneElement):
    """ Specific eligibility requirements required to use the service.

    Does this service have specific eligibility requirements that need to be
    met in order to use the service?
    """
    resource_type: ClassVar[str] = "HealthcareServiceEligibility"
    code: Optional[CodeableConcept] = None
    comment: Optional[str] = None

    def elementProperties(self):
        js = super(HealthcareServiceEligibility, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, False),
            ("comment", "comment", str, False, None, False),
        ])
        return js


@dataclass
class HealthcareServiceAvailableTime(BackboneElement):
    """ Times the Service Site is available.

    A collection of times that the Service Site is available.
    """
    resource_type: ClassVar[str] = "HealthcareServiceAvailableTime"
    allDay: Optional[bool] = None
    availableEndTime: Optional[FHIRDate] = None
    availableStartTime: Optional[FHIRDate] = None
    daysOfWeek: Optional[List[str]] = empty_list()

    def elementProperties(self):
        js = super(HealthcareServiceAvailableTime, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, False, None, False),
            ("availableEndTime", "availableEndTime", FHIRDate, False, None, False),
            ("availableStartTime", "availableStartTime", FHIRDate, False, None, False),
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
        ])
        return js


@dataclass
class HealthcareService(DomainResource):
    """ The details of a healthcare service available at a location.
    """
    resource_type: ClassVar[str] = "HealthcareService"
    active: Optional[bool] = None
    appointmentRequired: Optional[bool] = None
    availabilityExceptions: Optional[str] = None
    availableTime: Optional[List[HealthcareServiceAvailableTime]] = empty_list()
    category: Optional[List[CodeableConcept]] = empty_list()
    characteristic: Optional[List[CodeableConcept]] = empty_list()
    comment: Optional[str] = None
    communication: Optional[List[CodeableConcept]] = empty_list()
    coverageArea: Optional[List[FHIRReference]] = empty_list()
    eligibility: Optional[List[HealthcareServiceEligibility]] = empty_list()
    endpoint: Optional[List[FHIRReference]] = empty_list()
    extraDetails: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    location: Optional[List[FHIRReference]] = empty_list()
    name: Optional[str] = None
    notAvailable: Optional[List[HealthcareServiceNotAvailable]] = empty_list()
    photo: Optional[Attachment] = None
    program: Optional[List[CodeableConcept]] = empty_list()
    providedBy: Optional[FHIRReference] = None
    referralMethod: Optional[List[CodeableConcept]] = empty_list()
    serviceProvisionCode: Optional[List[CodeableConcept]] = empty_list()
    specialty: Optional[List[CodeableConcept]] = empty_list()
    telecom: Optional[List[ContactPoint]] = empty_list()
    type: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(HealthcareService, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("appointmentRequired", "appointmentRequired", bool, False, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("availableTime", "availableTime", HealthcareServiceAvailableTime, True, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("characteristic", "characteristic", CodeableConcept, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("communication", "communication", CodeableConcept, True, None, False),
            ("coverageArea", "coverageArea", FHIRReference, True, None, False),
            ("eligibility", "eligibility", HealthcareServiceEligibility, True, None, False),
            ("endpoint", "endpoint", FHIRReference, True, None, False),
            ("extraDetails", "extraDetails", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("location", "location", FHIRReference, True, None, False),
            ("name", "name", str, False, None, False),
            ("notAvailable", "notAvailable", HealthcareServiceNotAvailable, True, None, False),
            ("photo", "photo", Attachment, False, None, False),
            ("program", "program", CodeableConcept, True, None, False),
            ("providedBy", "providedBy", FHIRReference, False, None, False),
            ("referralMethod", "referralMethod", CodeableConcept, True, None, False),
            ("serviceProvisionCode", "serviceProvisionCode", CodeableConcept, True, None, False),
            ("specialty", "specialty", CodeableConcept, True, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
            ("type", "type", CodeableConcept, True, None, False),
        ])
        return js