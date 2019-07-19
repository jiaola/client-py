#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Person) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .address import Address
from .attachment import Attachment
from .backboneelement import BackboneElement
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .humanname import HumanName
from .identifier import Identifier


@dataclass
class PersonLink(BackboneElement):
    """ Link to a resource that concerns the same actual person.
    """
    resource_type: ClassVar[str] = "PersonLink"
    assurance: Optional[str] = None
    target: FHIRReference = None

    def elementProperties(self):
        js = super(PersonLink, self).elementProperties()
        js.extend([
            ("assurance", "assurance", str, False, None, False),
            ("target", "target", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class Person(DomainResource):
    """ A generic person record.

    Demographics and administrative information about a person independent of a
    specific health-related context.
    """
    resource_type: ClassVar[str] = "Person"
    active: Optional[bool] = None
    address: Optional[List[Address]] = empty_list()
    birthDate: Optional[FHIRDate] = None
    gender: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    link: Optional[List[PersonLink]] = empty_list()
    managingOrganization: Optional[FHIRReference] = None
    name: Optional[List[HumanName]] = empty_list()
    photo: Optional[Attachment] = None
    telecom: Optional[List[ContactPoint]] = empty_list()

    def elementProperties(self):
        js = super(Person, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("address", "address", Address, True, None, False),
            ("birthDate", "birthDate", FHIRDate, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("link", "link", PersonLink, True, None, False),
            ("managingOrganization", "managingOrganization", FHIRReference, False, None, False),
            ("name", "name", HumanName, True, None, False),
            ("photo", "photo", Attachment, False, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
        ])
        return js