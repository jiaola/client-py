#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ResearchStudy) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import contactdetail
from . import domainresource
from . import fhirreference
from . import identifier
from . import period
from . import relatedartifact

from . import backboneelement

@dataclass
class ResearchStudyObjective(backboneelement.BackboneElement):
    """ A goal for the study.

    A goal that the study is aiming to achieve in terms of a scientific
    question to be answered by the analysis of data collected during the study.
    """
    resource_type: ClassVar[str] = "ResearchStudyObjective"
    name: Optional[str] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ResearchStudyObjective, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class ResearchStudyArm(backboneelement.BackboneElement):
    """ Defined path through the study for a subject.

    Describes an expected sequence of events for one of the participants of a
    study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out,
    follow-up.
    """
    resource_type: ClassVar[str] = "ResearchStudyArm"
    description: Optional[str] = None
    name: str = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ResearchStudyArm, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

from . import domainresource

@dataclass
class ResearchStudy(domainresource.DomainResource):
    """ Investigation to increase healthcare-related patient-independent knowledge.

    A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices, therapies
    and other interventional and investigative techniques.  A ResearchStudy
    involves the gathering of information about human or animal subjects.
    """
    resource_type: ClassVar[str] = "ResearchStudy"
    arm: Optional[List[ResearchStudyArm]] = empty_list()
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    condition: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    description: Optional[str] = None
    enrollment: Optional[List[fhirreference.FHIRReference]] = empty_list()
    focus: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    keyword: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    location: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    note: Optional[List[annotation.Annotation]] = empty_list()
    objective: Optional[List[ResearchStudyObjective]] = empty_list()
    partOf: Optional[List[fhirreference.FHIRReference]] = empty_list()
    period: Optional[period.Period] = None
    phase: Optional[codeableconcept.CodeableConcept] = None
    primaryPurposeType: Optional[codeableconcept.CodeableConcept] = None
    principalInvestigator: Optional[fhirreference.FHIRReference] = None
    protocol: Optional[List[fhirreference.FHIRReference]] = empty_list()
    reasonStopped: Optional[codeableconcept.CodeableConcept] = None
    relatedArtifact: Optional[List[relatedartifact.RelatedArtifact]] = empty_list()
    site: Optional[List[fhirreference.FHIRReference]] = empty_list()
    sponsor: Optional[fhirreference.FHIRReference] = None
    status: str = None
    title: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ResearchStudy, self).elementProperties()
        js.extend([
            ("arm", "arm", ResearchStudyArm, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("condition", "condition", codeableconcept.CodeableConcept, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("enrollment", "enrollment", fhirreference.FHIRReference, True, None, False),
            ("focus", "focus", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("keyword", "keyword", codeableconcept.CodeableConcept, True, None, False),
            ("location", "location", codeableconcept.CodeableConcept, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("objective", "objective", ResearchStudyObjective, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("phase", "phase", codeableconcept.CodeableConcept, False, None, False),
            ("primaryPurposeType", "primaryPurposeType", codeableconcept.CodeableConcept, False, None, False),
            ("principalInvestigator", "principalInvestigator", fhirreference.FHIRReference, False, None, False),
            ("protocol", "protocol", fhirreference.FHIRReference, True, None, False),
            ("reasonStopped", "reasonStopped", codeableconcept.CodeableConcept, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("site", "site", fhirreference.FHIRReference, True, None, False),
            ("sponsor", "sponsor", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
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
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
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
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']