#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/PlanDefinition) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import age
from . import backboneelement
from . import codeableconcept
from . import contactdetail
from . import datarequirement
from . import domainresource
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
from . import relatedartifact
from . import timing
from . import triggerdefinition
from . import usagecontext

from . import domainresource

@dataclass
class PlanDefinition(domainresource.DomainResource):
    """ The definition of a plan for a series of actions, independent of any
    specific patient or context.

    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical artifacts
    such as clinical decision support rules, order sets and protocols.
    """
    resource_type: ClassVar[str] = "PlanDefinition"
    action: Optional[List[PlanDefinitionAction]] = empty_list()
    approvalDate: Optional[fhirdate.FHIRDate] = None
    author: Optional[List[contactdetail.ContactDetail]] = empty_list()
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[fhirdate.FHIRDate] = None
    description: Optional[str] = None
    editor: Optional[List[contactdetail.ContactDetail]] = empty_list()
    effectivePeriod: Optional[period.Period] = None
    endorser: Optional[List[contactdetail.ContactDetail]] = empty_list()
    experimental: Optional[bool] = None
    goal: Optional[List[PlanDefinitionGoal]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    lastReviewDate: Optional[fhirdate.FHIRDate] = None
    library: Optional[List[str]] = empty_list()
    name: Optional[str] = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    relatedArtifact: Optional[List[relatedartifact.RelatedArtifact]] = empty_list()
    reviewer: Optional[List[contactdetail.ContactDetail]] = empty_list()
    status: str = None
    subjectCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    subjectReference: Optional[fhirreference.FHIRReference] = None
    subtitle: Optional[str] = None
    title: Optional[str] = None
    topic: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    type: Optional[codeableconcept.CodeableConcept] = None
    url: Optional[str] = None
    usage: Optional[str] = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(PlanDefinition, self).elementProperties()
        js.extend([
            ("action", "action", PlanDefinitionAction, True, None, False),
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("goal", "goal", PlanDefinitionGoal, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("library", "library", str, True, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("status", "status", str, False, None, True),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("subtitle", "subtitle", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class PlanDefinitionAction(backboneelement.BackboneElement):
    """ Action defined by the plan.

    An action or group of actions to be taken as part of the plan.
    """
    resource_type: ClassVar[str] = "PlanDefinitionAction"
    action: Optional[List[PlanDefinitionAction]] = empty_list()
    cardinalityBehavior: Optional[str] = None
    code: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    condition: Optional[List[PlanDefinitionActionCondition]] = empty_list()
    definitionCanonical: Optional[str] = None
    definitionUri: Optional[str] = None
    description: Optional[str] = None
    documentation: Optional[List[relatedartifact.RelatedArtifact]] = empty_list()
    dynamicValue: Optional[List[PlanDefinitionActionDynamicValue]] = empty_list()
    goalId: Optional[List[str]] = empty_list()
    groupingBehavior: Optional[str] = None
    input: Optional[List[datarequirement.DataRequirement]] = empty_list()
    output: Optional[List[datarequirement.DataRequirement]] = empty_list()
    participant: Optional[List[PlanDefinitionActionParticipant]] = empty_list()
    precheckBehavior: Optional[str] = None
    prefix: Optional[str] = None
    priority: Optional[str] = None
    reason: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    relatedAction: Optional[List[PlanDefinitionActionRelatedAction]] = empty_list()
    requiredBehavior: Optional[str] = None
    selectionBehavior: Optional[str] = None
    subjectCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    subjectReference: Optional[fhirreference.FHIRReference] = None
    textEquivalent: Optional[str] = None
    timingAge: Optional[age.Age] = None
    timingDateTime: Optional[fhirdate.FHIRDate] = None
    timingDuration: Optional[duration.Duration] = None
    timingPeriod: Optional[period.Period] = None
    timingRange: Optional[range.Range] = None
    timingTiming: Optional[timing.Timing] = None
    title: Optional[str] = None
    transform: Optional[str] = None
    trigger: Optional[List[triggerdefinition.TriggerDefinition]] = empty_list()
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(PlanDefinitionAction, self).elementProperties()
        js.extend([
            ("action", "action", PlanDefinitionAction, True, None, False),
            ("cardinalityBehavior", "cardinalityBehavior", str, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("condition", "condition", PlanDefinitionActionCondition, True, None, False),
            ("definitionCanonical", "definitionCanonical", str, False, "definition", False),
            ("definitionUri", "definitionUri", str, False, "definition", False),
            ("description", "description", str, False, None, False),
            ("documentation", "documentation", relatedartifact.RelatedArtifact, True, None, False),
            ("dynamicValue", "dynamicValue", PlanDefinitionActionDynamicValue, True, None, False),
            ("goalId", "goalId", str, True, None, False),
            ("groupingBehavior", "groupingBehavior", str, False, None, False),
            ("input", "input", datarequirement.DataRequirement, True, None, False),
            ("output", "output", datarequirement.DataRequirement, True, None, False),
            ("participant", "participant", PlanDefinitionActionParticipant, True, None, False),
            ("precheckBehavior", "precheckBehavior", str, False, None, False),
            ("prefix", "prefix", str, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False),
            ("relatedAction", "relatedAction", PlanDefinitionActionRelatedAction, True, None, False),
            ("requiredBehavior", "requiredBehavior", str, False, None, False),
            ("selectionBehavior", "selectionBehavior", str, False, None, False),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("timingAge", "timingAge", age.Age, False, "timing", False),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("timingDuration", "timingDuration", duration.Duration, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingRange", "timingRange", range.Range, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("title", "title", str, False, None, False),
            ("transform", "transform", str, False, None, False),
            ("trigger", "trigger", triggerdefinition.TriggerDefinition, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class PlanDefinitionActionCondition(backboneelement.BackboneElement):
    """ Whether or not the action is applicable.

    An expression that describes applicability criteria or start/stop
    conditions for the action.
    """
    resource_type: ClassVar[str] = "PlanDefinitionActionCondition"
    expression: Optional[expression.Expression] = None
    kind: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(PlanDefinitionActionCondition, self).elementProperties()
        js.extend([
            ("expression", "expression", expression.Expression, False, None, False),
            ("kind", "kind", str, False, None, True),
        ])
        return js

@dataclass
class PlanDefinitionActionDynamicValue(backboneelement.BackboneElement):
    """ Dynamic aspects of the definition.

    Customizations that should be applied to the statically defined resource.
    For example, if the dosage of a medication must be computed based on the
    patient's weight, a customization would be used to specify an expression
    that calculated the weight, and the path on the resource that would contain
    the result.
    """
    resource_type: ClassVar[str] = "PlanDefinitionActionDynamicValue"
    expression: Optional[expression.Expression] = None
    path: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(PlanDefinitionActionDynamicValue, self).elementProperties()
        js.extend([
            ("expression", "expression", expression.Expression, False, None, False),
            ("path", "path", str, False, None, False),
        ])
        return js

@dataclass
class PlanDefinitionActionParticipant(backboneelement.BackboneElement):
    """ Who should participate in the action.

    Indicates who should participate in performing the action described.
    """
    resource_type: ClassVar[str] = "PlanDefinitionActionParticipant"
    role: Optional[codeableconcept.CodeableConcept] = None
    type: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(PlanDefinitionActionParticipant, self).elementProperties()
        js.extend([
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js

@dataclass
class PlanDefinitionActionRelatedAction(backboneelement.BackboneElement):
    """ Relationship to another action.

    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """
    resource_type: ClassVar[str] = "PlanDefinitionActionRelatedAction"
    actionId: str = None
    offsetDuration: Optional[duration.Duration] = None
    offsetRange: Optional[range.Range] = None
    relationship: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(PlanDefinitionActionRelatedAction, self).elementProperties()
        js.extend([
            ("actionId", "actionId", str, False, None, True),
            ("offsetDuration", "offsetDuration", duration.Duration, False, "offset", False),
            ("offsetRange", "offsetRange", range.Range, False, "offset", False),
            ("relationship", "relationship", str, False, None, True),
        ])
        return js

@dataclass
class PlanDefinitionGoal(backboneelement.BackboneElement):
    """ What the plan is trying to accomplish.

    Goals that describe what the activities within the plan are intended to
    achieve. For example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """
    resource_type: ClassVar[str] = "PlanDefinitionGoal"
    addresses: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    category: Optional[codeableconcept.CodeableConcept] = None
    description:codeableconcept.CodeableConcept = None
    documentation: Optional[List[relatedartifact.RelatedArtifact]] = empty_list()
    priority: Optional[codeableconcept.CodeableConcept] = None
    start: Optional[codeableconcept.CodeableConcept] = None
    target: Optional[List[PlanDefinitionGoalTarget]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(PlanDefinitionGoal, self).elementProperties()
        js.extend([
            ("addresses", "addresses", codeableconcept.CodeableConcept, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("description", "description", codeableconcept.CodeableConcept, False, None, True),
            ("documentation", "documentation", relatedartifact.RelatedArtifact, True, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("start", "start", codeableconcept.CodeableConcept, False, None, False),
            ("target", "target", PlanDefinitionGoalTarget, True, None, False),
        ])
        return js

@dataclass
class PlanDefinitionGoalTarget(backboneelement.BackboneElement):
    """ Target outcome for the goal.

    Indicates what should be done and within what timeframe.
    """
    resource_type: ClassVar[str] = "PlanDefinitionGoalTarget"
    detailCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    detailQuantity: Optional[quantity.Quantity] = None
    detailRange: Optional[range.Range] = None
    due: Optional[duration.Duration] = None
    measure: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(PlanDefinitionGoalTarget, self).elementProperties()
        js.extend([
            ("detailCodeableConcept", "detailCodeableConcept", codeableconcept.CodeableConcept, False, "detail", False),
            ("detailQuantity", "detailQuantity", quantity.Quantity, False, "detail", False),
            ("detailRange", "detailRange", range.Range, False, "detail", False),
            ("due", "due", duration.Duration, False, None, False),
            ("measure", "measure", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + '.age']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + '.datarequirement']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import expression
except ImportError:
    expression = sys.modules[__package__ + '.expression']
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
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
try:
    from . import triggerdefinition
except ImportError:
    triggerdefinition = sys.modules[__package__ + '.triggerdefinition']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']