#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ProdCharacteristic) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import backboneelement
from . import codeableconcept
from . import quantity

from . import backboneelement

@dataclass
class ProdCharacteristic(backboneelement.BackboneElement):
    """ The marketing status describes the date when a medicinal product is
    actually put on the market or the date as of which it is no longer
    available.
    """
    resource_type: ClassVar[str] = "ProdCharacteristic"
    color: Optional[List[str]] = empty_list()
    depth: Optional[quantity.Quantity] = None
    externalDiameter: Optional[quantity.Quantity] = None
    height: Optional[quantity.Quantity] = None
    image: Optional[List[attachment.Attachment]] = empty_list()
    imprint: Optional[List[str]] = empty_list()
    nominalVolume: Optional[quantity.Quantity] = None
    scoring: Optional[codeableconcept.CodeableConcept] = None
    shape: Optional[str] = None
    weight: Optional[quantity.Quantity] = None
    width: Optional[quantity.Quantity] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ProdCharacteristic, self).elementProperties()
        js.extend([
            ("color", "color", str, True, None, False),
            ("depth", "depth", quantity.Quantity, False, None, False),
            ("externalDiameter", "externalDiameter", quantity.Quantity, False, None, False),
            ("height", "height", quantity.Quantity, False, None, False),
            ("image", "image", attachment.Attachment, True, None, False),
            ("imprint", "imprint", str, True, None, False),
            ("nominalVolume", "nominalVolume", quantity.Quantity, False, None, False),
            ("scoring", "scoring", codeableconcept.CodeableConcept, False, None, False),
            ("shape", "shape", str, False, None, False),
            ("weight", "weight", quantity.Quantity, False, None, False),
            ("width", "width", quantity.Quantity, False, None, False),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']