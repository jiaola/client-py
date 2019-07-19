#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Dosage) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .element import Element
from .quantity import Quantity
from .range import Range
from .ratio import Ratio
from .timing import Timing


@dataclass
class DosageDoseAndRate(Element):
    """ Amount of medication administered.

    The amount of medication administered.
    """
    resource_type: ClassVar[str] = "DosageDoseAndRate"
    doseQuantity: Optional[Quantity] = None
    doseRange: Optional[Range] = None
    rateQuantity: Optional[Quantity] = None
    rateRange: Optional[Range] = None
    rateRatio: Optional[Ratio] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(DosageDoseAndRate, self).elementProperties()
        js.extend([
            ("doseQuantity", "doseQuantity", Quantity, False, "dose", False),
            ("doseRange", "doseRange", Range, False, "dose", False),
            ("rateQuantity", "rateQuantity", Quantity, False, "rate", False),
            ("rateRange", "rateRange", Range, False, "rate", False),
            ("rateRatio", "rateRatio", Ratio, False, "rate", False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class Dosage(BackboneElement):
    """ How the medication is/was taken or should be taken.

    Indicates how the medication is/was taken or should be taken by the
    patient.
    """
    resource_type: ClassVar[str] = "Dosage"
    additionalInstruction: Optional[List[CodeableConcept]] = empty_list()
    asNeededBoolean: Optional[bool] = None
    asNeededCodeableConcept: Optional[CodeableConcept] = None
    doseAndRate: Optional[List[DosageDoseAndRate]] = empty_list()
    maxDosePerAdministration: Optional[Quantity] = None
    maxDosePerLifetime: Optional[Quantity] = None
    maxDosePerPeriod: Optional[Ratio] = None
    method: Optional[CodeableConcept] = None
    patientInstruction: Optional[str] = None
    route: Optional[CodeableConcept] = None
    sequence: Optional[int] = None
    site: Optional[CodeableConcept] = None
    text: Optional[str] = None
    timing: Optional[Timing] = None

    def elementProperties(self):
        js = super(Dosage, self).elementProperties()
        js.extend([
            ("additionalInstruction", "additionalInstruction", CodeableConcept, True, None, False),
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", CodeableConcept, False, "asNeeded", False),
            ("doseAndRate", "doseAndRate", DosageDoseAndRate, True, None, False),
            ("maxDosePerAdministration", "maxDosePerAdministration", Quantity, False, None, False),
            ("maxDosePerLifetime", "maxDosePerLifetime", Quantity, False, None, False),
            ("maxDosePerPeriod", "maxDosePerPeriod", Ratio, False, None, False),
            ("method", "method", CodeableConcept, False, None, False),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("route", "route", CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, False),
            ("site", "site", CodeableConcept, False, None, False),
            ("text", "text", str, False, None, False),
            ("timing", "timing", Timing, False, None, False),
        ])
        return js