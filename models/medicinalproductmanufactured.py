#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductManufactured) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import domainresource
from . import fhirreference
from . import prodcharacteristic
from . import quantity

from . import domainresource

@dataclass
class MedicinalProductManufactured(domainresource.DomainResource):
    """ The manufactured item as contained in the packaged medicinal product.
    """
    resource_type: ClassVar[str] = "MedicinalProductManufactured"
    ingredient: Optional[List[fhirreference.FHIRReference]] = empty_list()
    manufacturedDoseForm:codeableconcept.CodeableConcept = None
    manufacturer: Optional[List[fhirreference.FHIRReference]] = empty_list()
    otherCharacteristics: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    physicalCharacteristics: Optional[prodcharacteristic.ProdCharacteristic] = None
    quantity:quantity.Quantity = None
    unitOfPresentation: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductManufactured, self).elementProperties()
        js.extend([
            ("ingredient", "ingredient", fhirreference.FHIRReference, True, None, False),
            ("manufacturedDoseForm", "manufacturedDoseForm", codeableconcept.CodeableConcept, False, None, True),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("otherCharacteristics", "otherCharacteristics", codeableconcept.CodeableConcept, True, None, False),
            ("physicalCharacteristics", "physicalCharacteristics", prodcharacteristic.ProdCharacteristic, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, True),
            ("unitOfPresentation", "unitOfPresentation", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import prodcharacteristic
except ImportError:
    prodcharacteristic = sys.modules[__package__ + '.prodcharacteristic']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']