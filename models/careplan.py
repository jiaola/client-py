#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CarePlan) on 2019-07-15.
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
from . import timing

from . import domainresource

@dataclass
class CarePlan(domainresource.DomainResource):
    """ Healthcare plan for patient or group.

    Describes the intention of how one or more practitioners intend to deliver
    care for a particular patient, group or community for a period of time,
    possibly limited to care for a specific condition or set of conditions.
    """
    resource_type: ClassVar[str] = "CarePlan"
    activity: Optional[List[CarePlanActivity]] = empty_list()
    addresses: Optional[List[fhirreference.FHIRReference]] = empty_list()
    author: Optional[fhirreference.FHIRReference] = None
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    careTeam: Optional[List[fhirreference.FHIRReference]] = empty_list()
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    contributor: Optional[List[fhirreference.FHIRReference]] = empty_list()
    created: Optional[fhirdate.FHIRDate] = None
    description: Optional[str] = None
    encounter: Optional[fhirreference.FHIRReference] = None
    goal: Optional[List[fhirreference.FHIRReference]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    intent: str = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    partOf: Optional[List[fhirreference.FHIRReference]] = empty_list()
    period: Optional[period.Period] = None
    replaces: Optional[List[fhirreference.FHIRReference]] = empty_list()
    status: str = None
    subject:fhirreference.FHIRReference = None
    supportingInfo: Optional[List[fhirreference.FHIRReference]] = empty_list()
    title: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CarePlan, self).elementProperties()
        js.extend([
            ("activity", "activity", CarePlanActivity, True, None, False),
            ("addresses", "addresses", fhirreference.FHIRReference, True, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("careTeam", "careTeam", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("contributor", "contributor", fhirreference.FHIRReference, True, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("goal", "goal", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
            ("title", "title", str, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class CarePlanActivity(backboneelement.BackboneElement):
    """ Action to occur as part of plan.

    Identifies a planned action to occur as part of the plan.  For example, a
    medication to be used, lab tests to perform, self-monitoring, education,
    etc.
    """
    resource_type: ClassVar[str] = "CarePlanActivity"
    detail: Optional[CarePlanActivityDetail] = None
    outcomeCodeableConcept: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    outcomeReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    progress: Optional[List[annotation.Annotation]] = empty_list()
    reference: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CarePlanActivity, self).elementProperties()
        js.extend([
            ("detail", "detail", CarePlanActivityDetail, False, None, False),
            ("outcomeCodeableConcept", "outcomeCodeableConcept", codeableconcept.CodeableConcept, True, None, False),
            ("outcomeReference", "outcomeReference", fhirreference.FHIRReference, True, None, False),
            ("progress", "progress", annotation.Annotation, True, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, False),
        ])
        return js

@dataclass
class CarePlanActivityDetail(backboneelement.BackboneElement):
    """ In-line definition of activity.

    A simple summary of a planned activity suitable for a general care plan
    system (e.g. form driven) that doesn't know about specific resources such
    as procedure etc.
    """
    resource_type: ClassVar[str] = "CarePlanActivityDetail"
    code: Optional[codeableconcept.CodeableConcept] = None
    dailyAmount: Optional[quantity.Quantity] = None
    description: Optional[str] = None
    doNotPerform: Optional[bool] = None
    goal: Optional[List[fhirreference.FHIRReference]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    kind: Optional[str] = None
    location: Optional[fhirreference.FHIRReference] = None
    performer: Optional[List[fhirreference.FHIRReference]] = empty_list()
    productCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    productReference: Optional[fhirreference.FHIRReference] = None
    quantity: Optional[quantity.Quantity] = None
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    scheduledPeriod: Optional[period.Period] = None
    scheduledString: Optional[str] = None
    scheduledTiming: Optional[timing.Timing] = None
    status: str = None
    statusReason: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CarePlanActivityDetail, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("dailyAmount", "dailyAmount", quantity.Quantity, False, None, False),
            ("description", "description", str, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("goal", "goal", fhirreference.FHIRReference, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("kind", "kind", str, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("productCodeableConcept", "productCodeableConcept", codeableconcept.CodeableConcept, False, "product", False),
            ("productReference", "productReference", fhirreference.FHIRReference, False, "product", False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("scheduledPeriod", "scheduledPeriod", period.Period, False, "scheduled", False),
            ("scheduledString", "scheduledString", str, False, "scheduled", False),
            ("scheduledTiming", "scheduledTiming", timing.Timing, False, "scheduled", False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
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
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']