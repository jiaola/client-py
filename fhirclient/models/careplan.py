#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CarePlan) on 2019-07-18.
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
from .timing import Timing


@dataclass
class CarePlanActivityDetail(BackboneElement):
    """ In-line definition of activity.

    A simple summary of a planned activity suitable for a general care plan
    system (e.g. form driven) that doesn't know about specific resources such
    as procedure etc.
    """
    resource_type: ClassVar[str] = "CarePlanActivityDetail"
    code: Optional[CodeableConcept] = None
    dailyAmount: Optional[Quantity] = None
    description: Optional[str] = None
    doNotPerform: Optional[bool] = None
    goal: Optional[List[FHIRReference]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    kind: Optional[str] = None
    location: Optional[FHIRReference] = None
    performer: Optional[List[FHIRReference]] = empty_list()
    productCodeableConcept: Optional[CodeableConcept] = None
    productReference: Optional[FHIRReference] = None
    quantity: Optional[Quantity] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    scheduledPeriod: Optional[Period] = None
    scheduledString: Optional[str] = None
    scheduledTiming: Optional[Timing] = None
    status: str = None
    statusReason: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(CarePlanActivityDetail, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, False),
            ("dailyAmount", "dailyAmount", Quantity, False, None, False),
            ("description", "description", str, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("goal", "goal", FHIRReference, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("kind", "kind", str, False, None, False),
            ("location", "location", FHIRReference, False, None, False),
            ("performer", "performer", FHIRReference, True, None, False),
            ("productCodeableConcept", "productCodeableConcept", CodeableConcept, False, "product", False),
            ("productReference", "productReference", FHIRReference, False, "product", False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("scheduledPeriod", "scheduledPeriod", Period, False, "scheduled", False),
            ("scheduledString", "scheduledString", str, False, "scheduled", False),
            ("scheduledTiming", "scheduledTiming", Timing, False, "scheduled", False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class CarePlanActivity(BackboneElement):
    """ Action to occur as part of plan.

    Identifies a planned action to occur as part of the plan.  For example, a
    medication to be used, lab tests to perform, self-monitoring, education,
    etc.
    """
    resource_type: ClassVar[str] = "CarePlanActivity"
    detail: Optional[CarePlanActivityDetail] = None
    outcomeCodeableConcept: Optional[List[CodeableConcept]] = empty_list()
    outcomeReference: Optional[List[FHIRReference]] = empty_list()
    progress: Optional[List[Annotation]] = empty_list()
    reference: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(CarePlanActivity, self).elementProperties()
        js.extend([
            ("detail", "detail", CarePlanActivityDetail, False, None, False),
            ("outcomeCodeableConcept", "outcomeCodeableConcept", CodeableConcept, True, None, False),
            ("outcomeReference", "outcomeReference", FHIRReference, True, None, False),
            ("progress", "progress", Annotation, True, None, False),
            ("reference", "reference", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class CarePlan(DomainResource):
    """ Healthcare plan for patient or group.

    Describes the intention of how one or more practitioners intend to deliver
    care for a particular patient, group or community for a period of time,
    possibly limited to care for a specific condition or set of conditions.
    """
    resource_type: ClassVar[str] = "CarePlan"
    activity: Optional[List[CarePlanActivity]] = empty_list()
    addresses: Optional[List[FHIRReference]] = empty_list()
    author: Optional[FHIRReference] = None
    basedOn: Optional[List[FHIRReference]] = empty_list()
    careTeam: Optional[List[FHIRReference]] = empty_list()
    category: Optional[List[CodeableConcept]] = empty_list()
    contributor: Optional[List[FHIRReference]] = empty_list()
    created: Optional[FHIRDate] = None
    description: Optional[str] = None
    encounter: Optional[FHIRReference] = None
    goal: Optional[List[FHIRReference]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    intent: str = None
    note: Optional[List[Annotation]] = empty_list()
    partOf: Optional[List[FHIRReference]] = empty_list()
    period: Optional[Period] = None
    replaces: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    subject: FHIRReference = None
    supportingInfo: Optional[List[FHIRReference]] = empty_list()
    title: Optional[str] = None

    def elementProperties(self):
        js = super(CarePlan, self).elementProperties()
        js.extend([
            ("activity", "activity", CarePlanActivity, True, None, False),
            ("addresses", "addresses", FHIRReference, True, None, False),
            ("author", "author", FHIRReference, False, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("careTeam", "careTeam", FHIRReference, True, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("contributor", "contributor", FHIRReference, True, None, False),
            ("created", "created", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("goal", "goal", FHIRReference, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("note", "note", Annotation, True, None, False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("period", "period", Period, False, None, False),
            ("replaces", "replaces", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, True),
            ("supportingInfo", "supportingInfo", FHIRReference, True, None, False),
            ("title", "title", str, False, None, False),
        ])
        return js