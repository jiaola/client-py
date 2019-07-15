#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DataRequirement) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import coding
from . import duration
from . import element
from . import fhirdate
from . import fhirreference
from . import period

from . import element

@dataclass
class DataRequirement(element.Element):
    """ Describes a required data item.

    Describes a required data item for evaluation in terms of the type of data,
    and optional code or date-based filters of the data.
    """
    resource_type: ClassVar[str] = "DataRequirement"
    codeFilter: Optional[List[DataRequirementCodeFilter]] = empty_list()
    dateFilter: Optional[List[DataRequirementDateFilter]] = empty_list()
    limit: Optional[int] = None
    mustSupport: Optional[List[str]] = empty_list()
    profile: Optional[List[str]] = empty_list()
    sort: Optional[List[DataRequirementSort]] = empty_list()
    subjectCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    subjectReference: Optional[fhirreference.FHIRReference] = None
    type: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DataRequirement, self).elementProperties()
        js.extend([
            ("codeFilter", "codeFilter", DataRequirementCodeFilter, True, None, False),
            ("dateFilter", "dateFilter", DataRequirementDateFilter, True, None, False),
            ("limit", "limit", int, False, None, False),
            ("mustSupport", "mustSupport", str, True, None, False),
            ("profile", "profile", str, True, None, False),
            ("sort", "sort", DataRequirementSort, True, None, False),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("type", "type", str, False, None, True),
        ])
        return js

@dataclass
class DataRequirementCodeFilter(element.Element):
    """ What codes are expected.

    Code filters specify additional constraints on the data, specifying the
    value set of interest for a particular element of the data. Each code
    filter defines an additional constraint on the data, i.e. code filters are
    AND'ed, not OR'ed.
    """
    resource_type: ClassVar[str] = "DataRequirementCodeFilter"
    code: Optional[List[coding.Coding]] = empty_list()
    path: Optional[str] = None
    searchParam: Optional[str] = None
    valueSet: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DataRequirementCodeFilter, self).elementProperties()
        js.extend([
            ("code", "code", coding.Coding, True, None, False),
            ("path", "path", str, False, None, False),
            ("searchParam", "searchParam", str, False, None, False),
            ("valueSet", "valueSet", str, False, None, False),
        ])
        return js

@dataclass
class DataRequirementDateFilter(element.Element):
    """ What dates/date ranges are expected.

    Date filters specify additional constraints on the data in terms of the
    applicable date range for specific elements. Each date filter specifies an
    additional constraint on the data, i.e. date filters are AND'ed, not OR'ed.
    """
    resource_type: ClassVar[str] = "DataRequirementDateFilter"
    path: Optional[str] = None
    searchParam: Optional[str] = None
    valueDateTime: Optional[fhirdate.FHIRDate] = None
    valueDuration: Optional[duration.Duration] = None
    valuePeriod: Optional[period.Period] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DataRequirementDateFilter, self).elementProperties()
        js.extend([
            ("path", "path", str, False, None, False),
            ("searchParam", "searchParam", str, False, None, False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
        ])
        return js

@dataclass
class DataRequirementSort(element.Element):
    """ Order of the results.

    Specifies the order of the results to be returned.
    """
    resource_type: ClassVar[str] = "DataRequirementSort"
    direction: str = None
    path: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DataRequirementSort, self).elementProperties()
        js.extend([
            ("direction", "direction", str, False, None, True),
            ("path", "path", str, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']