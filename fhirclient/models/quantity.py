#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MoneyQuantity) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .element import Element


@dataclass
class Quantity(Element):
    """ A measured or measurable amount.

    A measured amount (or an amount that can potentially be measured). Note
    that measured amounts include amounts that are not precisely quantified,
    including amounts involving arbitrary units and floating currencies.
    """
    resource_type: ClassVar[str] = "Quantity"
    code: Optional[str] = None
    comparator: Optional[str] = None
    system: Optional[str] = None
    unit: Optional[str] = None
    value: Optional[float] = None

    def elementProperties(self):
        js = super(Quantity, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("comparator", "comparator", str, False, None, False),
            ("system", "system", str, False, None, False),
            ("unit", "unit", str, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js