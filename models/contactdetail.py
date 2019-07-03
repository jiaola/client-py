#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ContactDetail) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import contactpoint
from . import element


from . import element

@dataclass
class ContactDetail(element.Element):
    """ Contact information.

    Specifies contact information for a person or organization.
    """
    resource_type: ClassVar[str] = "ContactDetail"
    name: Optional[str] = None
    telecom: Optional[List[contactpoint.ContactPoint]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.name = None
#        """ Name of an individual to contact.
#        Type `str`
#
#. """
#
#
#        self.telecom = None
#        """ Contact details for individual or organization.
#        List of `ContactPoint` items
#
# (represented as `dict` in JSON). """
#

#        super(ContactDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ContactDetail, self).elementProperties()
        js.extend([
            ("name", "name", str, {  # #}False, None, {  # #}False),
            ("telecom", "telecom", contactpoint.ContactPoint, {  # #}True, None, {  # #}False),
        ])
        return js