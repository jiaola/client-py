#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicationKnowledge) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import dosage
from . import duration
from . import fhirreference
from . import money
from . import quantity
from . import ratio

from . import backboneelement

@dataclass
class MedicationKnowledgeRelatedMedicationKnowledge(backboneelement.BackboneElement):
    """ Associated or related medication information.

    Associated or related knowledge about a medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeRelatedMedicationKnowledge"
    reference: List[fhirreference.FHIRReference] = empty_list()
    type:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationKnowledgeRelatedMedicationKnowledge, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, True, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class MedicationKnowledgeRegulatorySubstitution(backboneelement.BackboneElement):
    """ Specifies if changes are allowed when dispensing a medication from a
    regulatory perspective.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeRegulatorySubstitution"
    allowed: bool = None
    type:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatorySubstitution, self).elementProperties()
        js.extend([
            ("allowed", "allowed", bool, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class MedicationKnowledgeRegulatorySchedule(backboneelement.BackboneElement):
    """ Specifies the schedule of a medication in jurisdiction.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeRegulatorySchedule"
    schedule:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatorySchedule, self).elementProperties()
        js.extend([
            ("schedule", "schedule", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class MedicationKnowledgeRegulatoryMaxDispense(backboneelement.BackboneElement):
    """ The maximum number of units of the medication that can be dispensed in a
    period.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeRegulatoryMaxDispense"
    period: Optional[duration.Duration] = None
    quantity:quantity.Quantity = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatoryMaxDispense, self).elementProperties()
        js.extend([
            ("period", "period", duration.Duration, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, True),
        ])
        return js

@dataclass
class MedicationKnowledgeRegulatory(backboneelement.BackboneElement):
    """ Regulatory information about a medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeRegulatory"
    maxDispense: Optional[MedicationKnowledgeRegulatoryMaxDispense] = None
    regulatoryAuthority:fhirreference.FHIRReference = None
    schedule: Optional[List[MedicationKnowledgeRegulatorySchedule]] = empty_list()
    substitution: Optional[List[MedicationKnowledgeRegulatorySubstitution]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatory, self).elementProperties()
        js.extend([
            ("maxDispense", "maxDispense", MedicationKnowledgeRegulatoryMaxDispense, False, None, False),
            ("regulatoryAuthority", "regulatoryAuthority", fhirreference.FHIRReference, False, None, True),
            ("schedule", "schedule", MedicationKnowledgeRegulatorySchedule, True, None, False),
            ("substitution", "substitution", MedicationKnowledgeRegulatorySubstitution, True, None, False),
        ])
        return js

@dataclass
class MedicationKnowledgePackaging(backboneelement.BackboneElement):
    """ Details about packaged medications.

    Information that only applies to packages (not products).
    """
    resource_type: ClassVar[str] = "MedicationKnowledgePackaging"
    quantity: Optional[quantity.Quantity] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationKnowledgePackaging, self).elementProperties()
        js.extend([
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class MedicationKnowledgeMonograph(backboneelement.BackboneElement):
    """ Associated documentation about the medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeMonograph"
    source: Optional[fhirreference.FHIRReference] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationKnowledgeMonograph, self).elementProperties()
        js.extend([
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class MedicationKnowledgeMonitoringProgram(backboneelement.BackboneElement):
    """ Program under which a medication is reviewed.

    The program under which the medication is reviewed.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeMonitoringProgram"
    name: Optional[str] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationKnowledgeMonitoringProgram, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class MedicationKnowledgeMedicineClassification(backboneelement.BackboneElement):
    """ Categorization of the medication within a formulary or classification
    system.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeMedicineClassification"
    classification: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    type:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationKnowledgeMedicineClassification, self).elementProperties()
        js.extend([
            ("classification", "classification", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class MedicationKnowledgeKinetics(backboneelement.BackboneElement):
    """ The time course of drug absorption, distribution, metabolism and excretion
    of a medication from the body.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeKinetics"
    areaUnderCurve: Optional[List[quantity.Quantity]] = empty_list()
    halfLifePeriod: Optional[duration.Duration] = None
    lethalDose50: Optional[List[quantity.Quantity]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationKnowledgeKinetics, self).elementProperties()
        js.extend([
            ("areaUnderCurve", "areaUnderCurve", quantity.Quantity, True, None, False),
            ("halfLifePeriod", "halfLifePeriod", duration.Duration, False, None, False),
            ("lethalDose50", "lethalDose50", quantity.Quantity, True, None, False),
        ])
        return js

@dataclass
class MedicationKnowledgeIngredient(backboneelement.BackboneElement):
    """ Active or inactive ingredient.

    Identifies a particular constituent of interest in the product.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeIngredient"
    isActive: Optional[bool] = None
    itemCodeableConcept:codeableconcept.CodeableConcept = None
    itemReference:fhirreference.FHIRReference = None
    strength: Optional[ratio.Ratio] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationKnowledgeIngredient, self).elementProperties()
        js.extend([
            ("isActive", "isActive", bool, False, None, False),
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", True),
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", True),
            ("strength", "strength", ratio.Ratio, False, None, False),
        ])
        return js

@dataclass
class MedicationKnowledgeDrugCharacteristic(backboneelement.BackboneElement):
    """ Specifies descriptive properties of the medicine.

    Specifies descriptive properties of the medicine, such as color, shape,
    imprints, etc.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeDrugCharacteristic"
    type: Optional[codeableconcept.CodeableConcept] = None
    valueBase64Binary: Optional[str] = None
    valueCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    valueQuantity: Optional[quantity.Quantity] = None
    valueString: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationKnowledgeDrugCharacteristic, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
        ])
        return js

@dataclass
class MedicationKnowledgeCost(backboneelement.BackboneElement):
    """ The pricing of the medication.

    The price of the medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeCost"
    cost:money.Money = None
    source: Optional[str] = None
    type:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationKnowledgeCost, self).elementProperties()
        js.extend([
            ("cost", "cost", money.Money, False, None, True),
            ("source", "source", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics(backboneelement.BackboneElement):
    """ Characteristics of the patient that are relevant to the administration
    guidelines.

    Characteristics of the patient that are relevant to the administration
    guidelines (for example, height, weight, gender, etc.).
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics"
    characteristicCodeableConcept:codeableconcept.CodeableConcept = None
    characteristicQuantity:quantity.Quantity = None
    value: Optional[List[str]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics, self).elementProperties()
        js.extend([
            ("characteristicCodeableConcept", "characteristicCodeableConcept", codeableconcept.CodeableConcept, False, "characteristic", True),
            ("characteristicQuantity", "characteristicQuantity", quantity.Quantity, False, "characteristic", True),
            ("value", "value", str, True, None, False),
        ])
        return js

@dataclass
class MedicationKnowledgeAdministrationGuidelinesDosage(backboneelement.BackboneElement):
    """ Dosage for the medication for the specific guidelines.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeAdministrationGuidelinesDosage"
    dosage: List[dosage.Dosage] = empty_list()
    type:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationKnowledgeAdministrationGuidelinesDosage, self).elementProperties()
        js.extend([
            ("dosage", "dosage", dosage.Dosage, True, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class MedicationKnowledgeAdministrationGuidelines(backboneelement.BackboneElement):
    """ Guidelines for administration of the medication.

    Guidelines for the administration of the medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeAdministrationGuidelines"
    dosage: Optional[List[MedicationKnowledgeAdministrationGuidelinesDosage]] = empty_list()
    indicationCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    indicationReference: Optional[fhirreference.FHIRReference] = None
    patientCharacteristics: Optional[List[MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationKnowledgeAdministrationGuidelines, self).elementProperties()
        js.extend([
            ("dosage", "dosage", MedicationKnowledgeAdministrationGuidelinesDosage, True, None, False),
            ("indicationCodeableConcept", "indicationCodeableConcept", codeableconcept.CodeableConcept, False, "indication", False),
            ("indicationReference", "indicationReference", fhirreference.FHIRReference, False, "indication", False),
            ("patientCharacteristics", "patientCharacteristics", MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics, True, None, False),
        ])
        return js

from . import domainresource

@dataclass
class MedicationKnowledge(domainresource.DomainResource):
    """ Definition of Medication Knowledge.

    Information about a medication that is used to support knowledge.
    """
    resource_type: ClassVar[str] = "MedicationKnowledge"
    administrationGuidelines: Optional[List[MedicationKnowledgeAdministrationGuidelines]] = empty_list()
    amount: Optional[quantity.Quantity] = None
    associatedMedication: Optional[List[fhirreference.FHIRReference]] = empty_list()
    code: Optional[codeableconcept.CodeableConcept] = None
    contraindication: Optional[List[fhirreference.FHIRReference]] = empty_list()
    cost: Optional[List[MedicationKnowledgeCost]] = empty_list()
    doseForm: Optional[codeableconcept.CodeableConcept] = None
    drugCharacteristic: Optional[List[MedicationKnowledgeDrugCharacteristic]] = empty_list()
    ingredient: Optional[List[MedicationKnowledgeIngredient]] = empty_list()
    intendedRoute: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    kinetics: Optional[List[MedicationKnowledgeKinetics]] = empty_list()
    manufacturer: Optional[fhirreference.FHIRReference] = None
    medicineClassification: Optional[List[MedicationKnowledgeMedicineClassification]] = empty_list()
    monitoringProgram: Optional[List[MedicationKnowledgeMonitoringProgram]] = empty_list()
    monograph: Optional[List[MedicationKnowledgeMonograph]] = empty_list()
    packaging: Optional[MedicationKnowledgePackaging] = None
    preparationInstruction: Optional[str] = None
    productType: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    regulatory: Optional[List[MedicationKnowledgeRegulatory]] = empty_list()
    relatedMedicationKnowledge: Optional[List[MedicationKnowledgeRelatedMedicationKnowledge]] = empty_list()
    status: Optional[str] = None
    synonym: Optional[List[str]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationKnowledge, self).elementProperties()
        js.extend([
            ("administrationGuidelines", "administrationGuidelines", MedicationKnowledgeAdministrationGuidelines, True, None, False),
            ("amount", "amount", quantity.Quantity, False, None, False),
            ("associatedMedication", "associatedMedication", fhirreference.FHIRReference, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("contraindication", "contraindication", fhirreference.FHIRReference, True, None, False),
            ("cost", "cost", MedicationKnowledgeCost, True, None, False),
            ("doseForm", "doseForm", codeableconcept.CodeableConcept, False, None, False),
            ("drugCharacteristic", "drugCharacteristic", MedicationKnowledgeDrugCharacteristic, True, None, False),
            ("ingredient", "ingredient", MedicationKnowledgeIngredient, True, None, False),
            ("intendedRoute", "intendedRoute", codeableconcept.CodeableConcept, True, None, False),
            ("kinetics", "kinetics", MedicationKnowledgeKinetics, True, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False, None, False),
            ("medicineClassification", "medicineClassification", MedicationKnowledgeMedicineClassification, True, None, False),
            ("monitoringProgram", "monitoringProgram", MedicationKnowledgeMonitoringProgram, True, None, False),
            ("monograph", "monograph", MedicationKnowledgeMonograph, True, None, False),
            ("packaging", "packaging", MedicationKnowledgePackaging, False, None, False),
            ("preparationInstruction", "preparationInstruction", str, False, None, False),
            ("productType", "productType", codeableconcept.CodeableConcept, True, None, False),
            ("regulatory", "regulatory", MedicationKnowledgeRegulatory, True, None, False),
            ("relatedMedicationKnowledge", "relatedMedicationKnowledge", MedicationKnowledgeRelatedMedicationKnowledge, True, None, False),
            ("status", "status", str, False, None, False),
            ("synonym", "synonym", str, True, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import dosage
except ImportError:
    dosage = sys.modules[__package__ + '.dosage']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']