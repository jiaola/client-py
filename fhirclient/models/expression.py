#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Expression) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .element import Element


@dataclass
class Expression(Element):
    """ An expression that can be used to generate a value.

    A expression that is evaluated in a specified context and returns a value.
    The context of use of the expression must specify the context in which the
    expression is evaluated, and how the result of the expression is used.
    """
    resource_type: ClassVar[str] = "Expression"
    description: Optional[str] = None
    expression: Optional[str] = None
    language: str = None
    name: Optional[str] = None
    reference: Optional[str] = None

    def elementProperties(self):
        js = super(Expression, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("language", "language", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("reference", "reference", str, False, None, False),
        ])
        return js