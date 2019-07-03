#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Address) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import element
from . import period


from . import element

@dataclass
class Address(element.Element):
    """ An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).

    An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).  This data type may be used to convey
    addresses for use in delivering mail as well as for visiting locations
    which might not be valid for mail delivery.  There are a variety of postal
    address formats defined around the world.
    """
    resource_type: ClassVar[str] = "Address"
    city: Optional[str] = None
    country: Optional[str] = None
    district: Optional[str] = None
    line: Optional[List[str]] = empty_list()
    period: Optional[period.Period] = None
    postalCode: Optional[str] = None
    state: Optional[str] = None
    text: Optional[str] = None
    type: Optional[str] = None
    use: Optional[str] = None

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
#        self.city = None
#        """ Name of city, town etc..
#        Type `str`
#
#. """
#
#
#        self.country = None
#        """ Country (e.g. can be ISO 3166 2 or 3 letter code).
#        Type `str`
#
#. """
#
#
#        self.district = None
#        """ District name (aka county).
#        Type `str`
#
#. """
#
#
#        self.line = None
#        """ Street name, number, direction & P.O. Box etc..
#        List of `str` items
#
#. """
#
#
#        self.period = None
#        """ Time period when address was/is in use.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.postalCode = None
#        """ Postal code for area.
#        Type `str`
#
#. """
#
#
#        self.state = None
#        """ Sub-unit of country (abbreviations ok).
#        Type `str`
#
#. """
#
#
#        self.text = None
#        """ Text representation of the address.
#        Type `str`
#
#. """
#
#
#        self.type = None
#        """ postal | physical | both.
#        Type `str`
#
#. """
#
#
#        self.use = None
#        """ home | work | temp | old | billing - purpose of this address.
#        Type `str`
#
#. """
#

#        super(Address, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Address, self).elementProperties()
        js.extend([
            ("city", "city", str, {  # #}False, None, {  # #}False),
            ("country", "country", str, {  # #}False, None, {  # #}False),
            ("district", "district", str, {  # #}False, None, {  # #}False),
            ("line", "line", str, {  # #}True, None, {  # #}False),
            ("period", "period", period.Period, {  # #}False, None, {  # #}False),
            ("postalCode", "postalCode", str, {  # #}False, None, {  # #}False),
            ("state", "state", str, {  # #}False, None, {  # #}False),
            ("text", "text", str, {  # #}False, None, {  # #}False),
            ("type", "type", str, {  # #}False, None, {  # #}False),
            ("use", "use", str, {  # #}False, None, {  # #}False),
        ])
        return js