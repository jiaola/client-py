#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CareTeam) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class CareTeamParticipant(BackboneElement):
    """ Members of the team.

    Identifies all people and organizations who are expected to be involved in
    the care team.
    """
    resource_type: ClassVar[str] = "CareTeamParticipant"
    member: Optional[FHIRReference] = None
    onBehalfOf: Optional[FHIRReference] = None
    period: Optional[Period] = None
    role: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(CareTeamParticipant, self).elementProperties()
        js.extend([
            ("member", "member", FHIRReference, False, None, False),
            ("onBehalfOf", "onBehalfOf", FHIRReference, False, None, False),
            ("period", "period", Period, False, None, False),
            ("role", "role", CodeableConcept, True, None, False),
        ])
        return js


@dataclass
class CareTeam(DomainResource):
    """ Planned participants in the coordination and delivery of care for a patient
    or group.

    The Care Team includes all the people and organizations who plan to
    participate in the coordination and delivery of care for a patient.
    """
    resource_type: ClassVar[str] = "CareTeam"
    category: Optional[List[CodeableConcept]] = empty_list()
    encounter: Optional[FHIRReference] = None
    identifier: Optional[List[Identifier]] = empty_list()
    managingOrganization: Optional[List[FHIRReference]] = empty_list()
    name: Optional[str] = None
    note: Optional[List[Annotation]] = empty_list()
    participant: Optional[List[CareTeamParticipant]] = empty_list()
    period: Optional[Period] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    status: Optional[str] = None
    subject: Optional[FHIRReference] = None
    telecom: Optional[List[ContactPoint]] = empty_list()

    def elementProperties(self):
        js = super(CareTeam, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, True, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("managingOrganization", "managingOrganization", FHIRReference, True, None, False),
            ("name", "name", str, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("participant", "participant", CareTeamParticipant, True, None, False),
            ("period", "period", Period, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("subject", "subject", FHIRReference, False, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
        ])
        return js