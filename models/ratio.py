#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Ratio) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import element
from . import quantity


from . import element

@dataclass
class Ratio(element.Element):
    """ A ratio of two Quantity values - a numerator and a denominator.

    A relationship of two Quantity values - expressed as a numerator and a
    denominator.
    """
    resource_type: ClassVar[str] = "Ratio"
    denominator: Optional[quantity.Quantity] = None
    numerator: Optional[quantity.Quantity] = None

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
#        self.denominator = None
#        """ Denominator value.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.numerator = None
#        """ Numerator value.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#

#        super(Ratio, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Ratio, self).elementProperties()
        js.extend([
            ("denominator", "denominator", quantity.Quantity, {  # #}False, None, {  # #}False),
            ("numerator", "numerator", quantity.Quantity, {  # #}False, None, {  # #}False),
        ])
        return js