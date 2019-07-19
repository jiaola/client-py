#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Slot) on 2019-07-18.
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
class Slot(DomainResource):
    """ A slot of time on a schedule that may be available for booking appointments.
    """
    resource_type: ClassVar[str] = "Slot"
    appointmentType: Optional[CodeableConcept] = None
    comment: Optional[str] = None
    end: FHIRDate = None
    identifier: Optional[List[Identifier]] = empty_list()
    overbooked: Optional[bool] = None
    schedule: FHIRReference = None
    serviceCategory: Optional[List[CodeableConcept]] = empty_list()
    serviceType: Optional[List[CodeableConcept]] = empty_list()
    specialty: Optional[List[CodeableConcept]] = empty_list()
    start: FHIRDate = None
    status: str = None

    def elementProperties(self):
        js = super(Slot, self).elementProperties()
        js.extend([
            ("appointmentType", "appointmentType", CodeableConcept, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("end", "end", FHIRDate, False, None, True),
            ("identifier", "identifier", Identifier, True, None, False),
            ("overbooked", "overbooked", bool, False, None, False),
            ("schedule", "schedule", FHIRReference, False, None, True),
            ("serviceCategory", "serviceCategory", CodeableConcept, True, None, False),
            ("serviceType", "serviceType", CodeableConcept, True, None, False),
            ("specialty", "specialty", CodeableConcept, True, None, False),
            ("start", "start", FHIRDate, False, None, True),
            ("status", "status", str, False, None, True),
        ])
        return js