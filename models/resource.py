#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Resource) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import fhirabstractresource
from . import meta


from . import fhirabstractresource

@dataclass
class Resource(fhirabstractresource.FHIRAbstractResource):
    """ Base Resource.

    This is the base resource type for everything.
    """
    resource_type: ClassVar[str] = "Resource"
    id: Optional[str] = None
    implicitRules: Optional[str] = None
    language: Optional[str] = None
    meta: Optional[meta.Meta] = None

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
#        self.id = None
#        """ Logical id of this artifact.
#        Type `str`
#
#. """
#
#
#        self.implicitRules = None
#        """ A set of rules under which this content was created.
#        Type `str`
#
#. """
#
#
#        self.language = None
#        """ Language of the resource content.
#        Type `str`
#
#. """
#
#
#        self.meta = None
#        """ Metadata about the resource.
#        Type `Meta`
#
# (represented as `dict` in JSON). """
#

#        super(Resource, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Resource, self).elementProperties()
        js.extend([
            ("id", "id", str, {  # #}False, None, {  # #}False),
            ("implicitRules", "implicitRules", str, {  # #}False, None, {  # #}False),
            ("language", "language", str, {  # #}False, None, {  # #}False),
            ("meta", "meta", meta.Meta, {  # #}False, None, {  # #}False),
        ])
        return js