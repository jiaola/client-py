#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Money) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import element


from . import element

@dataclass
class Money(element.Element):
    """ An amount of economic utility in some recognized currency.
    """
    resource_type: ClassVar[str] = "Money"
    currency: Optional[str] = None
    value: Optional[float] = None

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
#        self.currency = None
#        """ ISO 4217 Currency Code.
#        Type `str`
#
#. """
#
#
#        self.value = None
#        """ Numerical value (with implicit precision).
#        Type `float`
#
#. """
#

#        super(Money, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Money, self).elementProperties()
        js.extend([
            ("currency", "currency", str, {  # #}False, None, {  # #}False),
            ("value", "value", float, {  # #}False, None, {  # #}False),
        ])
        return js