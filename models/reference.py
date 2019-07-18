#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Reference) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import element
from . import identifier

from . import element

@dataclass
class Reference(element.Element):
    """ A reference from one resource to another.
    """
    resource_type: ClassVar[str] = "Reference"
    display: Optional[str] = None
    identifier: Optional[identifier.Identifier] = None
    reference: Optional[str] = None
    type: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Reference, self).elementProperties()
        js.extend([
            ("display", "display", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("reference", "reference", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


import sys
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']