#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/VisionPrescription) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity


@dataclass
class VisionPrescriptionLensSpecificationPrism(BackboneElement):
    """ Eye alignment compensation.

    Allows for adjustment on two axis.
    """
    resource_type: ClassVar[str] = "VisionPrescriptionLensSpecificationPrism"
    amount: float = None
    base: str = None

    def elementProperties(self):
        js = super(VisionPrescriptionLensSpecificationPrism, self).elementProperties()
        js.extend([
            ("amount", "amount", float, False, None, True),
            ("base", "base", str, False, None, True),
        ])
        return js


@dataclass
class VisionPrescriptionLensSpecification(BackboneElement):
    """ Vision lens authorization.

    Contain the details of  the individual lens specifications and serves as
    the authorization for the fullfillment by certified professionals.
    """
    resource_type: ClassVar[str] = "VisionPrescriptionLensSpecification"
    add: Optional[float] = None
    axis: Optional[int] = None
    backCurve: Optional[float] = None
    brand: Optional[str] = None
    color: Optional[str] = None
    cylinder: Optional[float] = None
    diameter: Optional[float] = None
    duration: Optional[Quantity] = None
    eye: str = None
    note: Optional[List[Annotation]] = empty_list()
    power: Optional[float] = None
    prism: Optional[List[VisionPrescriptionLensSpecificationPrism]] = empty_list()
    product: CodeableConcept = None
    sphere: Optional[float] = None

    def elementProperties(self):
        js = super(VisionPrescriptionLensSpecification, self).elementProperties()
        js.extend([
            ("add", "add", float, False, None, False),
            ("axis", "axis", int, False, None, False),
            ("backCurve", "backCurve", float, False, None, False),
            ("brand", "brand", str, False, None, False),
            ("color", "color", str, False, None, False),
            ("cylinder", "cylinder", float, False, None, False),
            ("diameter", "diameter", float, False, None, False),
            ("duration", "duration", Quantity, False, None, False),
            ("eye", "eye", str, False, None, True),
            ("note", "note", Annotation, True, None, False),
            ("power", "power", float, False, None, False),
            ("prism", "prism", VisionPrescriptionLensSpecificationPrism, True, None, False),
            ("product", "product", CodeableConcept, False, None, True),
            ("sphere", "sphere", float, False, None, False),
        ])
        return js


@dataclass
class VisionPrescription(DomainResource):
    """ Prescription for vision correction products for a patient.

    An authorization for the provision of glasses and/or contact lenses to a
    patient.
    """
    resource_type: ClassVar[str] = "VisionPrescription"
    created: FHIRDate = None
    dateWritten: FHIRDate = None
    encounter: Optional[FHIRReference] = None
    identifier: Optional[List[Identifier]] = empty_list()
    lensSpecification: List[VisionPrescriptionLensSpecification] = empty_list()
    patient: FHIRReference = None
    prescriber: FHIRReference = None
    status: str = None

    def elementProperties(self):
        js = super(VisionPrescription, self).elementProperties()
        js.extend([
            ("created", "created", FHIRDate, False, None, True),
            ("dateWritten", "dateWritten", FHIRDate, False, None, True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("lensSpecification", "lensSpecification", VisionPrescriptionLensSpecification, True, None, True),
            ("patient", "patient", FHIRReference, False, None, True),
            ("prescriber", "prescriber", FHIRReference, False, None, True),
            ("status", "status", str, False, None, True),
        ])
        return js