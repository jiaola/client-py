#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/RelatedPerson) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .address import Address
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .humanname import HumanName
from .identifier import Identifier
from .period import Period


@dataclass
class RelatedPersonCommunication(BackboneElement):
    """ A language which may be used to communicate with about the patient's health.
    """
    resource_type: ClassVar[str] = "RelatedPersonCommunication"
    language: CodeableConcept = None
    preferred: Optional[bool] = None

    def elementProperties(self):
        js = super(RelatedPersonCommunication, self).elementProperties()
        js.extend([
            ("language", "language", CodeableConcept, False, None, True),
            ("preferred", "preferred", bool, False, None, False),
        ])
        return js


@dataclass
class RelatedPerson(DomainResource):
    """ A person that is related to a patient, but who is not a direct target of
    care.

    Information about a person that is involved in the care for a patient, but
    who is not the target of healthcare, nor has a formal responsibility in the
    care process.
    """
    resource_type: ClassVar[str] = "RelatedPerson"
    active: Optional[bool] = None
    address: Optional[List[Address]] = empty_list()
    birthDate: Optional[FHIRDate] = None
    communication: Optional[List[RelatedPersonCommunication]] = empty_list()
    gender: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    name: Optional[List[HumanName]] = empty_list()
    patient: FHIRReference = None
    period: Optional[Period] = None
    photo: Optional[List[Attachment]] = empty_list()
    relationship: Optional[List[CodeableConcept]] = empty_list()
    telecom: Optional[List[ContactPoint]] = empty_list()

    def elementProperties(self):
        js = super(RelatedPerson, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("address", "address", Address, True, None, False),
            ("birthDate", "birthDate", FHIRDate, False, None, False),
            ("communication", "communication", RelatedPersonCommunication, True, None, False),
            ("gender", "gender", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("name", "name", HumanName, True, None, False),
            ("patient", "patient", FHIRReference, False, None, True),
            ("period", "period", Period, False, None, False),
            ("photo", "photo", Attachment, True, None, False),
            ("relationship", "relationship", CodeableConcept, True, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
        ])
        return js