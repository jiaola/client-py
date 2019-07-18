#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Goal) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import duration
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import ratio

from . import backboneelement

@dataclass
class GoalTarget(backboneelement.BackboneElement):
    """ Target outcome for the goal.

    Indicates what should be done by when.
    """
    resource_type: ClassVar[str] = "GoalTarget"
    detailBoolean: Optional[bool] = None
    detailCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    detailInteger: Optional[int] = None
    detailQuantity: Optional[quantity.Quantity] = None
    detailRange: Optional[range.Range] = None
    detailRatio: Optional[ratio.Ratio] = None
    detailString: Optional[str] = None
    dueDate: Optional[fhirdate.FHIRDate] = None
    dueDuration: Optional[duration.Duration] = None
    measure: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(GoalTarget, self).elementProperties()
        js.extend([
            ("detailBoolean", "detailBoolean", bool, False, "detail", False),
            ("detailCodeableConcept", "detailCodeableConcept", codeableconcept.CodeableConcept, False, "detail", False),
            ("detailInteger", "detailInteger", int, False, "detail", False),
            ("detailQuantity", "detailQuantity", quantity.Quantity, False, "detail", False),
            ("detailRange", "detailRange", range.Range, False, "detail", False),
            ("detailRatio", "detailRatio", ratio.Ratio, False, "detail", False),
            ("detailString", "detailString", str, False, "detail", False),
            ("dueDate", "dueDate", fhirdate.FHIRDate, False, "due", False),
            ("dueDuration", "dueDuration", duration.Duration, False, "due", False),
            ("measure", "measure", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

from . import domainresource

@dataclass
class Goal(domainresource.DomainResource):
    """ Describes the intended objective(s) for a patient, group or organization.

    Describes the intended objective(s) for a patient, group or organization
    care, for example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """
    resource_type: ClassVar[str] = "Goal"
    achievementStatus: Optional[codeableconcept.CodeableConcept] = None
    addresses: Optional[List[fhirreference.FHIRReference]] = empty_list()
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    description:codeableconcept.CodeableConcept = None
    expressedBy: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    lifecycleStatus: str = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    outcomeCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    outcomeReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    priority: Optional[codeableconcept.CodeableConcept] = None
    startCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    startDate: Optional[fhirdate.FHIRDate] = None
    statusDate: Optional[fhirdate.FHIRDate] = None
    statusReason: Optional[str] = None
    subject:fhirreference.FHIRReference = None
    target: Optional[List[GoalTarget]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Goal, self).elementProperties()
        js.extend([
            ("achievementStatus", "achievementStatus", codeableconcept.CodeableConcept, False, None, False),
            ("addresses", "addresses", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("description", "description", codeableconcept.CodeableConcept, False, None, True),
            ("expressedBy", "expressedBy", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("lifecycleStatus", "lifecycleStatus", str, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("outcomeCode", "outcomeCode", codeableconcept.CodeableConcept, True, None, False),
            ("outcomeReference", "outcomeReference", fhirreference.FHIRReference, True, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("startCodeableConcept", "startCodeableConcept", codeableconcept.CodeableConcept, False, "start", False),
            ("startDate", "startDate", fhirdate.FHIRDate, False, "start", False),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, False),
            ("statusReason", "statusReason", str, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("target", "target", GoalTarget, True, None, False),
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
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
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