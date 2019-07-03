#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Goal) on 2019-07-03.
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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.achievementStatus = None
#        """ in-progress | improving | worsening | no-change | achieved |
        sustaining | not-achieved | no-progress | not-attainable.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.addresses = None
#        """ Issues addressed by this goal.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.category = None
#        """ E.g. Treatment, dietary, behavioral, etc..
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.description = None
#        """ Code or text describing goal.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.expressedBy = None
#        """ Who's responsible for creating Goal?.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ External Ids for this goal.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.lifecycleStatus = None
#        """ proposed | planned | accepted | active | on-hold | completed |
        cancelled | entered-in-error | rejected.
#        Type `str`
#
#. """
#
#
#        self.note = None
#        """ Comments about the goal.
#        List of `Annotation` items
#
# (represented as `dict` in JSON). """
#
#
#        self.outcomeCode = None
#        """ What result was achieved regarding the goal?.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.outcomeReference = None
#        """ Observation that resulted from goal.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.priority = None
#        """ high-priority | medium-priority | low-priority.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.startCodeableConcept = None
#        """ When goal pursuit begins.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.startDate = None
#        """ When goal pursuit begins.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.statusDate = None
#        """ When goal status took effect.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.statusReason = None
#        """ Reason for current status.
#        Type `str`
#
#. """
#
#
#        self.subject = None
#        """ Who this goal is intended for.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.target = None
#        """ Target outcome for the goal.
#        List of `GoalTarget` items
#
# (represented as `dict` in JSON). """
#

#        super(Goal, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Goal, self).elementProperties()
        js.extend([
            ("achievementStatus", "achievementStatus", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("addresses", "addresses", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("category", "category", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("description", "description", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("expressedBy", "expressedBy", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("lifecycleStatus", "lifecycleStatus", str, {  # #}False, None, {  # #}True),
            ("note", "note", annotation.Annotation, {  # #}True, None, {  # #}False),
            ("outcomeCode", "outcomeCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("outcomeReference", "outcomeReference", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("priority", "priority", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("startCodeableConcept", "startCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "start", {  # #}False),
            ("startDate", "startDate", fhirdate.FHIRDate, {  # #}False, "start", {  # #}False),
            ("statusDate", "statusDate", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("statusReason", "statusReason", str, {  # #}False, None, {  # #}False),
            ("subject", "subject", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("target", "target", GoalTarget, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.detailBoolean = None
#        """ The target value to be achieved.
#        Type `bool`
#
#. """
#
#
#        self.detailCodeableConcept = None
#        """ The target value to be achieved.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.detailInteger = None
#        """ The target value to be achieved.
#        Type `int`
#
#. """
#
#
#        self.detailQuantity = None
#        """ The target value to be achieved.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.detailRange = None
#        """ The target value to be achieved.
#        Type `Range`
#
# (represented as `dict` in JSON). """
#
#
#        self.detailRatio = None
#        """ The target value to be achieved.
#        Type `Ratio`
#
# (represented as `dict` in JSON). """
#
#
#        self.detailString = None
#        """ The target value to be achieved.
#        Type `str`
#
#. """
#
#
#        self.dueDate = None
#        """ Reach goal on or before.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.dueDuration = None
#        """ Reach goal on or before.
#        Type `Duration`
#
# (represented as `dict` in JSON). """
#
#
#        self.measure = None
#        """ The parameter whose value is being tracked.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(GoalTarget, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(GoalTarget, self).elementProperties()
        js.extend([
            ("detailBoolean", "detailBoolean", bool, {  # #}False, "detail", {  # #}False),
            ("detailCodeableConcept", "detailCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "detail", {  # #}False),
            ("detailInteger", "detailInteger", int, {  # #}False, "detail", {  # #}False),
            ("detailQuantity", "detailQuantity", quantity.Quantity, {  # #}False, "detail", {  # #}False),
            ("detailRange", "detailRange", range.Range, {  # #}False, "detail", {  # #}False),
            ("detailRatio", "detailRatio", ratio.Ratio, {  # #}False, "detail", {  # #}False),
            ("detailString", "detailString", str, {  # #}False, "detail", {  # #}False),
            ("dueDate", "dueDate", fhirdate.FHIRDate, {  # #}False, "due", {  # #}False),
            ("dueDuration", "dueDuration", duration.Duration, {  # #}False, "due", {  # #}False),
            ("measure", "measure", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
        ])
        return js