#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Person) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import backboneelement
from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier

from . import backboneelement

@dataclass
class PersonLink(backboneelement.BackboneElement):
    """ Link to a resource that concerns the same actual person.
    """
    resource_type: ClassVar[str] = "PersonLink"
    assurance: Optional[str] = None
    target:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(PersonLink, self).elementProperties()
        js.extend([
            ("assurance", "assurance", str, False, None, False),
            ("target", "target", fhirreference.FHIRReference, False, None, True),
        ])
        return js

from . import domainresource

@dataclass
class Person(domainresource.DomainResource):
    """ A generic person record.

    Demographics and administrative information about a person independent of a
    specific health-related context.
    """
    resource_type: ClassVar[str] = "Person"
    active: Optional[bool] = None
    address: Optional[List[address.Address]] = empty_list()
    birthDate: Optional[fhirdate.FHIRDate] = None
    gender: Optional[str] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    link: Optional[List[PersonLink]] = empty_list()
    managingOrganization: Optional[fhirreference.FHIRReference] = None
    name: Optional[List[humanname.HumanName]] = empty_list()
    photo: Optional[attachment.Attachment] = None
    telecom: Optional[List[contactpoint.ContactPoint]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Person, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("address", "address", address.Address, True, None, False),
            ("birthDate", "birthDate", fhirdate.FHIRDate, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("link", "link", PersonLink, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("name", "name", humanname.HumanName, True, None, False),
            ("photo", "photo", attachment.Attachment, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


import sys
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import humanname
except ImportError:
    humanname = sys.modules[__package__ + '.humanname']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']