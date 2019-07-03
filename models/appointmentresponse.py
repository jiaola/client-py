#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/AppointmentResponse) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier


from . import domainresource

@dataclass
class AppointmentResponse(domainresource.DomainResource):
    """ A reply to an appointment request for a patient and/or practitioner(s),
    such as a confirmation or rejection.
    """
    resource_type: ClassVar[str] = "AppointmentResponse"
    actor: Optional[fhirreference.FHIRReference] = None
    appointment:fhirreference.FHIRReference = None
    comment: Optional[str] = None
    end: Optional[fhirdate.FHIRDate] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    participantStatus: str = None
    participantType: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    start: Optional[fhirdate.FHIRDate] = None

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
#        """ Person, Location, HealthcareService, or Device.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.appointment = None
#        """ Appointment this response relates to.
#        Type `FHIRReference`
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
#        self.end = None
#        """ Time from appointment, or requested new end time.
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
#        self.participantStatus = None
#        """ accepted | declined | tentative | in-process | completed | needs-
        action | entered-in-error.
#        Type `str`
#
#. """
#
#
#        self.participantType = None
#        """ Role of participant in the appointment.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.start = None
#        """ Time from appointment, or requested new start time.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#

#        super(AppointmentResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AppointmentResponse, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("appointment", "appointment", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("comment", "comment", str, {  # #}False, None, {  # #}False),
            ("end", "end", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("participantStatus", "participantStatus", str, {  # #}False, None, {  # #}True),
            ("participantType", "participantType", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("start", "start", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
        ])
        return js