#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Goal) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .duration import Duration
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .range import Range
from .ratio import Ratio


@dataclass
class GoalTarget(BackboneElement):
    """ Target outcome for the goal.

    Indicates what should be done by when.
    """
    resource_type: ClassVar[str] = "GoalTarget"
    detailBoolean: Optional[bool] = None
    detailCodeableConcept: Optional[CodeableConcept] = None
    detailInteger: Optional[int] = None
    detailQuantity: Optional[Quantity] = None
    detailRange: Optional[Range] = None
    detailRatio: Optional[Ratio] = None
    detailString: Optional[str] = None
    dueDate: Optional[FHIRDate] = None
    dueDuration: Optional[Duration] = None
    measure: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(GoalTarget, self).elementProperties()
        js.extend([
            ("detailBoolean", "detailBoolean", bool, False, "detail", False),
            ("detailCodeableConcept", "detailCodeableConcept", CodeableConcept, False, "detail", False),
            ("detailInteger", "detailInteger", int, False, "detail", False),
            ("detailQuantity", "detailQuantity", Quantity, False, "detail", False),
            ("detailRange", "detailRange", Range, False, "detail", False),
            ("detailRatio", "detailRatio", Ratio, False, "detail", False),
            ("detailString", "detailString", str, False, "detail", False),
            ("dueDate", "dueDate", FHIRDate, False, "due", False),
            ("dueDuration", "dueDuration", Duration, False, "due", False),
            ("measure", "measure", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class Goal(DomainResource):
    """ Describes the intended objective(s) for a patient, group or organization.

    Describes the intended objective(s) for a patient, group or organization
    care, for example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """
    resource_type: ClassVar[str] = "Goal"
    achievementStatus: Optional[CodeableConcept] = None
    addresses: Optional[List[FHIRReference]] = empty_list()
    category: Optional[List[CodeableConcept]] = empty_list()
    description: CodeableConcept = None
    expressedBy: Optional[FHIRReference] = None
    identifier: Optional[List[Identifier]] = empty_list()
    lifecycleStatus: str = None
    note: Optional[List[Annotation]] = empty_list()
    outcomeCode: Optional[List[CodeableConcept]] = empty_list()
    outcomeReference: Optional[List[FHIRReference]] = empty_list()
    priority: Optional[CodeableConcept] = None
    startCodeableConcept: Optional[CodeableConcept] = None
    startDate: Optional[FHIRDate] = None
    statusDate: Optional[FHIRDate] = None
    statusReason: Optional[str] = None
    subject: FHIRReference = None
    target: Optional[List[GoalTarget]] = empty_list()

    def elementProperties(self):
        js = super(Goal, self).elementProperties()
        js.extend([
            ("achievementStatus", "achievementStatus", CodeableConcept, False, None, False),
            ("addresses", "addresses", FHIRReference, True, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("description", "description", CodeableConcept, False, None, True),
            ("expressedBy", "expressedBy", FHIRReference, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("lifecycleStatus", "lifecycleStatus", str, False, None, True),
            ("note", "note", Annotation, True, None, False),
            ("outcomeCode", "outcomeCode", CodeableConcept, True, None, False),
            ("outcomeReference", "outcomeReference", FHIRReference, True, None, False),
            ("priority", "priority", CodeableConcept, False, None, False),
            ("startCodeableConcept", "startCodeableConcept", CodeableConcept, False, "start", False),
            ("startDate", "startDate", FHIRDate, False, "start", False),
            ("statusDate", "statusDate", FHIRDate, False, None, False),
            ("statusReason", "statusReason", str, False, None, False),
            ("subject", "subject", FHIRReference, False, None, True),
            ("target", "target", GoalTarget, True, None, False),
        ])
        return js