#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/BackboneElement) on 2019-07-03.
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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.modifierExtension = None
#        """ Extensions that cannot be ignored even if unrecognized.
#        List of `Extension` items
#
# (represented as `dict` in JSON). """
#

#        super(BackboneElement, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(BackboneElement, self).elementProperties()
        js.extend([
            ("modifierExtension", "modifierExtension", extension.Extension, {  # #}True, None, {  # #}False),
        ])
        return js