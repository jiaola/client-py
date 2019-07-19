#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Appointment) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class AppointmentParticipant(BackboneElement):
    """ Participants involved in appointment.

    List of participants involved in the appointment.
    """
    resource_type: ClassVar[str] = "AppointmentParticipant"
    actor: Optional[FHIRReference] = None
    period: Optional[Period] = None
    required: Optional[str] = None
    status: str = None
    type: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(AppointmentParticipant, self).elementProperties()
        js.extend([
            ("actor", "actor", FHIRReference, False, None, False),
            ("period", "period", Period, False, None, False),
            ("required", "required", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("type", "type", CodeableConcept, True, None, False),
        ])
        return js


@dataclass
class Appointment(DomainResource):
    """ A booking of a healthcare event among patient(s), practitioner(s), related
    person(s) and/or device(s) for a specific date/time. This may result in one
    or more Encounter(s).
    """
    resource_type: ClassVar[str] = "Appointment"
    appointmentType: Optional[CodeableConcept] = None
    basedOn: Optional[List[FHIRReference]] = empty_list()
    cancelationReason: Optional[CodeableConcept] = None
    comment: Optional[str] = None
    created: Optional[FHIRDate] = None
    description: Optional[str] = None
    end: Optional[FHIRDate] = None
    identifier: Optional[List[Identifier]] = empty_list()
    minutesDuration: Optional[int] = None
    participant: List[AppointmentParticipant] = empty_list()
    patientInstruction: Optional[str] = None
    priority: Optional[int] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    requestedPeriod: Optional[List[Period]] = empty_list()
    serviceCategory: Optional[List[CodeableConcept]] = empty_list()
    serviceType: Optional[List[CodeableConcept]] = empty_list()
    slot: Optional[List[FHIRReference]] = empty_list()
    specialty: Optional[List[CodeableConcept]] = empty_list()
    start: Optional[FHIRDate] = None
    status: str = None
    supportingInformation: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(Appointment, self).elementProperties()
        js.extend([
            ("appointmentType", "appointmentType", CodeableConcept, False, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("cancelationReason", "cancelationReason", CodeableConcept, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("created", "created", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("end", "end", FHIRDate, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("minutesDuration", "minutesDuration", int, False, None, False),
            ("participant", "participant", AppointmentParticipant, True, None, True),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("priority", "priority", int, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("requestedPeriod", "requestedPeriod", Period, True, None, False),
            ("serviceCategory", "serviceCategory", CodeableConcept, True, None, False),
            ("serviceType", "serviceType", CodeableConcept, True, None, False),
            ("slot", "slot", FHIRReference, True, None, False),
            ("specialty", "specialty", CodeableConcept, True, None, False),
            ("start", "start", FHIRDate, False, None, False),
            ("status", "status", str, False, None, True),
            ("supportingInformation", "supportingInformation", FHIRReference, True, None, False),
        ])
        return js