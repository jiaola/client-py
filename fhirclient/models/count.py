#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Count) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .quantity import Quantity


@dataclass
class Count(Quantity):
    """ A measured or measurable amount.

    A measured amount (or an amount that can potentially be measured). Note
    that measured amounts include amounts that are not precisely quantified,
    including amounts involving arbitrary units and floating currencies.
    """
    resource_type: ClassVar[str] = "Count"