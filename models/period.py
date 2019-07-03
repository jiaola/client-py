#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Period) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import element
from . import fhirdate


from . import element

@dataclass
class Period(element.Element):
    """ Time range defined by start and end date/time.

    A time period defined by a start and end date and optionally time.
    """
    resource_type: ClassVar[str] = "Period"
    end: Optional[fhirdate.FHIRDate] = None
    start: Optional[fhirdate.FHIRDate] = None

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
#        self.end = None
#        """ End time with inclusive boundary, if not ongoing.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.start = None
#        """ Starting time with inclusive boundary.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#

#        super(Period, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Period, self).elementProperties()
        js.extend([
            ("end", "end", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("start", "start", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
        ])
        return js