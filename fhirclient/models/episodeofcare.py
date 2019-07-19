#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/EpisodeOfCare) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class EpisodeOfCareStatusHistory(BackboneElement):
    """ Past list of status codes (the current status may be included to cover the
    start date of the status).

    The history of statuses that the EpisodeOfCare has been through (without
    requiring processing the history of the resource).
    """
    resource_type: ClassVar[str] = "EpisodeOfCareStatusHistory"
    period: Period = None
    status: str = None

    def elementProperties(self):
        js = super(EpisodeOfCareStatusHistory, self).elementProperties()
        js.extend([
            ("period", "period", Period, False, None, True),
            ("status", "status", str, False, None, True),
        ])
        return js


@dataclass
class EpisodeOfCareDiagnosis(BackboneElement):
    """ The list of diagnosis relevant to this episode of care.
    """
    resource_type: ClassVar[str] = "EpisodeOfCareDiagnosis"
    condition: FHIRReference = None
    rank: Optional[int] = None
    role: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(EpisodeOfCareDiagnosis, self).elementProperties()
        js.extend([
            ("condition", "condition", FHIRReference, False, None, True),
            ("rank", "rank", int, False, None, False),
            ("role", "role", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class EpisodeOfCare(DomainResource):
    """ An association of a Patient with an Organization and  Healthcare
    Provider(s) for a period of time that the Organization assumes some level
    of responsibility.

    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during this
    time.
    """
    resource_type: ClassVar[str] = "EpisodeOfCare"
    account: Optional[List[FHIRReference]] = empty_list()
    careManager: Optional[FHIRReference] = None
    diagnosis: Optional[List[EpisodeOfCareDiagnosis]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    managingOrganization: Optional[FHIRReference] = None
    patient: FHIRReference = None
    period: Optional[Period] = None
    referralRequest: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    statusHistory: Optional[List[EpisodeOfCareStatusHistory]] = empty_list()
    team: Optional[List[FHIRReference]] = empty_list()
    type: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(EpisodeOfCare, self).elementProperties()
        js.extend([
            ("account", "account", FHIRReference, True, None, False),
            ("careManager", "careManager", FHIRReference, False, None, False),
            ("diagnosis", "diagnosis", EpisodeOfCareDiagnosis, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("managingOrganization", "managingOrganization", FHIRReference, False, None, False),
            ("patient", "patient", FHIRReference, False, None, True),
            ("period", "period", Period, False, None, False),
            ("referralRequest", "referralRequest", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusHistory", "statusHistory", EpisodeOfCareStatusHistory, True, None, False),
            ("team", "team", FHIRReference, True, None, False),
            ("type", "type", CodeableConcept, True, None, False),
        ])
        return js