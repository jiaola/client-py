#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ManufacturedItemDefinition) on 2019-08-26.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .prodcharacteristic import ProdCharacteristic
from .quantity import Quantity


@dataclass
class ManufacturedItemDefinition(DomainResource):
    """ The manufactured item as contained in the packaged medicinal product.
    """
    resource_type: ClassVar[str] = "ManufacturedItemDefinition"

    manufacturedDoseForm: CodeableConcept = None
    unitOfPresentation: Optional[CodeableConcept] = None
    quantity: Quantity = None
    manufacturer: Optional[List[FHIRReference]] = None
    ingredient: Optional[List[FHIRReference]] = None
    physicalCharacteristics: Optional[ProdCharacteristic] = None
    otherCharacteristics: Optional[List[CodeableConcept]] = None