#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductIngredient) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirreference
from . import identifier
from . import ratio


from . import domainresource

@dataclass
class MedicinalProductIngredient(domainresource.DomainResource):
    """ An ingredient of a manufactured item or pharmaceutical product.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredient"
    allergenicIndicator: Optional[bool] = None
    identifier: Optional[identifier.Identifier] = None
    manufacturer: Optional[List[fhirreference.FHIRReference]] = empty_list()
    role:codeableconcept.CodeableConcept = None
    specifiedSubstance: Optional[List[MedicinalProductIngredientSpecifiedSubstance]] = empty_list()
    substance: Optional[MedicinalProductIngredientSubstance] = None

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
#        self.allergenicIndicator = None
#        """ If the ingredient is a known or suspected allergen.
#        Type `bool`
#
#. """
#
#
#        self.identifier = None
#        """ Identifier for the ingredient.
#        Type `Identifier`
#
# (represented as `dict` in JSON). """
#
#
#        self.manufacturer = None
#        """ Manufacturer of this Ingredient.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.role = None
#        """ Ingredient role e.g. Active ingredient, excipient.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.specifiedSubstance = None
#        """ A specified substance that comprises this ingredient.
#        List of `MedicinalProductIngredientSpecifiedSubstance` items
#
# (represented as `dict` in JSON). """
#
#
#        self.substance = None
#        """ The ingredient substance.
#        Type `MedicinalProductIngredientSubstance`
#
# (represented as `dict` in JSON). """
#

#        super(MedicinalProductIngredient, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicinalProductIngredient, self).elementProperties()
        js.extend([
            ("allergenicIndicator", "allergenicIndicator", bool, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}False, None, {  # #}False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("role", "role", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("specifiedSubstance", "specifiedSubstance", MedicinalProductIngredientSpecifiedSubstance, {  # #}True, None, {  # #}False),
            ("substance", "substance", MedicinalProductIngredientSubstance, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import fhirreference
from . import identifier
from . import ratio


from . import backboneelement

@dataclass
class MedicinalProductIngredientSpecifiedSubstance(backboneelement.BackboneElement):
    """ A specified substance that comprises this ingredient.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredientSpecifiedSubstance"
    code:codeableconcept.CodeableConcept = None
    confidentiality: Optional[codeableconcept.CodeableConcept] = None
    group:codeableconcept.CodeableConcept = None
    strength: Optional[List[MedicinalProductIngredientSpecifiedSubstanceStrength]] = empty_list()

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
#        self.code = None
#        """ The specified substance.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.confidentiality = None
#        """ Confidentiality level of the specified substance as the ingredient.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.group = None
#        """ The group of specified substance, e.g. group 1 to 4.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.strength = None
#        """ Quantity of the substance or specified substance present in the
        manufactured item or pharmaceutical product.
#        List of `MedicinalProductIngredientSpecifiedSubstanceStrength` items
#
# (represented as `dict` in JSON). """
#

#        super(MedicinalProductIngredientSpecifiedSubstance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicinalProductIngredientSpecifiedSubstance, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("confidentiality", "confidentiality", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("group", "group", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("strength", "strength", MedicinalProductIngredientSpecifiedSubstanceStrength, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import ratio


@dataclass
class MedicinalProductIngredientSpecifiedSubstanceStrength(backboneelement.BackboneElement):
    """ Quantity of the substance or specified substance present in the
    manufactured item or pharmaceutical product.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredientSpecifiedSubstanceStrength"
    concentration: Optional[ratio.Ratio] = None
    concentrationLowLimit: Optional[ratio.Ratio] = None
    country: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    measurementPoint: Optional[str] = None
    presentation:ratio.Ratio = None
    presentationLowLimit: Optional[ratio.Ratio] = None
    referenceStrength: Optional[List[MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength]] = empty_list()

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
#        self.concentration = None
#        """ The strength per unitary volume (or mass).
#        Type `Ratio`
#
# (represented as `dict` in JSON). """
#
#
#        self.concentrationLowLimit = None
#        """ A lower limit for the strength per unitary volume (or mass), for
        when there is a range. The concentration attribute then becomes the
        upper limit.
#        Type `Ratio`
#
# (represented as `dict` in JSON). """
#
#
#        self.country = None
#        """ The country or countries for which the strength range applies.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.measurementPoint = None
#        """ For when strength is measured at a particular point or distance.
#        Type `str`
#
#. """
#
#
#        self.presentation = None
#        """ The quantity of substance in the unit of presentation, or in the
        volume (or mass) of the single pharmaceutical product or
        manufactured item.
#        Type `Ratio`
#
# (represented as `dict` in JSON). """
#
#
#        self.presentationLowLimit = None
#        """ A lower limit for the quantity of substance in the unit of
        presentation. For use when there is a range of strengths, this is
        the lower limit, with the presentation attribute becoming the upper
        limit.
#        Type `Ratio`
#
# (represented as `dict` in JSON). """
#
#
#        self.referenceStrength = None
#        """ Strength expressed in terms of a reference substance.
#        List of `MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength` items
#
# (represented as `dict` in JSON). """
#

#        super(MedicinalProductIngredientSpecifiedSubstanceStrength, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicinalProductIngredientSpecifiedSubstanceStrength, self).elementProperties()
        js.extend([
            ("concentration", "concentration", ratio.Ratio, {  # #}False, None, {  # #}False),
            ("concentrationLowLimit", "concentrationLowLimit", ratio.Ratio, {  # #}False, None, {  # #}False),
            ("country", "country", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("measurementPoint", "measurementPoint", str, {  # #}False, None, {  # #}False),
            ("presentation", "presentation", ratio.Ratio, {  # #}False, None, {  # #}True),
            ("presentationLowLimit", "presentationLowLimit", ratio.Ratio, {  # #}False, None, {  # #}False),
            ("referenceStrength", "referenceStrength", MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import ratio


@dataclass
class MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength(backboneelement.BackboneElement):
    """ Strength expressed in terms of a reference substance.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength"
    country: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    measurementPoint: Optional[str] = None
    strength:ratio.Ratio = None
    strengthLowLimit: Optional[ratio.Ratio] = None
    substance: Optional[codeableconcept.CodeableConcept] = None

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
#        self.country = None
#        """ The country or countries for which the strength range applies.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.measurementPoint = None
#        """ For when strength is measured at a particular point or distance.
#        Type `str`
#
#. """
#
#
#        self.strength = None
#        """ Strength expressed in terms of a reference substance.
#        Type `Ratio`
#
# (represented as `dict` in JSON). """
#
#
#        self.strengthLowLimit = None
#        """ Strength expressed in terms of a reference substance.
#        Type `Ratio`
#
# (represented as `dict` in JSON). """
#
#
#        self.substance = None
#        """ Relevant reference substance.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength, self).elementProperties()
        js.extend([
            ("country", "country", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("measurementPoint", "measurementPoint", str, {  # #}False, None, {  # #}False),
            ("strength", "strength", ratio.Ratio, {  # #}False, None, {  # #}True),
            ("strengthLowLimit", "strengthLowLimit", ratio.Ratio, {  # #}False, None, {  # #}False),
            ("substance", "substance", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import ratio


@dataclass
class MedicinalProductIngredientSubstance(backboneelement.BackboneElement):
    """ The ingredient substance.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredientSubstance"
    code:codeableconcept.CodeableConcept = None
    strength: Optional[List[MedicinalProductIngredientSpecifiedSubstanceStrength]] = empty_list()

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
#        self.code = None
#        """ The ingredient substance.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.strength = None
#        """ Quantity of the substance or specified substance present in the
        manufactured item or pharmaceutical product.
#        List of `MedicinalProductIngredientSpecifiedSubstanceStrength` items
#
# (represented as `dict` in JSON). """
#

#        super(MedicinalProductIngredientSubstance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicinalProductIngredientSubstance, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("strength", "strength", MedicinalProductIngredientSpecifiedSubstanceStrength, {  # #}True, None, {  # #}False),
        ])
        return js