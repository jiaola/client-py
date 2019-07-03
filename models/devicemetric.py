#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DeviceMetric) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import timing


from . import domainresource

@dataclass
class DeviceMetric(domainresource.DomainResource):
    """ Measurement, calculation or setting capability of a medical device.

    Describes a measurement, calculation or setting capability of a medical
    device.
    """
    resource_type: ClassVar[str] = "DeviceMetric"
    calibration: Optional[List[DeviceMetricCalibration]] = empty_list()
    category: str = None
    color: Optional[str] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    measurementPeriod: Optional[timing.Timing] = None
    operationalStatus: Optional[str] = None
    parent: Optional[fhirreference.FHIRReference] = None
    source: Optional[fhirreference.FHIRReference] = None
    type:codeableconcept.CodeableConcept = None
    unit: Optional[codeableconcept.CodeableConcept] = None

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
#        self.calibration = None
#        """ Describes the calibrations that have been performed or that are
        required to be performed.
#        List of `DeviceMetricCalibration` items
#
# (represented as `dict` in JSON). """
#
#
#        self.category = None
#        """ measurement | setting | calculation | unspecified.
#        Type `str`
#
#. """
#
#
#        self.color = None
#        """ black | red | green | yellow | blue | magenta | cyan | white.
#        Type `str`
#
#. """
#
#
#        self.identifier = None
#        """ Instance identifier.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.measurementPeriod = None
#        """ Describes the measurement repetition time.
#        Type `Timing`
#
# (represented as `dict` in JSON). """
#
#
#        self.operationalStatus = None
#        """ on | off | standby | entered-in-error.
#        Type `str`
#
#. """
#
#
#        self.parent = None
#        """ Describes the link to the parent Device.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.source = None
#        """ Describes the link to the source Device.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ Identity of metric, for example Heart Rate or PEEP Setting.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.unit = None
#        """ Unit of Measure for the Metric.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(DeviceMetric, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceMetric, self).elementProperties()
        js.extend([
            ("calibration", "calibration", DeviceMetricCalibration, {  # #}True, None, {  # #}False),
            ("category", "category", str, {  # #}False, None, {  # #}True),
            ("color", "color", str, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("measurementPeriod", "measurementPeriod", timing.Timing, {  # #}False, None, {  # #}False),
            ("operationalStatus", "operationalStatus", str, {  # #}False, None, {  # #}False),
            ("parent", "parent", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("source", "source", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("unit", "unit", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import timing


from . import backboneelement

@dataclass
class DeviceMetricCalibration(backboneelement.BackboneElement):
    """ Describes the calibrations that have been performed or that are required to
    be performed.
    """
    resource_type: ClassVar[str] = "DeviceMetricCalibration"
    state: Optional[str] = None
    time: Optional[fhirdate.FHIRDate] = None
    type: Optional[str] = None

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
#        self.state = None
#        """ not-calibrated | calibration-required | calibrated | unspecified.
#        Type `str`
#
#. """
#
#
#        self.time = None
#        """ Describes the time last calibration has been performed.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.type = None
#        """ unspecified | offset | gain | two-point.
#        Type `str`
#
#. """
#

#        super(DeviceMetricCalibration, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceMetricCalibration, self).elementProperties()
        js.extend([
            ("state", "state", str, {  # #}False, None, {  # #}False),
            ("time", "time", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("type", "type", str, {  # #}False, None, {  # #}False),
        ])
        return js