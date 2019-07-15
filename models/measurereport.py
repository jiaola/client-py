#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MeasureReport) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity

from . import domainresource

@dataclass
class MeasureReport(domainresource.DomainResource):
    """ Results of a measure evaluation.

    The MeasureReport resource contains the results of the calculation of a
    measure; and optionally a reference to the resources involved in that
    calculation.
    """
    resource_type: ClassVar[str] = "MeasureReport"
    date: Optional[fhirdate.FHIRDate] = None
    evaluatedResource: Optional[List[fhirreference.FHIRReference]] = empty_list()
    group: Optional[List[MeasureReportGroup]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    improvementNotation: Optional[codeableconcept.CodeableConcept] = None
    measure: str = None
    period:period.Period = None
    reporter: Optional[fhirreference.FHIRReference] = None
    status: str = None
    subject: Optional[fhirreference.FHIRReference] = None
    type: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MeasureReport, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("evaluatedResource", "evaluatedResource", fhirreference.FHIRReference, True, None, False),
            ("group", "group", MeasureReportGroup, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("improvementNotation", "improvementNotation", codeableconcept.CodeableConcept, False, None, False),
            ("measure", "measure", str, False, None, True),
            ("period", "period", period.Period, False, None, True),
            ("reporter", "reporter", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js

from . import backboneelement

@dataclass
class MeasureReportGroup(backboneelement.BackboneElement):
    """ Measure results for each group.

    The results of the calculation, one for each population group in the
    measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroup"
    code: Optional[codeableconcept.CodeableConcept] = None
    measureScore: Optional[quantity.Quantity] = None
    population: Optional[List[MeasureReportGroupPopulation]] = empty_list()
    stratifier: Optional[List[MeasureReportGroupStratifier]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MeasureReportGroup, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("measureScore", "measureScore", quantity.Quantity, False, None, False),
            ("population", "population", MeasureReportGroupPopulation, True, None, False),
            ("stratifier", "stratifier", MeasureReportGroupStratifier, True, None, False),
        ])
        return js

@dataclass
class MeasureReportGroupPopulation(backboneelement.BackboneElement):
    """ The populations in the group.

    The populations that make up the population group, one for each type of
    population appropriate for the measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupPopulation"
    code: Optional[codeableconcept.CodeableConcept] = None
    count: Optional[int] = None
    subjectResults: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MeasureReportGroupPopulation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("count", "count", int, False, None, False),
            ("subjectResults", "subjectResults", fhirreference.FHIRReference, False, None, False),
        ])
        return js

@dataclass
class MeasureReportGroupStratifier(backboneelement.BackboneElement):
    """ Stratification results.

    When a measure includes multiple stratifiers, there will be a stratifier
    group for each stratifier defined by the measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupStratifier"
    code: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    stratum: Optional[List[MeasureReportGroupStratifierStratum]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MeasureReportGroupStratifier, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("stratum", "stratum", MeasureReportGroupStratifierStratum, True, None, False),
        ])
        return js

@dataclass
class MeasureReportGroupStratifierStratum(backboneelement.BackboneElement):
    """ Stratum results, one for each unique value, or set of values, in the
    stratifier, or stratifier components.

    This element contains the results for a single stratum within the
    stratifier. For example, when stratifying on administrative gender, there
    will be four strata, one for each possible gender value.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupStratifierStratum"
    component: Optional[List[MeasureReportGroupStratifierStratumComponent]] = empty_list()
    measureScore: Optional[quantity.Quantity] = None
    population: Optional[List[MeasureReportGroupStratifierStratumPopulation]] = empty_list()
    value: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MeasureReportGroupStratifierStratum, self).elementProperties()
        js.extend([
            ("component", "component", MeasureReportGroupStratifierStratumComponent, True, None, False),
            ("measureScore", "measureScore", quantity.Quantity, False, None, False),
            ("population", "population", MeasureReportGroupStratifierStratumPopulation, True, None, False),
            ("value", "value", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class MeasureReportGroupStratifierStratumComponent(backboneelement.BackboneElement):
    """ Stratifier component values.

    A stratifier component value.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupStratifierStratumComponent"
    code:codeableconcept.CodeableConcept = None
    value:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MeasureReportGroupStratifierStratumComponent, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class MeasureReportGroupStratifierStratumPopulation(backboneelement.BackboneElement):
    """ Population results in this stratum.

    The populations that make up the stratum, one for each type of population
    appropriate to the measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupStratifierStratumPopulation"
    code: Optional[codeableconcept.CodeableConcept] = None
    count: Optional[int] = None
    subjectResults: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MeasureReportGroupStratifierStratumPopulation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("count", "count", int, False, None, False),
            ("subjectResults", "subjectResults", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']