#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/PlanDefinition) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .age import Age
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .datarequirement import DataRequirement
from .domainresource import DomainResource
from .duration import Duration
from .expression import Expression
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .range import Range
from .relatedartifact import RelatedArtifact
from .timing import Timing
from .triggerdefinition import TriggerDefinition
from .usagecontext import UsageContext


@dataclass
class PlanDefinitionGoalTarget(BackboneElement):
    """ Target outcome for the goal.

    Indicates what should be done and within what timeframe.
    """
    resource_type: ClassVar[str] = "PlanDefinitionGoalTarget"
    detailCodeableConcept: Optional[CodeableConcept] = None
    detailQuantity: Optional[Quantity] = None
    detailRange: Optional[Range] = None
    due: Optional[Duration] = None
    measure: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(PlanDefinitionGoalTarget, self).elementProperties()
        js.extend([
            ("detailCodeableConcept", "detailCodeableConcept", CodeableConcept, False, "detail", False),
            ("detailQuantity", "detailQuantity", Quantity, False, "detail", False),
            ("detailRange", "detailRange", Range, False, "detail", False),
            ("due", "due", Duration, False, None, False),
            ("measure", "measure", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class PlanDefinitionGoal(BackboneElement):
    """ What the plan is trying to accomplish.

    Goals that describe what the activities within the plan are intended to
    achieve. For example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """
    resource_type: ClassVar[str] = "PlanDefinitionGoal"
    addresses: Optional[List[CodeableConcept]] = empty_list()
    category: Optional[CodeableConcept] = None
    description: CodeableConcept = None
    documentation: Optional[List[RelatedArtifact]] = empty_list()
    priority: Optional[CodeableConcept] = None
    start: Optional[CodeableConcept] = None
    target: Optional[List[PlanDefinitionGoalTarget]] = empty_list()

    def elementProperties(self):
        js = super(PlanDefinitionGoal, self).elementProperties()
        js.extend([
            ("addresses", "addresses", CodeableConcept, True, None, False),
            ("category", "category", CodeableConcept, False, None, False),
            ("description", "description", CodeableConcept, False, None, True),
            ("documentation", "documentation", RelatedArtifact, True, None, False),
            ("priority", "priority", CodeableConcept, False, None, False),
            ("start", "start", CodeableConcept, False, None, False),
            ("target", "target", PlanDefinitionGoalTarget, True, None, False),
        ])
        return js


@dataclass
class PlanDefinitionActionRelatedAction(BackboneElement):
    """ Relationship to another action.

    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """
    resource_type: ClassVar[str] = "PlanDefinitionActionRelatedAction"
    actionId: str = None
    offsetDuration: Optional[Duration] = None
    offsetRange: Optional[Range] = None
    relationship: str = None

    def elementProperties(self):
        js = super(PlanDefinitionActionRelatedAction, self).elementProperties()
        js.extend([
            ("actionId", "actionId", str, False, None, True),
            ("offsetDuration", "offsetDuration", Duration, False, "offset", False),
            ("offsetRange", "offsetRange", Range, False, "offset", False),
            ("relationship", "relationship", str, False, None, True),
        ])
        return js


@dataclass
class PlanDefinitionActionParticipant(BackboneElement):
    """ Who should participate in the action.

    Indicates who should participate in performing the action described.
    """
    resource_type: ClassVar[str] = "PlanDefinitionActionParticipant"
    role: Optional[CodeableConcept] = None
    type: str = None

    def elementProperties(self):
        js = super(PlanDefinitionActionParticipant, self).elementProperties()
        js.extend([
            ("role", "role", CodeableConcept, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


@dataclass
class PlanDefinitionActionDynamicValue(BackboneElement):
    """ Dynamic aspects of the definition.

    Customizations that should be applied to the statically defined resource.
    For example, if the dosage of a medication must be computed based on the
    patient's weight, a customization would be used to specify an expression
    that calculated the weight, and the path on the resource that would contain
    the result.
    """
    resource_type: ClassVar[str] = "PlanDefinitionActionDynamicValue"
    expression: Optional[Expression] = None
    path: Optional[str] = None

    def elementProperties(self):
        js = super(PlanDefinitionActionDynamicValue, self).elementProperties()
        js.extend([
            ("expression", "expression", Expression, False, None, False),
            ("path", "path", str, False, None, False),
        ])
        return js


@dataclass
class PlanDefinitionActionCondition(BackboneElement):
    """ Whether or not the action is applicable.

    An expression that describes applicability criteria or start/stop
    conditions for the action.
    """
    resource_type: ClassVar[str] = "PlanDefinitionActionCondition"
    expression: Optional[Expression] = None
    kind: str = None

    def elementProperties(self):
        js = super(PlanDefinitionActionCondition, self).elementProperties()
        js.extend([
            ("expression", "expression", Expression, False, None, False),
            ("kind", "kind", str, False, None, True),
        ])
        return js


@dataclass
class PlanDefinitionAction(BackboneElement):
    """ Action defined by the plan.

    An action or group of actions to be taken as part of the plan.
    """
    resource_type: ClassVar[str] = "PlanDefinitionAction"
    action: Optional[List[PlanDefinitionAction]] = empty_list()
    cardinalityBehavior: Optional[str] = None
    code: Optional[List[CodeableConcept]] = empty_list()
    condition: Optional[List[PlanDefinitionActionCondition]] = empty_list()
    definitionCanonical: Optional[str] = None
    definitionUri: Optional[str] = None
    description: Optional[str] = None
    documentation: Optional[List[RelatedArtifact]] = empty_list()
    dynamicValue: Optional[List[PlanDefinitionActionDynamicValue]] = empty_list()
    goalId: Optional[List[str]] = empty_list()
    groupingBehavior: Optional[str] = None
    input: Optional[List[DataRequirement]] = empty_list()
    output: Optional[List[DataRequirement]] = empty_list()
    participant: Optional[List[PlanDefinitionActionParticipant]] = empty_list()
    precheckBehavior: Optional[str] = None
    prefix: Optional[str] = None
    priority: Optional[str] = None
    reason: Optional[List[CodeableConcept]] = empty_list()
    relatedAction: Optional[List[PlanDefinitionActionRelatedAction]] = empty_list()
    requiredBehavior: Optional[str] = None
    selectionBehavior: Optional[str] = None
    subjectCodeableConcept: Optional[CodeableConcept] = None
    subjectReference: Optional[FHIRReference] = None
    textEquivalent: Optional[str] = None
    timingAge: Optional[Age] = None
    timingDateTime: Optional[FHIRDate] = None
    timingDuration: Optional[Duration] = None
    timingPeriod: Optional[Period] = None
    timingRange: Optional[Range] = None
    timingTiming: Optional[Timing] = None
    title: Optional[str] = None
    transform: Optional[str] = None
    trigger: Optional[List[TriggerDefinition]] = empty_list()
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(PlanDefinitionAction, self).elementProperties()
        js.extend([
            ("action", "action", PlanDefinitionAction, True, None, False),
            ("cardinalityBehavior", "cardinalityBehavior", str, False, None, False),
            ("code", "code", CodeableConcept, True, None, False),
            ("condition", "condition", PlanDefinitionActionCondition, True, None, False),
            ("definitionCanonical", "definitionCanonical", str, False, "definition", False),
            ("definitionUri", "definitionUri", str, False, "definition", False),
            ("description", "description", str, False, None, False),
            ("documentation", "documentation", RelatedArtifact, True, None, False),
            ("dynamicValue", "dynamicValue", PlanDefinitionActionDynamicValue, True, None, False),
            ("goalId", "goalId", str, True, None, False),
            ("groupingBehavior", "groupingBehavior", str, False, None, False),
            ("input", "input", DataRequirement, True, None, False),
            ("output", "output", DataRequirement, True, None, False),
            ("participant", "participant", PlanDefinitionActionParticipant, True, None, False),
            ("precheckBehavior", "precheckBehavior", str, False, None, False),
            ("prefix", "prefix", str, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("reason", "reason", CodeableConcept, True, None, False),
            ("relatedAction", "relatedAction", PlanDefinitionActionRelatedAction, True, None, False),
            ("requiredBehavior", "requiredBehavior", str, False, None, False),
            ("selectionBehavior", "selectionBehavior", str, False, None, False),
            ("subjectCodeableConcept", "subjectCodeableConcept", CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", FHIRReference, False, "subject", False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("timingAge", "timingAge", Age, False, "timing", False),
            ("timingDateTime", "timingDateTime", FHIRDate, False, "timing", False),
            ("timingDuration", "timingDuration", Duration, False, "timing", False),
            ("timingPeriod", "timingPeriod", Period, False, "timing", False),
            ("timingRange", "timingRange", Range, False, "timing", False),
            ("timingTiming", "timingTiming", Timing, False, "timing", False),
            ("title", "title", str, False, None, False),
            ("transform", "transform", str, False, None, False),
            ("trigger", "trigger", TriggerDefinition, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class PlanDefinition(DomainResource):
    """ The definition of a plan for a series of actions, independent of any
    specific patient or context.

    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical artifacts
    such as clinical decision support rules, order sets and protocols.
    """
    resource_type: ClassVar[str] = "PlanDefinition"
    action: Optional[List[PlanDefinitionAction]] = empty_list()
    approvalDate: Optional[FHIRDate] = None
    author: Optional[List[ContactDetail]] = empty_list()
    contact: Optional[List[ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[FHIRDate] = None
    description: Optional[str] = None
    editor: Optional[List[ContactDetail]] = empty_list()
    effectivePeriod: Optional[Period] = None
    endorser: Optional[List[ContactDetail]] = empty_list()
    experimental: Optional[bool] = None
    goal: Optional[List[PlanDefinitionGoal]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    lastReviewDate: Optional[FHIRDate] = None
    library: Optional[List[str]] = empty_list()
    name: Optional[str] = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    relatedArtifact: Optional[List[RelatedArtifact]] = empty_list()
    reviewer: Optional[List[ContactDetail]] = empty_list()
    status: str = None
    subjectCodeableConcept: Optional[CodeableConcept] = None
    subjectReference: Optional[FHIRReference] = None
    subtitle: Optional[str] = None
    title: Optional[str] = None
    topic: Optional[List[CodeableConcept]] = empty_list()
    type: Optional[CodeableConcept] = None
    url: Optional[str] = None
    usage: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    version: Optional[str] = None

    def elementProperties(self):
        js = super(PlanDefinition, self).elementProperties()
        js.extend([
            ("action", "action", PlanDefinitionAction, True, None, False),
            ("approvalDate", "approvalDate", FHIRDate, False, None, False),
            ("author", "author", ContactDetail, True, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("editor", "editor", ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", Period, False, None, False),
            ("endorser", "endorser", ContactDetail, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("goal", "goal", PlanDefinitionGoal, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", FHIRDate, False, None, False),
            ("library", "library", str, True, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", ContactDetail, True, None, False),
            ("status", "status", str, False, None, True),
            ("subjectCodeableConcept", "subjectCodeableConcept", CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", FHIRReference, False, "subject", False),
            ("subtitle", "subtitle", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", CodeableConcept, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js