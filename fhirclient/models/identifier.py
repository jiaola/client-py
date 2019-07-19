#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Identifier) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .element import Element



@dataclass
class Identifier(Element):
    """ An identifier intended for computation.

    An identifier - identifies some entity uniquely and unambiguously.
    Typically this is used for business identifiers.
    """
    resource_type: ClassVar[str] = "Identifier"
    assigner: Optional["FHIRReference"] = None
    period: Optional["Period"] = None
    system: Optional["str"] = None
    type: Optional["CodeableConcept"] = None
    use: Optional["str"] = None
    value: Optional["str"] = None

    def elementProperties(self):
        from .codeableconcept import CodeableConcept
        from .fhirreference import FHIRReference
        from .period import Period
        
        js = super(Identifier, self).elementProperties()
        js.extend([
            ("assigner", "assigner", FHIRReference, False, None, False),
            ("period", "period", Period, False, None, False),
            ("system", "system", str, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("use", "use", str, False, None, False),
            ("value", "value", str, False, None, False),
        ])
        return js