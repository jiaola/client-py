#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/RelatedArtifact) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .element import Element


@dataclass
class RelatedArtifact(Element):
    """ Related artifacts for a knowledge resource.

    Related artifacts such as additional documentation, justification, or
    bibliographic references.
    """
    resource_type: ClassVar[str] = "RelatedArtifact"
    citation: Optional[str] = None
    display: Optional[str] = None
    document: Optional[Attachment] = None
    label: Optional[str] = None
    resource: Optional[str] = None
    type: str = None
    url: Optional[str] = None

    def elementProperties(self):
        js = super(RelatedArtifact, self).elementProperties()
        js.extend([
            ("citation", "citation", str, False, None, False),
            ("display", "display", str, False, None, False),
            ("document", "document", Attachment, False, None, False),
            ("label", "label", str, False, None, False),
            ("resource", "resource", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, False),
        ])
        return js