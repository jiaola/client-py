#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SubstanceAmount) on 2019-07-18.
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

from . import element

@dataclass
class SubstanceAmountReferenceRange(element.Element):
    """ Reference range of possible or expected values.
    """
    resource_type: ClassVar[str] = "SubstanceAmountReferenceRange"
    highLimit: Optional[quantity.Quantity] = None
    lowLimit: Optional[quantity.Quantity] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceAmountReferenceRange, self).elementProperties()
        js.extend([
            ("highLimit", "highLimit", quantity.Quantity, False, None, False),
            ("lowLimit", "lowLimit", quantity.Quantity, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class SubstanceAmount(backboneelement.BackboneElement):
    """ Chemical substances are a single substance type whose primary defining
    element is the molecular structure. Chemical substances shall be defined on
    the basis of their complete covalent molecular structure; the presence of a
    salt (counter-ion) and/or solvates (water, alcohols) is also captured.
    Purity, grade, physical form or particle size are not taken into account in
    the definition of a chemical substance or in the assignment of a Substance
    ID.
    """
    resource_type: ClassVar[str] = "SubstanceAmount"
    amountQuantity: Optional[quantity.Quantity] = None
    amountRange: Optional[range.Range] = None
    amountString: Optional[str] = None
    amountText: Optional[str] = None
    amountType: Optional[codeableconcept.CodeableConcept] = None
    referenceRange: Optional[SubstanceAmountReferenceRange] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceAmount, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("amountRange", "amountRange", range.Range, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
            ("amountText", "amountText", str, False, None, False),
            ("amountType", "amountType", codeableconcept.CodeableConcept, False, None, False),
            ("referenceRange", "referenceRange", SubstanceAmountReferenceRange, False, None, False),
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