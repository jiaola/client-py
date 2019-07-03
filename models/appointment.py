#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Appointment) on 2019-07-03.
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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.appointmentType = None
#        """ The style of appointment or patient that has been booked in the
        slot (not service type).
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.basedOn = None
#        """ The service request this appointment is allocated to assess.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.cancelationReason = None
#        """ The coded reason for the appointment being cancelled.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.comment = None
#        """ Additional comments.
#        Type `str`
#
#. """
#
#
#        self.created = None
#        """ The date that this appointment was initially created.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.description = None
#        """ Shown on a subject line in a meeting request, or appointment list.
#        Type `str`
#
#. """
#
#
#        self.end = None
#        """ When appointment is to conclude.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.identifier = None
#        """ External Ids for this item.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.minutesDuration = None
#        """ Can be less than start/end (e.g. estimate).
#        Type `int`
#
#. """
#
#
#        self.participant = None
#        """ Participants involved in appointment.
#        List of `AppointmentParticipant` items
#
# (represented as `dict` in JSON). """
#
#
#        self.patientInstruction = None
#        """ Detailed information and instructions for the patient.
#        Type `str`
#
#. """
#
#
#        self.priority = None
#        """ Used to make informed decisions if needing to re-prioritize.
#        Type `int`
#
#. """
#
#
#        self.reasonCode = None
#        """ Coded reason this appointment is scheduled.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.reasonReference = None
#        """ Reason the appointment is to take place (resource).
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.requestedPeriod = None
#        """ Potential date/time interval(s) requested to allocate the
        appointment within.
#        List of `Period` items
#
# (represented as `dict` in JSON). """
#
#
#        self.serviceCategory = None
#        """ A broad categorization of the service that is to be performed
        during this appointment.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.serviceType = None
#        """ The specific service that is to be performed during this
        appointment.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.slot = None
#        """ The slots that this appointment is filling.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.specialty = None
#        """ The specialty of a practitioner that would be required to perform
        the service requested in this appointment.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.start = None
#        """ When appointment is to take place.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.status = None
#        """ proposed | pending | booked | arrived | fulfilled | cancelled |
        noshow | entered-in-error | checked-in | waitlist.
#        Type `str`
#
#. """
#
#
#        self.supportingInformation = None
#        """ Additional information to support the appointment.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#

#        super(Appointment, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Appointment, self).elementProperties()
        js.extend([
            ("appointmentType", "appointmentType", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("cancelationReason", "cancelationReason", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("comment", "comment", str, {  # #}False, None, {  # #}False),
            ("created", "created", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("end", "end", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("minutesDuration", "minutesDuration", int, {  # #}False, None, {  # #}False),
            ("participant", "participant", AppointmentParticipant, {  # #}True, None, {  # #}True),
            ("patientInstruction", "patientInstruction", str, {  # #}False, None, {  # #}False),
            ("priority", "priority", int, {  # #}False, None, {  # #}False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("requestedPeriod", "requestedPeriod", period.Period, {  # #}True, None, {  # #}False),
            ("serviceCategory", "serviceCategory", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("serviceType", "serviceType", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("slot", "slot", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("start", "start", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.actor = None
#        """ Person, Location/HealthcareService or Device.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.period = None
#        """ Participation period of the actor.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.required = None
#        """ required | optional | information-only.
#        Type `str`
#
#. """
#
#
#        self.status = None
#        """ accepted | declined | tentative | needs-action.
#        Type `str`
#
#. """
#
#
#        self.type = None
#        """ Role of participant in the appointment.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#

#        super(AppointmentParticipant, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AppointmentParticipant, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("period", "period", period.Period, {  # #}False, None, {  # #}False),
            ("required", "required", str, {  # #}False, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
        ])
        return js