#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/RequestGroup) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import age
from . import annotation
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import range
from . import relatedartifact
from . import timing

from . import domainresource

@dataclass
class RequestGroup(domainresource.DomainResource):
    """ A group of related requests.

    A group of related requests that can be used to capture intended activities
    that have inter-dependencies such as "give this medication after that one".
    """
    resource_type: ClassVar[str] = "RequestGroup"
    action: Optional[List[RequestGroupAction]] = empty_list()
    author: Optional[fhirreference.FHIRReference] = None
    authoredOn: Optional[fhirdate.FHIRDate] = None
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    code: Optional[codeableconcept.CodeableConcept] = None
    encounter: Optional[fhirreference.FHIRReference] = None
    groupIdentifier: Optional[identifier.Identifier] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    intent: str = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    priority: Optional[str] = None
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    replaces: Optional[List[fhirreference.FHIRReference]] = empty_list()
    status: str = None
    subject: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(RequestGroup, self).elementProperties()
        js.extend([
            ("action", "action", RequestGroupAction, True, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class RequestGroupAction(backboneelement.BackboneElement):
    """ Proposed actions, if any.

    The actions, if any, produced by the evaluation of the artifact.
    """
    resource_type: ClassVar[str] = "RequestGroupAction"
    action: Optional[List[RequestGroupAction]] = empty_list()
    cardinalityBehavior: Optional[str] = None
    code: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    condition: Optional[List[RequestGroupActionCondition]] = empty_list()
    description: Optional[str] = None
    documentation: Optional[List[relatedartifact.RelatedArtifact]] = empty_list()
    groupingBehavior: Optional[str] = None
    participant: Optional[List[fhirreference.FHIRReference]] = empty_list()
    precheckBehavior: Optional[str] = None
    prefix: Optional[str] = None
    priority: Optional[str] = None
    relatedAction: Optional[List[RequestGroupActionRelatedAction]] = empty_list()
    requiredBehavior: Optional[str] = None
    resource: Optional[fhirreference.FHIRReference] = None
    selectionBehavior: Optional[str] = None
    textEquivalent: Optional[str] = None
    timingAge: Optional[age.Age] = None
    timingDateTime: Optional[fhirdate.FHIRDate] = None
    timingDuration: Optional[duration.Duration] = None
    timingPeriod: Optional[period.Period] = None
    timingRange: Optional[range.Range] = None
    timingTiming: Optional[timing.Timing] = None
    title: Optional[str] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(RequestGroupAction, self).elementProperties()
        js.extend([
            ("action", "action", RequestGroupAction, True, None, False),
            ("cardinalityBehavior", "cardinalityBehavior", str, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("condition", "condition", RequestGroupActionCondition, True, None, False),
            ("description", "description", str, False, None, False),
            ("documentation", "documentation", relatedartifact.RelatedArtifact, True, None, False),
            ("groupingBehavior", "groupingBehavior", str, False, None, False),
            ("participant", "participant", fhirreference.FHIRReference, True, None, False),
            ("precheckBehavior", "precheckBehavior", str, False, None, False),
            ("prefix", "prefix", str, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("relatedAction", "relatedAction", RequestGroupActionRelatedAction, True, None, False),
            ("requiredBehavior", "requiredBehavior", str, False, None, False),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
            ("selectionBehavior", "selectionBehavior", str, False, None, False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("timingAge", "timingAge", age.Age, False, "timing", False),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("timingDuration", "timingDuration", duration.Duration, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingRange", "timingRange", range.Range, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("title", "title", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class RequestGroupActionCondition(backboneelement.BackboneElement):
    """ Whether or not the action is applicable.

    An expression that describes applicability criteria, or start/stop
    conditions for the action.
    """
    resource_type: ClassVar[str] = "RequestGroupActionCondition"
    expression: Optional[expression.Expression] = None
    kind: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(RequestGroupActionCondition, self).elementProperties()
        js.extend([
            ("expression", "expression", expression.Expression, False, None, False),
            ("kind", "kind", str, False, None, True),
        ])
        return js

@dataclass
class RequestGroupActionRelatedAction(backboneelement.BackboneElement):
    """ Relationship to another action.

    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """
    resource_type: ClassVar[str] = "RequestGroupActionRelatedAction"
    actionId: str = None
    offsetDuration: Optional[duration.Duration] = None
    offsetRange: Optional[range.Range] = None
    relationship: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(RequestGroupActionRelatedAction, self).elementProperties()
        js.extend([
            ("actionId", "actionId", str, False, None, True),
            ("offsetDuration", "offsetDuration", duration.Duration, False, "offset", False),
            ("offsetRange", "offsetRange", range.Range, False, "offset", False),
            ("relationship", "relationship", str, False, None, True),
        ])
        return js


import sys
try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + '.age']
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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