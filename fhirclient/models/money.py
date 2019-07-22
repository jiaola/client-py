#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Money) on 2019-07-22.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .element import Element


@dataclass
class Money(Element):
    """ An amount of economic utility in some recognized currency.
    """
    resource_type: ClassVar[str] = "Money"
    value: Optional[float] = None
    currency: Optional[str] = None

    def elementProperties(self):
        js = super(Money, self).elementProperties()
        js.extend([
            ("value", "value", float, False, None, False),
            ("currency", "currency", str, False, None, False),
        ])
        return js