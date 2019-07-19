#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Observation) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .range import Range
from .ratio import Ratio
from .sampleddata import SampledData
from .timing import Timing


@dataclass
class ObservationReferenceRange(BackboneElement):
    """ Provides guide for interpretation.

    Guidance on how to interpret the value by comparison to a normal or
    recommended range.  Multiple reference ranges are interpreted as an "OR".
    In other words, to represent two distinct target populations, two
    `referenceRange` elements would be used.
    """
    resource_type: ClassVar[str] = "ObservationReferenceRange"
    age: Optional[Range] = None
    appliesTo: Optional[List[CodeableConcept]] = empty_list()
    high: Optional[Quantity] = None
    low: Optional[Quantity] = None
    text: Optional[str] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ObservationReferenceRange, self).elementProperties()
        js.extend([
            ("age", "age", Range, False, None, False),
            ("appliesTo", "appliesTo", CodeableConcept, True, None, False),
            ("high", "high", Quantity, False, None, False),
            ("low", "low", Quantity, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ObservationComponent(BackboneElement):
    """ Component results.

    Some observations have multiple component observations.  These component
    observations are expressed as separate code value pairs that share the same
    attributes.  Examples include systolic and diastolic component observations
    for blood pressure measurement and multiple component observations for
    genetics observations.
    """
    resource_type: ClassVar[str] = "ObservationComponent"
    code: CodeableConcept = None
    dataAbsentReason: Optional[CodeableConcept] = None
    interpretation: Optional[List[CodeableConcept]] = empty_list()
    referenceRange: Optional[List[ObservationReferenceRange]] = empty_list()
    valueBoolean: Optional[bool] = None
    valueCodeableConcept: Optional[CodeableConcept] = None
    valueDateTime: Optional[FHIRDate] = None
    valueInteger: Optional[int] = None
    valuePeriod: Optional[Period] = None
    valueQuantity: Optional[Quantity] = None
    valueRange: Optional[Range] = None
    valueRatio: Optional[Ratio] = None
    valueSampledData: Optional[SampledData] = None
    valueString: Optional[str] = None
    valueTime: Optional[FHIRDate] = None

    def elementProperties(self):
        js = super(ObservationComponent, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("dataAbsentReason", "dataAbsentReason", CodeableConcept, False, None, False),
            ("interpretation", "interpretation", CodeableConcept, True, None, False),
            ("referenceRange", "referenceRange", ObservationReferenceRange, True, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", CodeableConcept, False, "value", False),
            ("valueDateTime", "valueDateTime", FHIRDate, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valuePeriod", "valuePeriod", Period, False, "value", False),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", False),
            ("valueRange", "valueRange", Range, False, "value", False),
            ("valueRatio", "valueRatio", Ratio, False, "value", False),
            ("valueSampledData", "valueSampledData", SampledData, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueTime", "valueTime", FHIRDate, False, "value", False),
        ])
        return js


@dataclass
class Observation(DomainResource):
    """ Measurements and simple assertions.

    Measurements and simple assertions made about a patient, device or other
    subject.
    """
    resource_type: ClassVar[str] = "Observation"
    basedOn: Optional[List[FHIRReference]] = empty_list()
    bodySite: Optional[CodeableConcept] = None
    category: Optional[List[CodeableConcept]] = empty_list()
    code: CodeableConcept = None
    component: Optional[List[ObservationComponent]] = empty_list()
    dataAbsentReason: Optional[CodeableConcept] = None
    derivedFrom: Optional[List[FHIRReference]] = empty_list()
    device: Optional[FHIRReference] = None
    effectiveDateTime: Optional[FHIRDate] = None
    effectiveInstant: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    effectiveTiming: Optional[Timing] = None
    encounter: Optional[FHIRReference] = None
    focus: Optional[List[FHIRReference]] = empty_list()
    hasMember: Optional[List[FHIRReference]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    interpretation: Optional[List[CodeableConcept]] = empty_list()
    issued: Optional[FHIRDate] = None
    method: Optional[CodeableConcept] = None
    note: Optional[List[Annotation]] = empty_list()
    partOf: Optional[List[FHIRReference]] = empty_list()
    performer: Optional[List[FHIRReference]] = empty_list()
    referenceRange: Optional[List[ObservationReferenceRange]] = empty_list()
    specimen: Optional[FHIRReference] = None
    status: str = None
    subject: Optional[FHIRReference] = None
    valueBoolean: Optional[bool] = None
    valueCodeableConcept: Optional[CodeableConcept] = None
    valueDateTime: Optional[FHIRDate] = None
    valueInteger: Optional[int] = None
    valuePeriod: Optional[Period] = None
    valueQuantity: Optional[Quantity] = None
    valueRange: Optional[Range] = None
    valueRatio: Optional[Ratio] = None
    valueSampledData: Optional[SampledData] = None
    valueString: Optional[str] = None
    valueTime: Optional[FHIRDate] = None

    def elementProperties(self):
        js = super(Observation, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("bodySite", "bodySite", CodeableConcept, False, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("code", "code", CodeableConcept, False, None, True),
            ("component", "component", ObservationComponent, True, None, False),
            ("dataAbsentReason", "dataAbsentReason", CodeableConcept, False, None, False),
            ("derivedFrom", "derivedFrom", FHIRReference, True, None, False),
            ("device", "device", FHIRReference, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", FHIRDate, False, "effective", False),
            ("effectiveInstant", "effectiveInstant", FHIRDate, False, "effective", False),
            ("effectivePeriod", "effectivePeriod", Period, False, "effective", False),
            ("effectiveTiming", "effectiveTiming", Timing, False, "effective", False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("focus", "focus", FHIRReference, True, None, False),
            ("hasMember", "hasMember", FHIRReference, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("interpretation", "interpretation", CodeableConcept, True, None, False),
            ("issued", "issued", FHIRDate, False, None, False),
            ("method", "method", CodeableConcept, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("performer", "performer", FHIRReference, True, None, False),
            ("referenceRange", "referenceRange", ObservationReferenceRange, True, None, False),
            ("specimen", "specimen", FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", CodeableConcept, False, "value", False),
            ("valueDateTime", "valueDateTime", FHIRDate, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valuePeriod", "valuePeriod", Period, False, "value", False),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", False),
            ("valueRange", "valueRange", Range, False, "value", False),
            ("valueRatio", "valueRatio", Ratio, False, "value", False),
            ("valueSampledData", "valueSampledData", SampledData, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueTime", "valueTime", FHIRDate, False, "value", False),
        ])
        return js