#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/HumanName) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import element
from . import period

from . import element

@dataclass
class HumanName(element.Element):
    """ Name of a human - parts and usage.

    A human's name with the ability to identify parts and usage.
    """
    resource_type: ClassVar[str] = "HumanName"
    family: Optional[str] = None
    given: Optional[List[str]] = empty_list()
    period: Optional[period.Period] = None
    prefix: Optional[List[str]] = empty_list()
    suffix: Optional[List[str]] = empty_list()
    text: Optional[str] = None
    use: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(HumanName, self).elementProperties()
        js.extend([
            ("family", "family", str, False, None, False),
            ("given", "given", str, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("prefix", "prefix", str, True, None, False),
            ("suffix", "suffix", str, True, None, False),
            ("text", "text", str, False, None, False),
            ("use", "use", str, False, None, False),
        ])
        return js


import sys
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']