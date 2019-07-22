#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ObservationDefinition) on 2019-07-22.
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
    customaryUnit: Optional[CodeableConcept] = None
    unit: Optional[CodeableConcept] = None
    conversionFactor: Optional[float] = None
    decimalPrecision: Optional[int] = None

    def elementProperties(self):
        js = super(ObservationDefinitionQuantitativeDetails, self).elementProperties()
        js.extend([
            ("customaryUnit", "customaryUnit", CodeableConcept, False, None, False),
            ("unit", "unit", CodeableConcept, False, None, False),
            ("conversionFactor", "conversionFactor", float, False, None, False),
            ("decimalPrecision", "decimalPrecision", int, False, None, False),
        ])
        return js


@dataclass
class ObservationDefinitionQualifiedInterval(BackboneElement):
    """ Qualified range for continuous and ordinal observation results.

    Multiple  ranges of results qualified by different contexts for ordinal or
    continuous observations conforming to this ObservationDefinition.
    """
    resource_type: ClassVar[str] = "ObservationDefinitionQualifiedInterval"
    category: Optional[str] = None
    range: Optional[Range] = None
    context: Optional[CodeableConcept] = None
    appliesTo: Optional[List[CodeableConcept]] = empty_list()
    gender: Optional[str] = None
    age: Optional[Range] = None
    gestationalAge: Optional[Range] = None
    condition: Optional[str] = None

    def elementProperties(self):
        js = super(ObservationDefinitionQualifiedInterval, self).elementProperties()
        js.extend([
            ("category", "category", str, False, None, False),
            ("range", "range", Range, False, None, False),
            ("context", "context", CodeableConcept, False, None, False),
            ("appliesTo", "appliesTo", CodeableConcept, True, None, False),
            ("gender", "gender", str, False, None, False),
            ("age", "age", Range, False, None, False),
            ("gestationalAge", "gestationalAge", Range, False, None, False),
            ("condition", "condition", str, False, None, False),
        ])
        return js


@dataclass
class ObservationDefinition(DomainResource):
    """ Definition of an observation.

    Set of definitional characteristics for a kind of observation or
    measurement produced or consumed by an orderable health care service.
    """
    resource_type: ClassVar[str] = "ObservationDefinition"
    category: Optional[List[CodeableConcept]] = empty_list()
    code: CodeableConcept = None
    identifier: Optional[List[Identifier]] = empty_list()
    permittedDataType: Optional[List[str]] = empty_list()
    multipleResultsAllowed: Optional[bool] = None
    method: Optional[CodeableConcept] = None
    preferredReportName: Optional[str] = None
    quantitativeDetails: Optional[ObservationDefinitionQuantitativeDetails] = None
    qualifiedInterval: Optional[List[ObservationDefinitionQualifiedInterval]] = empty_list()
    validCodedValueSet: Optional[FHIRReference] = None
    normalCodedValueSet: Optional[FHIRReference] = None
    abnormalCodedValueSet: Optional[FHIRReference] = None
    criticalCodedValueSet: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(ObservationDefinition, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, True, None, False),
            ("code", "code", CodeableConcept, False, None, True),
            ("identifier", "identifier", Identifier, True, None, False),
            ("permittedDataType", "permittedDataType", str, True, None, False),
            ("multipleResultsAllowed", "multipleResultsAllowed", bool, False, None, False),
            ("method", "method", CodeableConcept, False, None, False),
            ("preferredReportName", "preferredReportName", str, False, None, False),
            ("quantitativeDetails", "quantitativeDetails", ObservationDefinitionQuantitativeDetails, False, None, False),
            ("qualifiedInterval", "qualifiedInterval", ObservationDefinitionQualifiedInterval, True, None, False),
            ("validCodedValueSet", "validCodedValueSet", FHIRReference, False, None, False),
            ("normalCodedValueSet", "normalCodedValueSet", FHIRReference, False, None, False),
            ("abnormalCodedValueSet", "abnormalCodedValueSet", FHIRReference, False, None, False),
            ("criticalCodedValueSet", "criticalCodedValueSet", FHIRReference, False, None, False),
        ])
        return js