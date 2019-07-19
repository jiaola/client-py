#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DeviceMetric) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .timing import Timing


@dataclass
class DeviceMetricCalibration(BackboneElement):
    """ Describes the calibrations that have been performed or that are required to
    be performed.
    """
    resource_type: ClassVar[str] = "DeviceMetricCalibration"
    state: Optional[str] = None
    time: Optional[FHIRDate] = None
    type: Optional[str] = None

    def elementProperties(self):
        js = super(DeviceMetricCalibration, self).elementProperties()
        js.extend([
            ("state", "state", str, False, None, False),
            ("time", "time", FHIRDate, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


@dataclass
class DeviceMetric(DomainResource):
    """ Measurement, calculation or setting capability of a medical device.

    Describes a measurement, calculation or setting capability of a medical
    device.
    """
    resource_type: ClassVar[str] = "DeviceMetric"
    calibration: Optional[List[DeviceMetricCalibration]] = empty_list()
    category: str = None
    color: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    measurementPeriod: Optional[Timing] = None
    operationalStatus: Optional[str] = None
    parent: Optional[FHIRReference] = None
    source: Optional[FHIRReference] = None
    type: CodeableConcept = None
    unit: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(DeviceMetric, self).elementProperties()
        js.extend([
            ("calibration", "calibration", DeviceMetricCalibration, True, None, False),
            ("category", "category", str, False, None, True),
            ("color", "color", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("measurementPeriod", "measurementPeriod", Timing, False, None, False),
            ("operationalStatus", "operationalStatus", str, False, None, False),
            ("parent", "parent", FHIRReference, False, None, False),
            ("source", "source", FHIRReference, False, None, False),
            ("type", "type", CodeableConcept, False, None, True),
            ("unit", "unit", CodeableConcept, False, None, False),
        ])
        return js