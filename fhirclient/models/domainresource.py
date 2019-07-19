#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DomainResource) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .extension import Extension
from .narrative import Narrative
from .resource import Resource


@dataclass
class DomainResource(Resource):
    """ A resource with narrative, extensions, and contained resources.

    A resource that includes narrative, extensions, and contained resources.
    """
    resource_type: ClassVar[str] = "DomainResource"
    contained: Optional[List[Resource]] = empty_list()
    extension: Optional[List[Extension]] = empty_list()
    modifierExtension: Optional[List[Extension]] = empty_list()
    text: Optional[Narrative] = None

    def elementProperties(self):
        js = super(DomainResource, self).elementProperties()
        js.extend([
            ("contained", "contained", Resource, True, None, False),
            ("extension", "extension", Extension, True, None, False),
            ("modifierExtension", "modifierExtension", Extension, True, None, False),
            ("text", "text", Narrative, False, None, False),
        ])
        return js