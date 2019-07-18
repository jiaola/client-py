#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ObservationDefinition) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirreference
from . import identifier
from . import range

from . import backboneelement

@dataclass
class ObservationDefinitionQuantitativeDetails(backboneelement.BackboneElement):
    """ Characteristics of quantitative results.

    Characteristics for quantitative results of this observation.
    """
    resource_type: ClassVar[str] = "ObservationDefinitionQuantitativeDetails"
    conversionFactor: Optional[float] = None
    customaryUnit: Optional[codeableconcept.CodeableConcept] = None
    decimalPrecision: Optional[int] = None
    unit: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ObservationDefinitionQuantitativeDetails, self).elementProperties()
        js.extend([
            ("conversionFactor", "conversionFactor", float, False, None, False),
            ("customaryUnit", "customaryUnit", codeableconcept.CodeableConcept, False, None, False),
            ("decimalPrecision", "decimalPrecision", int, False, None, False),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class ObservationDefinitionQualifiedInterval(backboneelement.BackboneElement):
    """ Qualified range for continuous and ordinal observation results.

    Multiple  ranges of results qualified by different contexts for ordinal or
    continuous observations conforming to this ObservationDefinition.
    """
    resource_type: ClassVar[str] = "ObservationDefinitionQualifiedInterval"
    age: Optional[range.Range] = None
    appliesTo: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    category: Optional[str] = None
    condition: Optional[str] = None
    context: Optional[codeableconcept.CodeableConcept] = None
    gender: Optional[str] = None
    gestationalAge: Optional[range.Range] = None
    range: Optional[range.Range] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ObservationDefinitionQualifiedInterval, self).elementProperties()
        js.extend([
            ("age", "age", range.Range, False, None, False),
            ("appliesTo", "appliesTo", codeableconcept.CodeableConcept, True, None, False),
            ("category", "category", str, False, None, False),
            ("condition", "condition", str, False, None, False),
            ("context", "context", codeableconcept.CodeableConcept, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("gestationalAge", "gestationalAge", range.Range, False, None, False),
            ("range", "range", range.Range, False, None, False),
        ])
        return js

from . import domainresource

@dataclass
class ObservationDefinition(domainresource.DomainResource):
    """ Definition of an observation.

    Set of definitional characteristics for a kind of observation or
    measurement produced or consumed by an orderable health care service.
    """
    resource_type: ClassVar[str] = "ObservationDefinition"
    abnormalCodedValueSet: Optional[fhirreference.FHIRReference] = None
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    code:codeableconcept.CodeableConcept = None
    criticalCodedValueSet: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    method: Optional[codeableconcept.CodeableConcept] = None
    multipleResultsAllowed: Optional[bool] = None
    normalCodedValueSet: Optional[fhirreference.FHIRReference] = None
    permittedDataType: Optional[List[str]] = empty_list()
    preferredReportName: Optional[str] = None
    qualifiedInterval: Optional[List[ObservationDefinitionQualifiedInterval]] = empty_list()
    quantitativeDetails: Optional[ObservationDefinitionQuantitativeDetails] = None
    validCodedValueSet: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ObservationDefinition, self).elementProperties()
        js.extend([
            ("abnormalCodedValueSet", "abnormalCodedValueSet", fhirreference.FHIRReference, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("criticalCodedValueSet", "criticalCodedValueSet", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("multipleResultsAllowed", "multipleResultsAllowed", bool, False, None, False),
            ("normalCodedValueSet", "normalCodedValueSet", fhirreference.FHIRReference, False, None, False),
            ("permittedDataType", "permittedDataType", str, True, None, False),
            ("preferredReportName", "preferredReportName", str, False, None, False),
            ("qualifiedInterval", "qualifiedInterval", ObservationDefinitionQualifiedInterval, True, None, False),
            ("quantitativeDetails", "quantitativeDetails", ObservationDefinitionQuantitativeDetails, False, None, False),
            ("validCodedValueSet", "validCodedValueSet", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']