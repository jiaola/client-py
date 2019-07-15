#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/BackboneElement) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import element
from . import extension

from . import element

@dataclass
class BackboneElement(element.Element):
    """ Base for elements defined inside a resource.

    Base definition for all elements that are defined inside a resource - but
    not those in a data type.
    """
    resource_type: ClassVar[str] = "BackboneElement"
    modifierExtension: Optional[List[extension.Extension]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(BackboneElement, self).elementProperties()
        js.extend([
            ("modifierExtension", "modifierExtension", extension.Extension, True, None, False),
        ])
        return js


import sys
try:
    from . import extension
except ImportError:
    extension = sys.modules[__package__ + '.extension']