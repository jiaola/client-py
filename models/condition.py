#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Condition) on 2019-07-18.
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
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import range

from . import backboneelement

@dataclass
class ConditionStage(backboneelement.BackboneElement):
    """ Stage/grade, usually assessed formally.

    Clinical stage or grade of a condition. May include formal severity
    assessments.
    """
    resource_type: ClassVar[str] = "ConditionStage"
    assessment: Optional[List[fhirreference.FHIRReference]] = empty_list()
    summary: Optional[codeableconcept.CodeableConcept] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ConditionStage, self).elementProperties()
        js.extend([
            ("assessment", "assessment", fhirreference.FHIRReference, True, None, False),
            ("summary", "summary", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class ConditionEvidence(backboneelement.BackboneElement):
    """ Supporting evidence.

    Supporting evidence / manifestations that are the basis of the Condition's
    verification status, such as evidence that confirmed or refuted the
    condition.
    """
    resource_type: ClassVar[str] = "ConditionEvidence"
    code: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    detail: Optional[List[fhirreference.FHIRReference]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ConditionEvidence, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("detail", "detail", fhirreference.FHIRReference, True, None, False),
        ])
        return js

from . import domainresource

@dataclass
class Condition(domainresource.DomainResource):
    """ Detailed information about conditions, problems or diagnoses.

    A clinical condition, problem, diagnosis, or other event, situation, issue,
    or clinical concept that has risen to a level of concern.
    """
    resource_type: ClassVar[str] = "Condition"
    abatementAge: Optional[age.Age] = None
    abatementDateTime: Optional[fhirdate.FHIRDate] = None
    abatementPeriod: Optional[period.Period] = None
    abatementRange: Optional[range.Range] = None
    abatementString: Optional[str] = None
    asserter: Optional[fhirreference.FHIRReference] = None
    bodySite: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    clinicalStatus: Optional[codeableconcept.CodeableConcept] = None
    code: Optional[codeableconcept.CodeableConcept] = None
    encounter: Optional[fhirreference.FHIRReference] = None
    evidence: Optional[List[ConditionEvidence]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    note: Optional[List[annotation.Annotation]] = empty_list()
    onsetAge: Optional[age.Age] = None
    onsetDateTime: Optional[fhirdate.FHIRDate] = None
    onsetPeriod: Optional[period.Period] = None
    onsetRange: Optional[range.Range] = None
    onsetString: Optional[str] = None
    recordedDate: Optional[fhirdate.FHIRDate] = None
    recorder: Optional[fhirreference.FHIRReference] = None
    severity: Optional[codeableconcept.CodeableConcept] = None
    stage: Optional[List[ConditionStage]] = empty_list()
    subject:fhirreference.FHIRReference = None
    verificationStatus: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Condition, self).elementProperties()
        js.extend([
            ("abatementAge", "abatementAge", age.Age, False, "abatement", False),
            ("abatementDateTime", "abatementDateTime", fhirdate.FHIRDate, False, "abatement", False),
            ("abatementPeriod", "abatementPeriod", period.Period, False, "abatement", False),
            ("abatementRange", "abatementRange", range.Range, False, "abatement", False),
            ("abatementString", "abatementString", str, False, "abatement", False),
            ("asserter", "asserter", fhirreference.FHIRReference, False, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("clinicalStatus", "clinicalStatus", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("evidence", "evidence", ConditionEvidence, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("onsetAge", "onsetAge", age.Age, False, "onset", False),
            ("onsetDateTime", "onsetDateTime", fhirdate.FHIRDate, False, "onset", False),
            ("onsetPeriod", "onsetPeriod", period.Period, False, "onset", False),
            ("onsetRange", "onsetRange", range.Range, False, "onset", False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("recordedDate", "recordedDate", fhirdate.FHIRDate, False, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("severity", "severity", codeableconcept.CodeableConcept, False, None, False),
            ("stage", "stage", ConditionStage, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("verificationStatus", "verificationStatus", codeableconcept.CodeableConcept, False, None, False),
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