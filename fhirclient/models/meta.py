#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Meta) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .coding import Coding
from .element import Element
from .fhirdate import FHIRDate


@dataclass
class Meta(Element):
    """ Metadata about a resource.

    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content might not always
    be associated with version changes to the resource.
    """
    resource_type: ClassVar[str] = "Meta"
    lastUpdated: Optional[FHIRDate] = None
    profile: Optional[List[str]] = empty_list()
    security: Optional[List[Coding]] = empty_list()
    source: Optional[str] = None
    tag: Optional[List[Coding]] = empty_list()
    versionId: Optional[str] = None

    def elementProperties(self):
        js = super(Meta, self).elementProperties()
        js.extend([
            ("lastUpdated", "lastUpdated", FHIRDate, False, None, False),
            ("profile", "profile", str, True, None, False),
            ("security", "security", Coding, True, None, False),
            ("source", "source", str, False, None, False),
            ("tag", "tag", Coding, True, None, False),
            ("versionId", "versionId", str, False, None, False),
        ])
        return js