#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Narrative) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .element import Element


@dataclass
class Narrative(Element):
    """ Human-readable summary of the resource (essential clinical and business
    information).

    A human-readable summary of the resource conveying the essential clinical
    and business information for the resource.
    """
    resource_type: ClassVar[str] = "Narrative"
    div: str = None
    status: str = None

    def elementProperties(self):
        js = super(Narrative, self).elementProperties()
        js.extend([
            ("div", "div", str, False, None, True),
            ("status", "status", str, False, None, True),
        ])
        return js