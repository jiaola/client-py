#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Group) on 2019-07-18.
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
from .quantity import Quantity
from .range import Range


@dataclass
class GroupMember(BackboneElement):
    """ Who or what is in group.

    Identifies the resource instances that are members of the group.
    """
    resource_type: ClassVar[str] = "GroupMember"
    entity: FHIRReference = None
    inactive: Optional[bool] = None
    period: Optional[Period] = None

    def elementProperties(self):
        js = super(GroupMember, self).elementProperties()
        js.extend([
            ("entity", "entity", FHIRReference, False, None, True),
            ("inactive", "inactive", bool, False, None, False),
            ("period", "period", Period, False, None, False),
        ])
        return js


@dataclass
class GroupCharacteristic(BackboneElement):
    """ Include / Exclude group members by Trait.

    Identifies traits whose presence r absence is shared by members of the
    group.
    """
    resource_type: ClassVar[str] = "GroupCharacteristic"
    code: CodeableConcept = None
    exclude: bool = None
    period: Optional[Period] = None
    valueBoolean: bool = None
    valueCodeableConcept: CodeableConcept = None
    valueQuantity: Quantity = None
    valueRange: Range = None
    valueReference: FHIRReference = None

    def elementProperties(self):
        js = super(GroupCharacteristic, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("exclude", "exclude", bool, False, None, True),
            ("period", "period", Period, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", CodeableConcept, False, "value", True),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", True),
            ("valueRange", "valueRange", Range, False, "value", True),
            ("valueReference", "valueReference", FHIRReference, False, "value", True),
        ])
        return js


@dataclass
class Group(DomainResource):
    """ Group of multiple entities.

    Represents a defined collection of entities that may be discussed or acted
    upon collectively but which are not expected to act collectively, and are
    not formally or legally recognized; i.e. a collection of entities that
    isn't an Organization.
    """
    resource_type: ClassVar[str] = "Group"
    active: Optional[bool] = None
    actual: bool = None
    characteristic: Optional[List[GroupCharacteristic]] = empty_list()
    code: Optional[CodeableConcept] = None
    identifier: Optional[List[Identifier]] = empty_list()
    managingEntity: Optional[FHIRReference] = None
    member: Optional[List[GroupMember]] = empty_list()
    name: Optional[str] = None
    quantity: Optional[int] = None
    type: str = None

    def elementProperties(self):
        js = super(Group, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("actual", "actual", bool, False, None, True),
            ("characteristic", "characteristic", GroupCharacteristic, True, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("managingEntity", "managingEntity", FHIRReference, False, None, False),
            ("member", "member", GroupMember, True, None, False),
            ("name", "name", str, False, None, False),
            ("quantity", "quantity", int, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js