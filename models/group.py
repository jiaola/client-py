#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Group) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range

from . import domainresource

@dataclass
class Group(domainresource.DomainResource):
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
    code: Optional[codeableconcept.CodeableConcept] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    managingEntity: Optional[fhirreference.FHIRReference] = None
    member: Optional[List[GroupMember]] = empty_list()
    name: Optional[str] = None
    quantity: Optional[int] = None
    type: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Group, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("actual", "actual", bool, False, None, True),
            ("characteristic", "characteristic", GroupCharacteristic, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("managingEntity", "managingEntity", fhirreference.FHIRReference, False, None, False),
            ("member", "member", GroupMember, True, None, False),
            ("name", "name", str, False, None, False),
            ("quantity", "quantity", int, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js

from . import backboneelement

@dataclass
class GroupCharacteristic(backboneelement.BackboneElement):
    """ Include / Exclude group members by Trait.

    Identifies traits whose presence r absence is shared by members of the
    group.
    """
    resource_type: ClassVar[str] = "GroupCharacteristic"
    code:codeableconcept.CodeableConcept = None
    exclude: bool = None
    period: Optional[period.Period] = None
    valueBoolean: bool = None
    valueCodeableConcept:codeableconcept.CodeableConcept = None
    valueQuantity:quantity.Quantity = None
    valueRange:range.Range = None
    valueReference:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(GroupCharacteristic, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("exclude", "exclude", bool, False, None, True),
            ("period", "period", period.Period, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
        ])
        return js

@dataclass
class GroupMember(backboneelement.BackboneElement):
    """ Who or what is in group.

    Identifies the resource instances that are members of the group.
    """
    resource_type: ClassVar[str] = "GroupMember"
    entity:fhirreference.FHIRReference = None
    inactive: Optional[bool] = None
    period: Optional[period.Period] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(GroupMember, self).elementProperties()
        js.extend([
            ("entity", "entity", fhirreference.FHIRReference, False, None, True),
            ("inactive", "inactive", bool, False, None, False),
            ("period", "period", period.Period, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']