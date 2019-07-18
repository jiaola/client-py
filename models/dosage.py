#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Dosage) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import element
from . import quantity
from . import range
from . import ratio
from . import timing

from . import element

@dataclass
class DosageDoseAndRate(element.Element):
    """ Amount of medication administered.

    The amount of medication administered.
    """
    resource_type: ClassVar[str] = "DosageDoseAndRate"
    doseQuantity: Optional[quantity.Quantity] = None
    doseRange: Optional[range.Range] = None
    rateQuantity: Optional[quantity.Quantity] = None
    rateRange: Optional[range.Range] = None
    rateRatio: Optional[ratio.Ratio] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DosageDoseAndRate, self).elementProperties()
        js.extend([
            ("doseQuantity", "doseQuantity", quantity.Quantity, False, "dose", False),
            ("doseRange", "doseRange", range.Range, False, "dose", False),
            ("rateQuantity", "rateQuantity", quantity.Quantity, False, "rate", False),
            ("rateRange", "rateRange", range.Range, False, "rate", False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class Dosage(backboneelement.BackboneElement):
    """ How the medication is/was taken or should be taken.

    Indicates how the medication is/was taken or should be taken by the
    patient.
    """
    resource_type: ClassVar[str] = "Dosage"
    additionalInstruction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    asNeededBoolean: Optional[bool] = None
    asNeededCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    doseAndRate: Optional[List[DosageDoseAndRate]] = empty_list()
    maxDosePerAdministration: Optional[quantity.Quantity] = None
    maxDosePerLifetime: Optional[quantity.Quantity] = None
    maxDosePerPeriod: Optional[ratio.Ratio] = None
    method: Optional[codeableconcept.CodeableConcept] = None
    patientInstruction: Optional[str] = None
    route: Optional[codeableconcept.CodeableConcept] = None
    sequence: Optional[int] = None
    site: Optional[codeableconcept.CodeableConcept] = None
    text: Optional[str] = None
    timing: Optional[timing.Timing] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Dosage, self).elementProperties()
        js.extend([
            ("additionalInstruction", "additionalInstruction", codeableconcept.CodeableConcept, True, None, False),
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False, "asNeeded", False),
            ("doseAndRate", "doseAndRate", DosageDoseAndRate, True, None, False),
            ("maxDosePerAdministration", "maxDosePerAdministration", quantity.Quantity, False, None, False),
            ("maxDosePerLifetime", "maxDosePerLifetime", quantity.Quantity, False, None, False),
            ("maxDosePerPeriod", "maxDosePerPeriod", ratio.Ratio, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, False),
            ("site", "site", codeableconcept.CodeableConcept, False, None, False),
            ("text", "text", str, False, None, False),
            ("timing", "timing", timing.Timing, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']