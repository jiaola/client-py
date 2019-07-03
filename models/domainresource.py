#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DomainResource) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import extension
from . import narrative
from . import resource


from . import resource

@dataclass
class DomainResource(resource.Resource):
    """ A resource with narrative, extensions, and contained resources.

    A resource that includes narrative, extensions, and contained resources.
    """
    resource_type: ClassVar[str] = "DomainResource"
    contained: Optional[List[resource.Resource]] = empty_list()
    extension: Optional[List[extension.Extension]] = empty_list()
    modifierExtension: Optional[List[extension.Extension]] = empty_list()
    text: Optional[narrative.Narrative] = None

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
#        self.contained = None
#        """ Contained, inline Resources.
#        List of `Resource` items
#
# (represented as `dict` in JSON). """
#
#
#        self.extension = None
#        """ Additional content defined by implementations.
#        List of `Extension` items
#
# (represented as `dict` in JSON). """
#
#
#        self.modifierExtension = None
#        """ Extensions that cannot be ignored.
#        List of `Extension` items
#
# (represented as `dict` in JSON). """
#
#
#        self.text = None
#        """ Text summary of the resource, for human interpretation.
#        Type `Narrative`
#
# (represented as `dict` in JSON). """
#

#        super(DomainResource, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DomainResource, self).elementProperties()
        js.extend([
            ("contained", "contained", resource.Resource, {  # #}True, None, {  # #}False),
            ("extension", "extension", extension.Extension, {  # #}True, None, {  # #}False),
            ("modifierExtension", "modifierExtension", extension.Extension, {  # #}True, None, {  # #}False),
            ("text", "text", narrative.Narrative, {  # #}False, None, {  # #}False),
        ])
        return js