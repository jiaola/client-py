#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductManufactured) on 2019-07-29.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .prodcharacteristic import ProdCharacteristic
from .quantity import Quantity


@dataclass
class MedicinalProductManufactured(DomainResource):
    """ The manufactured item as contained in the packaged medicinal product.
    """
    resource_type: ClassVar[str] = "MedicinalProductManufactured"
    manufacturedDoseForm: CodeableConcept = None
    unitOfPresentation: Optional[CodeableConcept] = None
    quantity: Quantity = None
    manufacturer: Optional[List[FHIRReference]] = empty_list()
    ingredient: Optional[List[FHIRReference]] = empty_list()
    physicalCharacteristics: Optional[ProdCharacteristic] = None
    otherCharacteristics: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(MedicinalProductManufactured, self).elementProperties()
        js.extend([
            ("manufacturedDoseForm", "manufacturedDoseForm", CodeableConcept, False, None, True),
            ("unitOfPresentation", "unitOfPresentation", CodeableConcept, False, None, False),
            ("quantity", "quantity", Quantity, False, None, True),
            ("manufacturer", "manufacturer", FHIRReference, True, None, False),
            ("ingredient", "ingredient", FHIRReference, True, None, False),
            ("physicalCharacteristics", "physicalCharacteristics", ProdCharacteristic, False, None, False),
            ("otherCharacteristics", "otherCharacteristics", CodeableConcept, True, None, False),
        ])
        return js