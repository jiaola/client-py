#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Element) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .fhirabstractbase import FHIRAbstractBase



@dataclass
class Element(FHIRAbstractBase):
    """ Base for all elements.

    Base definition for all elements in a resource.
    """
    resource_type: ClassVar[str] = "Element"
    extension: Optional[List["Extension"]] = empty_list()
    id: Optional["str"] = None

    def elementProperties(self):
        from .extension import Extension
        
        js = super(Element, self).elementProperties()
        js.extend([
            ("extension", "extension", Extension, True, None, False),
            ("id", "id", str, False, None, False),
        ])
        return js