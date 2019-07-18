#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Element) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import extension
from . import fhirabstractbase

from . import fhirabstractbase

@dataclass
class Element(fhirabstractbase.FHIRAbstractBase):
    """ Base for all elements.

    Base definition for all elements in a resource.
    """
    resource_type: ClassVar[str] = "Element"
    extension: Optional[List[extension.Extension]] = empty_list()
    id: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Element, self).elementProperties()
        from . import extension
        js.extend([
            ("extension", "extension", extension.Extension, True, None, False),
            ("id", "id", str, False, None, False),
        ])
        return js

