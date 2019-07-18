#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Appointment) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period

from . import backboneelement

@dataclass
class AppointmentParticipant(backboneelement.BackboneElement):
    """ Participants involved in appointment.

    List of participants involved in the appointment.
    """
    resource_type: ClassVar[str] = "AppointmentParticipant"
    actor: Optional[fhirreference.FHIRReference] = None
    period: Optional[period.Period] = None
    required: Optional[str] = None
    status: str = None
    type: Optional[List[codeableconcept.CodeableConcept]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(AppointmentParticipant, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("required", "required", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js

from . import domainresource

@dataclass
class Appointment(domainresource.DomainResource):
    """ A booking of a healthcare event among patient(s), practitioner(s), related
    person(s) and/or device(s) for a specific date/time. This may result in one
    or more Encounter(s).
    """
    resource_type: ClassVar[str] = "Appointment"
    appointmentType: Optional[codeableconcept.CodeableConcept] = None
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    cancelationReason: Optional[codeableconcept.CodeableConcept] = None
    comment: Optional[str] = None
    created: Optional[fhirdate.FHIRDate] = None
    description: Optional[str] = None
    end: Optional[fhirdate.FHIRDate] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    minutesDuration: Optional[int] = None
    participant: List[ AppointmentParticipant] = empty_list()
    patientInstruction: Optional[str] = None
    priority: Optional[int] = None
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    requestedPeriod: Optional[List[period.Period]] = empty_list()
    serviceCategory: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    serviceType: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    slot: Optional[List[fhirreference.FHIRReference]] = empty_list()
    specialty: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    start: Optional[fhirdate.FHIRDate] = None
    status: str = None
    supportingInformation: Optional[List[fhirreference.FHIRReference]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Appointment, self).elementProperties()
        js.extend([
            ("appointmentType", "appointmentType", codeableconcept.CodeableConcept, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("cancelationReason", "cancelationReason", codeableconcept.CodeableConcept, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("end", "end", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("minutesDuration", "minutesDuration", int, False, None, False),
            ("participant", "participant", AppointmentParticipant, True, None, True),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("priority", "priority", int, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("requestedPeriod", "requestedPeriod", period.Period, True, None, False),
            ("serviceCategory", "serviceCategory", codeableconcept.CodeableConcept, True, None, False),
            ("serviceType", "serviceType", codeableconcept.CodeableConcept, True, None, False),
            ("slot", "slot", fhirreference.FHIRReference, True, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("start", "start", fhirdate.FHIRDate, False, None, False),
            ("status", "status", str, False, None, True),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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