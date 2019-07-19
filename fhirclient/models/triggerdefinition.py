#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/TriggerDefinition) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .datarequirement import DataRequirement
from .element import Element
from .expression import Expression
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .timing import Timing


@dataclass
class TriggerDefinition(Element):
    """ Defines an expected trigger for a module.

    A description of a triggering event. Triggering events can be named events,
    data events, or periodic, as determined by the type element.
    """
    resource_type: ClassVar[str] = "TriggerDefinition"
    condition: Optional[Expression] = None
    data: Optional[List[DataRequirement]] = empty_list()
    name: Optional[str] = None
    timingDate: Optional[FHIRDate] = None
    timingDateTime: Optional[FHIRDate] = None
    timingReference: Optional[FHIRReference] = None
    timingTiming: Optional[Timing] = None
    type: str = None

    def elementProperties(self):
        js = super(TriggerDefinition, self).elementProperties()
        js.extend([
            ("condition", "condition", Expression, False, None, False),
            ("data", "data", DataRequirement, True, None, False),
            ("name", "name", str, False, None, False),
            ("timingDate", "timingDate", FHIRDate, False, "timing", False),
            ("timingDateTime", "timingDateTime", FHIRDate, False, "timing", False),
            ("timingReference", "timingReference", FHIRReference, False, "timing", False),
            ("timingTiming", "timingTiming", Timing, False, "timing", False),
            ("type", "type", str, False, None, True),
        ])
        return js