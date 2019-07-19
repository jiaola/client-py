#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/RequestGroup) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .age import Age
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .duration import Duration
from .expression import Expression
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .range import Range
from .relatedartifact import RelatedArtifact
from .timing import Timing


@dataclass
class RequestGroupActionRelatedAction(BackboneElement):
    """ Relationship to another action.

    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """
    resource_type: ClassVar[str] = "RequestGroupActionRelatedAction"
    actionId: str = None
    offsetDuration: Optional[Duration] = None
    offsetRange: Optional[Range] = None
    relationship: str = None

    def elementProperties(self):
        js = super(RequestGroupActionRelatedAction, self).elementProperties()
        js.extend([
            ("actionId", "actionId", str, False, None, True),
            ("offsetDuration", "offsetDuration", Duration, False, "offset", False),
            ("offsetRange", "offsetRange", Range, False, "offset", False),
            ("relationship", "relationship", str, False, None, True),
        ])
        return js


@dataclass
class RequestGroupActionCondition(BackboneElement):
    """ Whether or not the action is applicable.

    An expression that describes applicability criteria, or start/stop
    conditions for the action.
    """
    resource_type: ClassVar[str] = "RequestGroupActionCondition"
    expression: Optional[Expression] = None
    kind: str = None

    def elementProperties(self):
        js = super(RequestGroupActionCondition, self).elementProperties()
        js.extend([
            ("expression", "expression", Expression, False, None, False),
            ("kind", "kind", str, False, None, True),
        ])
        return js


@dataclass
class RequestGroupAction(BackboneElement):
    """ Proposed actions, if any.

    The actions, if any, produced by the evaluation of the artifact.
    """
    resource_type: ClassVar[str] = "RequestGroupAction"
    action: Optional[List[RequestGroupAction]] = empty_list()
    cardinalityBehavior: Optional[str] = None
    code: Optional[List[CodeableConcept]] = empty_list()
    condition: Optional[List[RequestGroupActionCondition]] = empty_list()
    description: Optional[str] = None
    documentation: Optional[List[RelatedArtifact]] = empty_list()
    groupingBehavior: Optional[str] = None
    participant: Optional[List[FHIRReference]] = empty_list()
    precheckBehavior: Optional[str] = None
    prefix: Optional[str] = None
    priority: Optional[str] = None
    relatedAction: Optional[List[RequestGroupActionRelatedAction]] = empty_list()
    requiredBehavior: Optional[str] = None
    resource: Optional[FHIRReference] = None
    selectionBehavior: Optional[str] = None
    textEquivalent: Optional[str] = None
    timingAge: Optional[Age] = None
    timingDateTime: Optional[FHIRDate] = None
    timingDuration: Optional[Duration] = None
    timingPeriod: Optional[Period] = None
    timingRange: Optional[Range] = None
    timingTiming: Optional[Timing] = None
    title: Optional[str] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(RequestGroupAction, self).elementProperties()
        js.extend([
            ("action", "action", RequestGroupAction, True, None, False),
            ("cardinalityBehavior", "cardinalityBehavior", str, False, None, False),
            ("code", "code", CodeableConcept, True, None, False),
            ("condition", "condition", RequestGroupActionCondition, True, None, False),
            ("description", "description", str, False, None, False),
            ("documentation", "documentation", RelatedArtifact, True, None, False),
            ("groupingBehavior", "groupingBehavior", str, False, None, False),
            ("participant", "participant", FHIRReference, True, None, False),
            ("precheckBehavior", "precheckBehavior", str, False, None, False),
            ("prefix", "prefix", str, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("relatedAction", "relatedAction", RequestGroupActionRelatedAction, True, None, False),
            ("requiredBehavior", "requiredBehavior", str, False, None, False),
            ("resource", "resource", FHIRReference, False, None, False),
            ("selectionBehavior", "selectionBehavior", str, False, None, False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("timingAge", "timingAge", Age, False, "timing", False),
            ("timingDateTime", "timingDateTime", FHIRDate, False, "timing", False),
            ("timingDuration", "timingDuration", Duration, False, "timing", False),
            ("timingPeriod", "timingPeriod", Period, False, "timing", False),
            ("timingRange", "timingRange", Range, False, "timing", False),
            ("timingTiming", "timingTiming", Timing, False, "timing", False),
            ("title", "title", str, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class RequestGroup(DomainResource):
    """ A group of related requests.

    A group of related requests that can be used to capture intended activities
    that have inter-dependencies such as "give this medication after that one".
    """
    resource_type: ClassVar[str] = "RequestGroup"
    action: Optional[List[RequestGroupAction]] = empty_list()
    author: Optional[FHIRReference] = None
    authoredOn: Optional[FHIRDate] = None
    basedOn: Optional[List[FHIRReference]] = empty_list()
    code: Optional[CodeableConcept] = None
    encounter: Optional[FHIRReference] = None
    groupIdentifier: Optional[Identifier] = None
    identifier: Optional[List[Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    intent: str = None
    note: Optional[List[Annotation]] = empty_list()
    priority: Optional[str] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    replaces: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    subject: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(RequestGroup, self).elementProperties()
        js.extend([
            ("action", "action", RequestGroupAction, True, None, False),
            ("author", "author", FHIRReference, False, None, False),
            ("authoredOn", "authoredOn", FHIRDate, False, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("groupIdentifier", "groupIdentifier", Identifier, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("note", "note", Annotation, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("replaces", "replaces", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, False),
        ])
        return js