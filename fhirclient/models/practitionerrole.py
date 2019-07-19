#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/PractitionerRole) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class PractitionerRoleNotAvailable(BackboneElement):
    """ Not available during this time due to provided reason.

    The practitioner is not available or performing this role during this
    period of time due to the provided reason.
    """
    resource_type: ClassVar[str] = "PractitionerRoleNotAvailable"
    description: str = None
    during: Optional[Period] = None

    def elementProperties(self):
        js = super(PractitionerRoleNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("during", "during", Period, False, None, False),
        ])
        return js


@dataclass
class PractitionerRoleAvailableTime(BackboneElement):
    """ Times the Service Site is available.

    A collection of times the practitioner is available or performing this role
    at the location and/or healthcareservice.
    """
    resource_type: ClassVar[str] = "PractitionerRoleAvailableTime"
    allDay: Optional[bool] = None
    availableEndTime: Optional[FHIRDate] = None
    availableStartTime: Optional[FHIRDate] = None
    daysOfWeek: Optional[List[str]] = empty_list()

    def elementProperties(self):
        js = super(PractitionerRoleAvailableTime, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, False, None, False),
            ("availableEndTime", "availableEndTime", FHIRDate, False, None, False),
            ("availableStartTime", "availableStartTime", FHIRDate, False, None, False),
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
        ])
        return js


@dataclass
class PractitionerRole(DomainResource):
    """ Roles/organizations the practitioner is associated with.

    A specific set of Roles/Locations/specialties/services that a practitioner
    may perform at an organization for a period of time.
    """
    resource_type: ClassVar[str] = "PractitionerRole"
    active: Optional[bool] = None
    availabilityExceptions: Optional[str] = None
    availableTime: Optional[List[PractitionerRoleAvailableTime]] = empty_list()
    code: Optional[List[CodeableConcept]] = empty_list()
    endpoint: Optional[List[FHIRReference]] = empty_list()
    healthcareService: Optional[List[FHIRReference]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    location: Optional[List[FHIRReference]] = empty_list()
    notAvailable: Optional[List[PractitionerRoleNotAvailable]] = empty_list()
    organization: Optional[FHIRReference] = None
    period: Optional[Period] = None
    practitioner: Optional[FHIRReference] = None
    specialty: Optional[List[CodeableConcept]] = empty_list()
    telecom: Optional[List[ContactPoint]] = empty_list()

    def elementProperties(self):
        js = super(PractitionerRole, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("availableTime", "availableTime", PractitionerRoleAvailableTime, True, None, False),
            ("code", "code", CodeableConcept, True, None, False),
            ("endpoint", "endpoint", FHIRReference, True, None, False),
            ("healthcareService", "healthcareService", FHIRReference, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("location", "location", FHIRReference, True, None, False),
            ("notAvailable", "notAvailable", PractitionerRoleNotAvailable, True, None, False),
            ("organization", "organization", FHIRReference, False, None, False),
            ("period", "period", Period, False, None, False),
            ("practitioner", "practitioner", FHIRReference, False, None, False),
            ("specialty", "specialty", CodeableConcept, True, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
        ])
        return js