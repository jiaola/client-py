#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Practitioner) on 2019-07-18.
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
class PractitionerQualification(BackboneElement):
    """ Certification, licenses, or training pertaining to the provision of care.

    The official certifications, training, and licenses that authorize or
    otherwise pertain to the provision of care by the practitioner.  For
    example, a medical license issued by a medical board authorizing the
    practitioner to practice medicine within a certian locality.
    """
    resource_type: ClassVar[str] = "PractitionerQualification"
    code: CodeableConcept = None
    identifier: Optional[List[Identifier]] = empty_list()
    issuer: Optional[FHIRReference] = None
    period: Optional[Period] = None

    def elementProperties(self):
        js = super(PractitionerQualification, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("identifier", "identifier", Identifier, True, None, False),
            ("issuer", "issuer", FHIRReference, False, None, False),
            ("period", "period", Period, False, None, False),
        ])
        return js


@dataclass
class Practitioner(DomainResource):
    """ A person with a  formal responsibility in the provisioning of healthcare or
    related services.

    A person who is directly or indirectly involved in the provisioning of
    healthcare.
    """
    resource_type: ClassVar[str] = "Practitioner"
    active: Optional[bool] = None
    address: Optional[List[Address]] = empty_list()
    birthDate: Optional[FHIRDate] = None
    communication: Optional[List[CodeableConcept]] = empty_list()
    gender: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    name: Optional[List[HumanName]] = empty_list()
    photo: Optional[List[Attachment]] = empty_list()
    qualification: Optional[List[PractitionerQualification]] = empty_list()
    telecom: Optional[List[ContactPoint]] = empty_list()

    def elementProperties(self):
        js = super(Practitioner, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("address", "address", Address, True, None, False),
            ("birthDate", "birthDate", FHIRDate, False, None, False),
            ("communication", "communication", CodeableConcept, True, None, False),
            ("gender", "gender", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("name", "name", HumanName, True, None, False),
            ("photo", "photo", Attachment, True, None, False),
            ("qualification", "qualification", PractitionerQualification, True, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
        ])
        return js