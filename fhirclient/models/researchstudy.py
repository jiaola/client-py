#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ResearchStudy) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .relatedartifact import RelatedArtifact


@dataclass
class ResearchStudyObjective(BackboneElement):
    """ A goal for the study.

    A goal that the study is aiming to achieve in terms of a scientific
    question to be answered by the analysis of data collected during the study.
    """
    resource_type: ClassVar[str] = "ResearchStudyObjective"
    name: Optional[str] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ResearchStudyObjective, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ResearchStudyArm(BackboneElement):
    """ Defined path through the study for a subject.

    Describes an expected sequence of events for one of the participants of a
    study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out,
    follow-up.
    """
    resource_type: ClassVar[str] = "ResearchStudyArm"
    description: Optional[str] = None
    name: str = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ResearchStudyArm, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ResearchStudy(DomainResource):
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
    category: Optional[List[CodeableConcept]] = empty_list()
    condition: Optional[List[CodeableConcept]] = empty_list()
    contact: Optional[List[ContactDetail]] = empty_list()
    description: Optional[str] = None
    enrollment: Optional[List[FHIRReference]] = empty_list()
    focus: Optional[List[CodeableConcept]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    keyword: Optional[List[CodeableConcept]] = empty_list()
    location: Optional[List[CodeableConcept]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    objective: Optional[List[ResearchStudyObjective]] = empty_list()
    partOf: Optional[List[FHIRReference]] = empty_list()
    period: Optional[Period] = None
    phase: Optional[CodeableConcept] = None
    primaryPurposeType: Optional[CodeableConcept] = None
    principalInvestigator: Optional[FHIRReference] = None
    protocol: Optional[List[FHIRReference]] = empty_list()
    reasonStopped: Optional[CodeableConcept] = None
    relatedArtifact: Optional[List[RelatedArtifact]] = empty_list()
    site: Optional[List[FHIRReference]] = empty_list()
    sponsor: Optional[FHIRReference] = None
    status: str = None
    title: Optional[str] = None

    def elementProperties(self):
        js = super(ResearchStudy, self).elementProperties()
        js.extend([
            ("arm", "arm", ResearchStudyArm, True, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("condition", "condition", CodeableConcept, True, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("enrollment", "enrollment", FHIRReference, True, None, False),
            ("focus", "focus", CodeableConcept, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("keyword", "keyword", CodeableConcept, True, None, False),
            ("location", "location", CodeableConcept, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("objective", "objective", ResearchStudyObjective, True, None, False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("period", "period", Period, False, None, False),
            ("phase", "phase", CodeableConcept, False, None, False),
            ("primaryPurposeType", "primaryPurposeType", CodeableConcept, False, None, False),
            ("principalInvestigator", "principalInvestigator", FHIRReference, False, None, False),
            ("protocol", "protocol", FHIRReference, True, None, False),
            ("reasonStopped", "reasonStopped", CodeableConcept, False, None, False),
            ("relatedArtifact", "relatedArtifact", RelatedArtifact, True, None, False),
            ("site", "site", FHIRReference, True, None, False),
            ("sponsor", "sponsor", FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
        ])
        return js