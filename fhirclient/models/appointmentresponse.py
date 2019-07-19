#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/AppointmentResponse) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class AppointmentResponse(DomainResource):
    """ A reply to an appointment request for a patient and/or practitioner(s),
    such as a confirmation or rejection.
    """
    resource_type: ClassVar[str] = "AppointmentResponse"
    actor: Optional[FHIRReference] = None
    appointment: FHIRReference = None
    comment: Optional[str] = None
    end: Optional[FHIRDate] = None
    identifier: Optional[List[Identifier]] = empty_list()
    participantStatus: str = None
    participantType: Optional[List[CodeableConcept]] = empty_list()
    start: Optional[FHIRDate] = None

    def elementProperties(self):
        js = super(AppointmentResponse, self).elementProperties()
        js.extend([
            ("actor", "actor", FHIRReference, False, None, False),
            ("appointment", "appointment", FHIRReference, False, None, True),
            ("comment", "comment", str, False, None, False),
            ("end", "end", FHIRDate, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("participantStatus", "participantStatus", str, False, None, True),
            ("participantType", "participantType", CodeableConcept, True, None, False),
            ("start", "start", FHIRDate, False, None, False),
        ])
        return js