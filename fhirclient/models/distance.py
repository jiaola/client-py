#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Distance) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .quantity import Quantity


@dataclass
class Distance(Quantity):
    """ A length - a value with a unit that is a physical distance.
    """
    resource_type: ClassVar[str] = "Distance"