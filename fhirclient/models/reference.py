#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Reference) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .element import Element
from .identifier import Identifier


@dataclass
class Reference(Element):
    """ A reference from one resource to another.
    """
    resource_type: ClassVar[str] = "Reference"
    display: Optional[str] = None
    identifier: Optional[Identifier] = None
    reference: Optional[str] = None
    type: Optional[str] = None

    def elementProperties(self):
        js = super(Reference, self).elementProperties()
        js.extend([
            ("display", "display", str, False, None, False),
            ("identifier", "identifier", Identifier, False, None, False),
            ("reference", "reference", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js