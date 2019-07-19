#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ObservationDefinition) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .range import Range


@dataclass
class ObservationDefinitionQuantitativeDetails(BackboneElement):
    """ Characteristics of quantitative results.

    Characteristics for quantitative results of this observation.
    """
    resource_type: ClassVar[str] = "ObservationDefinitionQuantitativeDetails"
    conversionFactor: Optional[float] = None
    customaryUnit: Optional[CodeableConcept] = None
    decimalPrecision: Optional[int] = None
    unit: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ObservationDefinitionQuantitativeDetails, self).elementProperties()
        js.extend([
            ("conversionFactor", "conversionFactor", float, False, None, False),
            ("customaryUnit", "customaryUnit", CodeableConcept, False, None, False),
            ("decimalPrecision", "decimalPrecision", int, False, None, False),
            ("unit", "unit", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ObservationDefinitionQualifiedInterval(BackboneElement):
    """ Qualified range for continuous and ordinal observation results.

    Multiple  ranges of results qualified by different contexts for ordinal or
    continuous observations conforming to this ObservationDefinition.
    """
    resource_type: ClassVar[str] = "ObservationDefinitionQualifiedInterval"
    age: Optional[Range] = None
    appliesTo: Optional[List[CodeableConcept]] = empty_list()
    category: Optional[str] = None
    condition: Optional[str] = None
    context: Optional[CodeableConcept] = None
    gender: Optional[str] = None
    gestationalAge: Optional[Range] = None
    range: Optional[Range] = None

    def elementProperties(self):
        js = super(ObservationDefinitionQualifiedInterval, self).elementProperties()
        js.extend([
            ("age", "age", Range, False, None, False),
            ("appliesTo", "appliesTo", CodeableConcept, True, None, False),
            ("category", "category", str, False, None, False),
            ("condition", "condition", str, False, None, False),
            ("context", "context", CodeableConcept, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("gestationalAge", "gestationalAge", Range, False, None, False),
            ("range", "range", Range, False, None, False),
        ])
        return js


@dataclass
class ObservationDefinition(DomainResource):
    """ Definition of an observation.

    Set of definitional characteristics for a kind of observation or
    measurement produced or consumed by an orderable health care service.
    """
    resource_type: ClassVar[str] = "ObservationDefinition"
    abnormalCodedValueSet: Optional[FHIRReference] = None
    category: Optional[List[CodeableConcept]] = empty_list()
    code: CodeableConcept = None
    criticalCodedValueSet: Optional[FHIRReference] = None
    identifier: Optional[List[Identifier]] = empty_list()
    method: Optional[CodeableConcept] = None
    multipleResultsAllowed: Optional[bool] = None
    normalCodedValueSet: Optional[FHIRReference] = None
    permittedDataType: Optional[List[str]] = empty_list()
    preferredReportName: Optional[str] = None
    qualifiedInterval: Optional[List[ObservationDefinitionQualifiedInterval]] = empty_list()
    quantitativeDetails: Optional[ObservationDefinitionQuantitativeDetails] = None
    validCodedValueSet: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(ObservationDefinition, self).elementProperties()
        js.extend([
            ("abnormalCodedValueSet", "abnormalCodedValueSet", FHIRReference, False, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("code", "code", CodeableConcept, False, None, True),
            ("criticalCodedValueSet", "criticalCodedValueSet", FHIRReference, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("method", "method", CodeableConcept, False, None, False),
            ("multipleResultsAllowed", "multipleResultsAllowed", bool, False, None, False),
            ("normalCodedValueSet", "normalCodedValueSet", FHIRReference, False, None, False),
            ("permittedDataType", "permittedDataType", str, True, None, False),
            ("preferredReportName", "preferredReportName", str, False, None, False),
            ("qualifiedInterval", "qualifiedInterval", ObservationDefinitionQualifiedInterval, True, None, False),
            ("quantitativeDetails", "quantitativeDetails", ObservationDefinitionQuantitativeDetails, False, None, False),
            ("validCodedValueSet", "validCodedValueSet", FHIRReference, False, None, False),
        ])
        return js