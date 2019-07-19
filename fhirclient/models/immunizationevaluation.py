#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation) on 2019-07-18.
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
class ImmunizationEvaluation(DomainResource):
    """ Immunization evaluation information.

    Describes a comparison of an immunization event against published
    recommendations to determine if the administration is "valid" in relation
    to those  recommendations.
    """
    resource_type: ClassVar[str] = "ImmunizationEvaluation"
    authority: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    description: Optional[str] = None
    doseNumberPositiveInt: Optional[int] = None
    doseNumberString: Optional[str] = None
    doseStatus: CodeableConcept = None
    doseStatusReason: Optional[List[CodeableConcept]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    immunizationEvent: FHIRReference = None
    patient: FHIRReference = None
    series: Optional[str] = None
    seriesDosesPositiveInt: Optional[int] = None
    seriesDosesString: Optional[str] = None
    status: str = None
    targetDisease: CodeableConcept = None

    def elementProperties(self):
        js = super(ImmunizationEvaluation, self).elementProperties()
        js.extend([
            ("authority", "authority", FHIRReference, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", False),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", False),
            ("doseStatus", "doseStatus", CodeableConcept, False, None, True),
            ("doseStatusReason", "doseStatusReason", CodeableConcept, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("immunizationEvent", "immunizationEvent", FHIRReference, False, None, True),
            ("patient", "patient", FHIRReference, False, None, True),
            ("series", "series", str, False, None, False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
            ("status", "status", str, False, None, True),
            ("targetDisease", "targetDisease", CodeableConcept, False, None, True),
        ])
        return js