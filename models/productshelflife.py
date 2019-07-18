#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ProductShelfLife) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import identifier
from . import quantity

from . import backboneelement

@dataclass
class ProductShelfLife(backboneelement.BackboneElement):
    """ The shelf-life and storage information for a medicinal product item or
    container can be described using this class.
    """
    resource_type: ClassVar[str] = "ProductShelfLife"
    identifier: Optional[identifier.Identifier] = None
    period:quantity.Quantity = None
    specialPrecautionsForStorage: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    type:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ProductShelfLife, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("period", "period", quantity.Quantity, False, None, True),
            ("specialPrecautionsForStorage", "specialPrecautionsForStorage", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']