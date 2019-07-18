#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Coding) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import element

from . import element

@dataclass
class Coding(element.Element):
    """ A reference to a code defined by a terminology system.
    """
    resource_type: ClassVar[str] = "Coding"
    code: Optional[str] = None
    display: Optional[str] = None
    system: Optional[str] = None
    userSelected: Optional[bool] = None
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Coding, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("display", "display", str, False, None, False),
            ("system", "system", str, False, None, False),
            ("userSelected", "userSelected", bool, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js

