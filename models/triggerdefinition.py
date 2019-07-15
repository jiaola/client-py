#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/TriggerDefinition) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import datarequirement
from . import element
from . import expression
from . import fhirdate
from . import fhirreference
from . import timing

from . import element

@dataclass
class TriggerDefinition(element.Element):
    """ Defines an expected trigger for a module.

    A description of a triggering event. Triggering events can be named events,
    data events, or periodic, as determined by the type element.
    """
    resource_type: ClassVar[str] = "TriggerDefinition"
    condition: Optional[expression.Expression] = None
    data: Optional[List[datarequirement.DataRequirement]] = empty_list()
    name: Optional[str] = None
    timingDate: Optional[fhirdate.FHIRDate] = None
    timingDateTime: Optional[fhirdate.FHIRDate] = None
    timingReference: Optional[fhirreference.FHIRReference] = None
    timingTiming: Optional[timing.Timing] = None
    type: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TriggerDefinition, self).elementProperties()
        js.extend([
            ("condition", "condition", expression.Expression, False, None, False),
            ("data", "data", datarequirement.DataRequirement, True, None, False),
            ("name", "name", str, False, None, False),
            ("timingDate", "timingDate", fhirdate.FHIRDate, False, "timing", False),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("timingReference", "timingReference", fhirreference.FHIRReference, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("type", "type", str, False, None, True),
        ])
        return js


import sys
try:
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + '.datarequirement']
try:
    from . import expression
except ImportError:
    expression = sys.modules[__package__ + '.expression']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']