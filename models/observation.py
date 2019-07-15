#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Observation) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
from . import ratio
from . import sampleddata
from . import timing

from . import domainresource

@dataclass
class Observation(domainresource.DomainResource):
    """ Measurements and simple assertions.

    Measurements and simple assertions made about a patient, device or other
    subject.
    """
    resource_type: ClassVar[str] = "Observation"
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    bodySite: Optional[codeableconcept.CodeableConcept] = None
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    code:codeableconcept.CodeableConcept = None
    component: Optional[List[ObservationComponent]] = empty_list()
    dataAbsentReason: Optional[codeableconcept.CodeableConcept] = None
    derivedFrom: Optional[List[fhirreference.FHIRReference]] = empty_list()
    device: Optional[fhirreference.FHIRReference] = None
    effectiveDateTime: Optional[fhirdate.FHIRDate] = None
    effectiveInstant: Optional[fhirdate.FHIRDate] = None
    effectivePeriod: Optional[period.Period] = None
    effectiveTiming: Optional[timing.Timing] = None
    encounter: Optional[fhirreference.FHIRReference] = None
    focus: Optional[List[fhirreference.FHIRReference]] = empty_list()
    hasMember: Optional[List[fhirreference.FHIRReference]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    interpretation: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    issued: Optional[fhirdate.FHIRDate] = None
    method: Optional[codeableconcept.CodeableConcept] = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    partOf: Optional[List[fhirreference.FHIRReference]] = empty_list()
    performer: Optional[List[fhirreference.FHIRReference]] = empty_list()
    referenceRange: Optional[List[ObservationReferenceRange]] = empty_list()
    specimen: Optional[fhirreference.FHIRReference] = None
    status: str = None
    subject: Optional[fhirreference.FHIRReference] = None
    valueBoolean: Optional[bool] = None
    valueCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    valueDateTime: Optional[fhirdate.FHIRDate] = None
    valueInteger: Optional[int] = None
    valuePeriod: Optional[period.Period] = None
    valueQuantity: Optional[quantity.Quantity] = None
    valueRange: Optional[range.Range] = None
    valueRatio: Optional[ratio.Ratio] = None
    valueSampledData: Optional[sampleddata.SampledData] = None
    valueString: Optional[str] = None
    valueTime: Optional[fhirdate.FHIRDate] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Observation, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("component", "component", ObservationComponent, True, None, False),
            ("dataAbsentReason", "dataAbsentReason", codeableconcept.CodeableConcept, False, None, False),
            ("derivedFrom", "derivedFrom", fhirreference.FHIRReference, True, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", fhirdate.FHIRDate, False, "effective", False),
            ("effectiveInstant", "effectiveInstant", fhirdate.FHIRDate, False, "effective", False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", False),
            ("effectiveTiming", "effectiveTiming", timing.Timing, False, "effective", False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("focus", "focus", fhirreference.FHIRReference, True, None, False),
            ("hasMember", "hasMember", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("interpretation", "interpretation", codeableconcept.CodeableConcept, True, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("referenceRange", "referenceRange", ObservationReferenceRange, True, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", False),
        ])
        return js

from . import backboneelement

@dataclass
class ObservationComponent(backboneelement.BackboneElement):
    """ Component results.

    Some observations have multiple component observations.  These component
    observations are expressed as separate code value pairs that share the same
    attributes.  Examples include systolic and diastolic component observations
    for blood pressure measurement and multiple component observations for
    genetics observations.
    """
    resource_type: ClassVar[str] = "ObservationComponent"
    code:codeableconcept.CodeableConcept = None
    dataAbsentReason: Optional[codeableconcept.CodeableConcept] = None
    interpretation: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    referenceRange: Optional[List[ObservationReferenceRange]] = empty_list()
    valueBoolean: Optional[bool] = None
    valueCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    valueDateTime: Optional[fhirdate.FHIRDate] = None
    valueInteger: Optional[int] = None
    valuePeriod: Optional[period.Period] = None
    valueQuantity: Optional[quantity.Quantity] = None
    valueRange: Optional[range.Range] = None
    valueRatio: Optional[ratio.Ratio] = None
    valueSampledData: Optional[sampleddata.SampledData] = None
    valueString: Optional[str] = None
    valueTime: Optional[fhirdate.FHIRDate] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ObservationComponent, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("dataAbsentReason", "dataAbsentReason", codeableconcept.CodeableConcept, False, None, False),
            ("interpretation", "interpretation", codeableconcept.CodeableConcept, True, None, False),
            ("referenceRange", "referenceRange", ObservationReferenceRange, True, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", False),
        ])
        return js

@dataclass
class ObservationReferenceRange(backboneelement.BackboneElement):
    """ Provides guide for interpretation.

    Guidance on how to interpret the value by comparison to a normal or
    recommended range.  Multiple reference ranges are interpreted as an "OR".
    In other words, to represent two distinct target populations, two
    `referenceRange` elements would be used.
    """
    resource_type: ClassVar[str] = "ObservationReferenceRange"
    age: Optional[range.Range] = None
    appliesTo: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    high: Optional[quantity.Quantity] = None
    low: Optional[quantity.Quantity] = None
    text: Optional[str] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ObservationReferenceRange, self).elementProperties()
        js.extend([
            ("age", "age", range.Range, False, None, False),
            ("appliesTo", "appliesTo", codeableconcept.CodeableConcept, True, None, False),
            ("high", "high", quantity.Quantity, False, None, False),
            ("low", "low", quantity.Quantity, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
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
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
try:
    from . import sampleddata
except ImportError:
    sampleddata = sys.modules[__package__ + '.sampleddata']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']