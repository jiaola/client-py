#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Schedule) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class Schedule(DomainResource):
    """ A container for slots of time that may be available for booking
    appointments.
    """
    resource_type: ClassVar[str] = "Schedule"
    active: Optional[bool] = None
    actor: List[FHIRReference] = empty_list()
    comment: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    planningHorizon: Optional[Period] = None
    serviceCategory: Optional[List[CodeableConcept]] = empty_list()
    serviceType: Optional[List[CodeableConcept]] = empty_list()
    specialty: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(Schedule, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("actor", "actor", FHIRReference, True, None, True),
            ("comment", "comment", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("planningHorizon", "planningHorizon", Period, False, None, False),
            ("serviceCategory", "serviceCategory", CodeableConcept, True, None, False),
            ("serviceType", "serviceType", CodeableConcept, True, None, False),
            ("specialty", "specialty", CodeableConcept, True, None, False),
        ])
        return js