#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DetectedIssue) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period

from . import backboneelement

@dataclass
class DetectedIssueMitigation(backboneelement.BackboneElement):
    """ Step taken to address.

    Indicates an action that has been taken or is committed to reduce or
    eliminate the likelihood of the risk identified by the detected issue from
    manifesting.  Can also reflect an observation of known mitigating factors
    that may reduce/eliminate the need for any action.
    """
    resource_type: ClassVar[str] = "DetectedIssueMitigation"
    action:codeableconcept.CodeableConcept = None
    author: Optional[fhirreference.FHIRReference] = None
    date: Optional[fhirdate.FHIRDate] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DetectedIssueMitigation, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, False, None, True),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
        ])
        return js

@dataclass
class DetectedIssueEvidence(backboneelement.BackboneElement):
    """ Supporting evidence.

    Supporting evidence or manifestations that provide the basis for
    identifying the detected issue such as a GuidanceResponse or MeasureReport.
    """
    resource_type: ClassVar[str] = "DetectedIssueEvidence"
    code: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    detail: Optional[List[fhirreference.FHIRReference]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DetectedIssueEvidence, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("detail", "detail", fhirreference.FHIRReference, True, None, False),
        ])
        return js

from . import domainresource

@dataclass
class DetectedIssue(domainresource.DomainResource):
    """ Clinical issue with action.

    Indicates an actual or potential clinical issue with or between one or more
    active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition conflict,
    etc.
    """
    resource_type: ClassVar[str] = "DetectedIssue"
    author: Optional[fhirreference.FHIRReference] = None
    code: Optional[codeableconcept.CodeableConcept] = None
    detail: Optional[str] = None
    evidence: Optional[List[DetectedIssueEvidence]] = empty_list()
    identifiedDateTime: Optional[fhirdate.FHIRDate] = None
    identifiedPeriod: Optional[period.Period] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    implicated: Optional[List[fhirreference.FHIRReference]] = empty_list()
    mitigation: Optional[List[DetectedIssueMitigation]] = empty_list()
    patient: Optional[fhirreference.FHIRReference] = None
    reference: Optional[str] = None
    severity: Optional[str] = None
    status: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DetectedIssue, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", str, False, None, False),
            ("evidence", "evidence", DetectedIssueEvidence, True, None, False),
            ("identifiedDateTime", "identifiedDateTime", fhirdate.FHIRDate, False, "identified", False),
            ("identifiedPeriod", "identifiedPeriod", period.Period, False, "identified", False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("implicated", "implicated", fhirreference.FHIRReference, True, None, False),
            ("mitigation", "mitigation", DetectedIssueMitigation, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("reference", "reference", str, False, None, False),
            ("severity", "severity", str, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js


import sys
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