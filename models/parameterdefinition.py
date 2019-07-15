#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ParameterDefinition) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import element

from . import element

@dataclass
class ParameterDefinition(element.Element):
    """ Definition of a parameter to a module.

    The parameters to the module. This collection specifies both the input and
    output parameters. Input parameters are provided by the caller as part of
    the $evaluate operation. Output parameters are included in the
    GuidanceResponse.
    """
    resource_type: ClassVar[str] = "ParameterDefinition"
    documentation: Optional[str] = None
    max: Optional[str] = None
    min: Optional[int] = None
    name: Optional[str] = None
    profile: Optional[str] = None
    type: str = None
    use: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ParameterDefinition, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("max", "max", str, False, None, False),
            ("min", "min", int, False, None, False),
            ("name", "name", str, False, None, False),
            ("profile", "profile", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("use", "use", str, False, None, True),
        ])
        return js

