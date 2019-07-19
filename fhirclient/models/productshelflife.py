#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ProductShelfLife) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .identifier import Identifier
from .quantity import Quantity


@dataclass
class ProductShelfLife(BackboneElement):
    """ The shelf-life and storage information for a medicinal product item or
    container can be described using this class.
    """
    resource_type: ClassVar[str] = "ProductShelfLife"
    identifier: Optional[Identifier] = None
    period: Quantity = None
    specialPrecautionsForStorage: Optional[List[CodeableConcept]] = empty_list()
    type: CodeableConcept = None

    def elementProperties(self):
        js = super(ProductShelfLife, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, False, None, False),
            ("period", "period", Quantity, False, None, True),
            ("specialPrecautionsForStorage", "specialPrecautionsForStorage", CodeableConcept, True, None, False),
            ("type", "type", CodeableConcept, False, None, True),
        ])
        return js