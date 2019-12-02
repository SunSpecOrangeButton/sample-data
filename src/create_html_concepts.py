# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This HTML viewpoints of Orange Button Entrypoints.

NOTE: This is in a very early and experimental mode.  Reading the relationships
is somewhat trial and error and needs extensive update.  Github is being primarily
used as Backup at this point and this is in no way ready for general usage.
"""

from oblib import taxonomy

import re
import sys

def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1)

TYPES = {    
    "dei:legalEntityIdentifierItemType": "String",
    "nonnum:domainItemType": "String",
    "num-us:electricCurrentItemType":  "Float",
    "num-us:frequencyItemType": "Float",
    "num-us:insolationItemType": "Float",
    "num-us:irradianceItemType": "Float",
    "num-us:planeAngleItemType": "Float",
    "num-us:pressureItemType": "Float",
    "num-us:speedItemType": "Float",
    "num-us:temperatureItemType": "Float",
    "num-us:voltageItemType": "Float",
    "num:areaItemType": "Float",
    "num:energyItemType": "Float",
    "num:lengthItemType": "Float",
    "num:massItemType": "Float",
    "num:percentItemType": "Float",
    "num:powerItemType": "Float",
    "num:volumeItemType": "Float",
    "solar-types:DERItemType": "Enumeration",
    "solar-types:aLTASurveyItemType": "Enumeration",
    "solar-types:approvalRequestItemType": "Enumeration",
    "solar-types:approvalStatusItemType": "Enumeration",
    "solar-types:assetSecuredItemType": "Enumeration",
    "solar-types:batteryChemistryItemType": "Enumeration",
    "solar-types:batteryConnectionItemType": "Enumeration",
    "solar-types:climateClassificationKoppenItemType": "Enumeration",
    "solar-types:climateZoneANSIItemType": "Enumeration",
    "solar-types:communicationProtocolItemType": "Enumeration",
    "solar-types:creditSupportStatusItemType": "Enumeration",
    "solar-types:deviceItemType": "Enumeration",
    "solar-types:distributedGenOrUtilityScaleItemType": "Enumeration",
    "solar-types:divisionStateApprovalStatusItemType": "Enumeration",
    "solar-types:employeeLevelItemType": "Enumeration",
    "solar-types:employeeRoleItemType": "Enumeration",
    "solar-types:energyBudgetPhaseItemType": "Enumeration",
    "solar-types:eventSeverityItemType": "Enumeration",
    "solar-types:eventStatusItemType": "Enumeration",
    "solar-types:feeStatusItemType": "Enumeration",
    "solar-types:financialTransactionItemType": "Enumeration",
    "solar-types:financingEventItemType": "Enumeration",
    "solar-types:fundOrProjectItemType": "Enumeration",
    "solar-types:fundStatusItemType": "Enumeration",
    "solar-types:gISFileFormatItemType": "Enumeration",
    "solar-types:hedgeItemType": "Enumeration",
    "solar-types:insuranceItemType": "Enumeration",
    "solar-types:internetConnectionItemType": "Enumeration",
    "solar-types:inverterItemType": "Enumeration",
    "solar-types:inverterPhaseItemType": "Enumeration",
    "solar-types:investmentStatusItemType": "Enumeration",
    "solar-types:mORLevelItemType": "Enumeration",
    "solar-types:moduleItemType": "Enumeration",
    "solar-types:moduleOrientationItemType": "Enumeration",
    "solar-types:moduleTechnologyItemType": "Enumeration",
    "solar-types:mountingItemType": "Enumeration",
    "solar-types:occupancyItemType": "Enumeration",
    "solar-types:optimizerTypeItemType": "Enumeration",
    "solar-types:participantItemType": "Enumeration",
    "solar-types:preventiveMaintenanceTaskStatusItemType": "Enumeration",
    "solar-types:projectAssetTypeItemType": "Enumeration",
    "solar-types:projectClassItemType": "Enumeration",
    "solar-types:projectInterconnectionItemType": "Enumeration",
    "solar-types:projectPhaseItemType": "Enumeration",
    "solar-types:projectStageItemType": "Enumeration",
    "solar-types:regulatoryApprovalStatusItemType": "Enumeration",
    "solar-types:regulatoryFacilityItemType": "Enumeration",
    "solar-types:reserveCollateralItemType": "Enumeration",
    "solar-types:reserveUseItemType": "Enumeration",
    "solar-types:roofItemType": "Enumeration",
    "solar-types:roofSlopeItemType": "Enumeration",
    "solar-types:securityInterestItemType": "Enumeration",
    "solar-types:securityInterestStatusItemType": "Enumeration",
    "solar-types:siteControlItemType": "Enumeration",
    "solar-types:solarSystemCharacterItemType": "Enumeration",
    "solar-types:sparePartsStatusItemType": "Enumeration",
    "solar-types:sPVOrCounterpartyItemType": "Enumeration",
    "solar-types:systemAvailabilityModeItemType": "Enumeration",
    "solar-types:systemOperationalStatusItemType": "Enumeration",
    "solar-types:titlePolicyInsuranceItemType": "Enumeration",
    "solar-types:trackerItemType": "Enumeration",
    "solar-types:uuidItemType": "String",
    "solar-types:uuidXbrlItemType": "String",
    "solar-types:zoningPermitPropertyItemType": "Enumeration",
    "us-types:perUnitItemType": "String",
    "xbrli:anyURIItemType": "String",
    "xbrli:booleanItemType": "Boolean",
    "xbrli:dateItemType": "Date",
    "xbrli:decimalItemType": "Float",
    "xbrli:durationItemType": "String",
    "xbrli:integerItemType": "Integer",
    "xbrli:monetaryItemType": "Float",
    "xbrli:normalizedStringItemType": "String",
    "xbrli:pureItemType": "String",
    "xbrli:stringItemType": "String"

}


tax = taxonomy.Taxonomy()

if len(sys.argv) != 2:
    print("Incorrect number of arguments - 1 required")
    print("  Path to Output directory (example: ./somepath/outdir)")
    sys.exit(1)

with open(sys.argv[1] + "/" + "concepts.html", "w") as out:
    out.write("<html>")
    out.write("  <body>")
    out.write("     <h1>Concepts</h1>")

    for concept in tax.semantic.get_all_concepts(details=True):
        details = tax.semantic.get_concept_details(concept)
        if not details.abstract:
            out.write("      <h2>" + concept.replace("dei:", "").replace("us-gaap:", "").replace("solar:", "") + "</h2>")
            out.write("      <ul>")

            out.write("        <li>Label: " + convert(details.name) + "</li>")

            t = "SOLAR"
            if details.id.startswith("us-gaap:"):
                t = "US-GAAP"
            elif details.id.startswith("dei:"):
                t = "DEI"
            out.write("        <li>Taxonomy: " + t + "</li>")
            out.write("        <li>Item Type: " + details.type_name.split(":")[1].replace("ItemType", "") + "</li>")
            out.write("        <li>Data Type: " + TYPES[details.type_name].lower() + "</li>")

            period = details.period_type.value
            if period == "instant":
                period = "Instant in time"
            else:
                period = "Period of time"
            out.write("        <li>Period: " + details.period_type.value + "</li>")
            out.write("        <li>Nillable: " + str(details.nillable) + "</li>")

            docs = tax.documentation.get_concept_documentation(concept)
            if docs is None:
                docs = ""
            out.write("        <li>Description: " + docs + "</li>")

            out.write("        <li>Entrypoints present in: ")
            for entrypoint in tax.semantic.get_all_entrypoints():
                if entrypoint != "All":
                    if concept in tax.semantic.get_entrypoint_concepts(entrypoint):
                        out.write(entrypoint + " ")

            if concept == "us-gaap:Revenues":
                calc = "Other Income + RebateRevenue + PeformanceBasedIncentiveRevenue + Electrical Generation Revenue = Revenues"
            else:
                calc = "N/A"
            out.write("        <li>Calculations: " + calc + "</li>")
            out.write("</li>")
            out.write("      </ul>")
    out.write("  </body>")
    out.write("</html>")