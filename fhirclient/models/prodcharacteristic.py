#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ProdCharacteristic) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .quantity import Quantity


@dataclass
class ProdCharacteristic(BackboneElement):
    """ The marketing status describes the date when a medicinal product is
    actually put on the market or the date as of which it is no longer
    available.
    """
    resource_type: ClassVar[str] = "ProdCharacteristic"
    color: Optional[List[str]] = empty_list()
    depth: Optional[Quantity] = None
    externalDiameter: Optional[Quantity] = None
    height: Optional[Quantity] = None
    image: Optional[List[Attachment]] = empty_list()
    imprint: Optional[List[str]] = empty_list()
    nominalVolume: Optional[Quantity] = None
    scoring: Optional[CodeableConcept] = None
    shape: Optional[str] = None
    weight: Optional[Quantity] = None
    width: Optional[Quantity] = None

    def elementProperties(self):
        js = super(ProdCharacteristic, self).elementProperties()
        js.extend([
            ("color", "color", str, True, None, False),
            ("depth", "depth", Quantity, False, None, False),
            ("externalDiameter", "externalDiameter", Quantity, False, None, False),
            ("height", "height", Quantity, False, None, False),
            ("image", "image", Attachment, True, None, False),
            ("imprint", "imprint", str, True, None, False),
            ("nominalVolume", "nominalVolume", Quantity, False, None, False),
            ("scoring", "scoring", CodeableConcept, False, None, False),
            ("shape", "shape", str, False, None, False),
            ("weight", "weight", Quantity, False, None, False),
            ("width", "width", Quantity, False, None, False),
        ])
        return js