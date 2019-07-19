#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Contributor) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .contactdetail import ContactDetail
from .element import Element


@dataclass
class Contributor(Element):
    """ Contributor information.

    A contributor to the content of a knowledge asset, including authors,
    editors, reviewers, and endorsers.
    """
    resource_type: ClassVar[str] = "Contributor"
    contact: Optional[List[ContactDetail]] = empty_list()
    name: str = None
    type: str = None

    def elementProperties(self):
        js = super(Contributor, self).elementProperties()
        js.extend([
            ("contact", "contact", ContactDetail, True, None, False),
            ("name", "name", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js