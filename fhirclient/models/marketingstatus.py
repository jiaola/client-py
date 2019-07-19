#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MarketingStatus) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .fhirdate import FHIRDate
from .period import Period


@dataclass
class MarketingStatus(BackboneElement):
    """ The marketing status describes the date when a medicinal product is
    actually put on the market or the date as of which it is no longer
    available.
    """
    resource_type: ClassVar[str] = "MarketingStatus"
    country: CodeableConcept = None
    dateRange: Period = None
    jurisdiction: Optional[CodeableConcept] = None
    restoreDate: Optional[FHIRDate] = None
    status: CodeableConcept = None

    def elementProperties(self):
        js = super(MarketingStatus, self).elementProperties()
        js.extend([
            ("country", "country", CodeableConcept, False, None, True),
            ("dateRange", "dateRange", Period, False, None, True),
            ("jurisdiction", "jurisdiction", CodeableConcept, False, None, False),
            ("restoreDate", "restoreDate", FHIRDate, False, None, False),
            ("status", "status", CodeableConcept, False, None, True),
        ])
        return js