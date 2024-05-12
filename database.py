import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate("lease-summarization-firebase-adminsdk-73zq4-49a66ec68b.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
'''
glossary = {
    "Tenant": "A person or entity who rents or leases property from a landlord.",
    "Landlord": "A person or entity who owns property and leases it to a tenant.",
    "Lease Term": "The duration for which the lease agreement is valid, typically expressed in months or years.",
    "Security Deposit": "A sum of money paid by the tenant to the landlord at the beginning of the lease term to cover any damages to the property or unpaid rent.",
    "Utilities": "Services such as water, electricity, gas, and trash collection that are necessary for the occupancy of the property.",
    "Sublease": "A lease agreement between the original tenant (sublessor) and a new tenant (sublessee) to rent the property for a portion of the original lease term.",
    "Eviction": "The legal process by which a landlord removes a tenant from the property for violating the terms of the lease agreement or failing to pay rent.",
    "Notice to Vacate": "A written notice from either the landlord or tenant informing the other party of their intention to end the lease agreement and vacate the property.",
    "Quiet Enjoyment": "The right of the tenant to peacefully and undisturbedly occupy the property without interference from the landlord.",
    "Lease Renewal": "The process by which the lease agreement is extended for an additional term after the initial lease term expires.",
    "Landlord's Insurance": "Insurance coverage purchased by the landlord to protect against property damage, liability claims, and loss of rental income.",
    "Tenant's Insurance (Renter's Insurance)": "Insurance coverage purchased by the tenant to protect personal belongings and provide liability coverage while renting the property.",
    "Lease Violation": "Any breach of the terms and conditions outlined in the lease agreement by either the landlord or tenant.",
    "Lease Amendment": "A formal change or modification to the original lease agreement, typically agreed upon by both the landlord and tenant.",
    "Rent Arrears": "Unpaid rent that is past due and owed to the landlord by the tenant.",
    "Notice Period": "The amount of advance notice required by either party (landlord or tenant) before making changes to the lease agreement or terminating the tenancy.",
    "Holding Over": "The act of a tenant remaining in the rental property after the lease term has expired without signing a new lease agreement.",
    "Pet Policy": "Rules and regulations established by the landlord regarding the keeping of pets on the rental property, including any associated fees or restrictions.",
    "Abandonment": "The act of a tenant leaving the rental property without notice or justification, effectively surrendering possession to the landlord.",
    "Subletting": "The process by which a tenant rents out all or part of the leased premises to another party, known as a subtenant, with the consent of the landlord.",
    "Holdover Tenant": "A tenant who continues to occupy the rental property after the expiration of the lease term without signing a new lease agreement.",
    "Tenant Improvements": "Alterations, additions, or improvements made to the rental property by the tenant with the landlord's permission.",
    "Early Termination Fee": "A fee charged to the tenant for terminating the lease agreement before the expiration of the lease term.",
    "Warranty of Habitability": "The landlord's obligation to provide a rental property that is safe, sanitary, and fit for human habitation.",
    "Substantial Damage": "Significant physical harm or destruction to the rental property, often requiring repairs or restoration.",
    "Utilities Disconnection": "The termination or interruption of essential utility services, such as water, electricity, or gas, to the rental property.",
    "Rent Control": "Government-imposed restrictions on the amount or frequency of rent increases for residential rental properties.",
    "Fair Housing Laws": "Federal, state, and local laws that prohibit discrimination in housing based on race, color, religion, national origin, sex, familial status, or disability.",
    "Quiet Title Action": "A legal proceeding to establish or clarify ownership of real property and resolve any disputes or claims to the property.",
    "Tenant Screening": "The process of evaluating potential tenants' rental history, creditworthiness, and background to assess their suitability as renters.",
    "Right of First Refusal": "The right granted to a tenant to match or exceed any offer made by a third party to purchase or lease the rental property.",
    "Joint and Several Liability": "A legal principle whereby each tenant in a lease agreement is individually and collectively responsible for fulfilling the terms of the lease, including payment of rent and damages.",
    "Abatement of Rent": "A temporary reduction or suspension of rent payments granted by the landlord to the tenant, often due to circumstances such as property damage or loss of essential services.",
    "Rent Concession": "A temporary reduction or discount in the rental rate offered by the landlord to attract tenants or incentivize lease agreements.",
    "Tenancy at Will": "A rental agreement that allows either the landlord or tenant to terminate the tenancy at any time without cause or penalty, typically with advance notice.",
    "Common Areas": "Shared spaces within a rental property, such as lobbies, hallways, elevators, and recreational facilities, used by multiple tenants.",
    "Implied Warranty of Quiet Enjoyment": "An implied promise in every lease agreement that the tenant will have the right to peacefully and undisturbedly enjoy the rental property without interference from the landlord or third parties.",
    "Constructive Eviction": "A legal doctrine that allows a tenant to terminate the lease agreement and vacate the rental property if the landlord fails to provide essential services or maintains conditions that render the property uninhabitable.",
    "Rent Stabilization": "Similar to rent control, rent stabilization refers to regulations that limit the amount or frequency of rent increases for residential rental properties, often with provisions for exceptions and adjustments.",
    "HUD (Housing and Urban Development)": "A federal agency responsible for enforcing fair housing laws, providing affordable housing assistance, and promoting community development.",
    "Termination Clause": "A provision in the lease agreement that outlines the conditions and requirements for terminating the lease, including notice periods and any associated penalties or fees.",
    "Zoning Laws": "Local regulations that govern the use of land and buildings within a municipality, including restrictions on residential, commercial, and industrial activities.",
    "Estoppel Certificate": "A legal document signed by a tenant confirming certain facts about the lease agreement, such as the lease term, rent amount, and security deposit, often requested by lenders or prospective buyers during property transactions.",
    "Code Compliance":"The requirement for rental properties to adhere to building codes, health and safety regulations, and other legal standards established by local authorities."
}


coll_ref = db.collection('glossary')

for term,definition in glossary.items():
    doc_ref = coll_ref.document(term)
    doc_ref.set({"definition":definition})
word = 'Tenant'
doc_ref = coll_ref.document(word)
doc = doc_ref.get()
if doc.exists:
    definition = doc.to_dict()["definition"]
    print(definition)
else:
    print("No definition found")
'''
rental_laws = {
    "Security Deposit Limits": {
        "Description": "Limits the maximum amount a landlord can charge as a security deposit.",
        "Acts": ["California Civil Code Section 1950.5", "New York Real Property Law Section 7-103"],
        "Charges": {
            "California": "Two months' rent for unfurnished units; three months' rent for furnished units.",
            "New York": "One month's rent for unfurnished units; two months' rent for furnished units."
        },
        "In Favor of Tenant": True,
        "Keywords": ["security deposit", "deposit limits"]
    },
    "Rent Increase Notice Period": {
        "Description": "Specifies the notice period landlords must provide tenants before increasing the rent.",
        "Acts": ["California Civil Code Section 1946.2", "New York Real Property Law Section 235-f"],
        "Charges": {
            "California": "30 days' notice for increases less than 10% of the lowest rent charged in the last 12 months; 60 days' notice for increases of 10% or more.",
            "New York": "30 days' notice for month-to-month tenants; 90 days' notice for tenants with a lease term of one year or more."
        },
        "In Favor of Tenant": True,
        "Keywords": ["rent increase", "notice period"]
    },
    "Rent Payment Methods": {
        "Description": "Specifies acceptable methods of rent payment.",
        "Acts": ["California Civil Code Section 1962", "New York Real Property Law Section 235-h"],
        "Charges": {
            "California": "Landlords must accept at least one form of payment that is not cash, unless tenant requests cash payment.",
            "New York": "Landlords must accept personal checks, cashier's checks, money orders, or electronic payments."
        },
        "In Favor of Tenant": True,
        "Keywords": ["rent payment", "payment methods"]
    },
    "Right to Repair": {
        "Description": "Grants tenants the right to request repairs for essential services.",
        "Acts": ["California Civil Code Section 1941.1", "New York Real Property Law Section 235-bb"],
        "Charges": {
            "California": "If landlord fails to repair within a reasonable time, tenant may make repairs and deduct costs from rent.",
            "New York": "Tenant may withhold rent until repairs are made, or seek legal remedies."
        },
        "In Favor of Tenant": True,
        "Keywords": ["right to repair", "repair requests"]
    },
    "Subletting": {
        "Description": "Regulates tenants' ability to sublet rental units.",
        "Acts": ["California Civil Code Section 1954", "New York Real Property Law Section 226-b"],
        "Charges": {
            "California": "Tenant may sublet with landlord's written consent, which cannot be unreasonably withheld.",
            "New York": "Tenant may sublet with landlord's written consent, which cannot be unreasonably withheld."
        },
        "In Favor of Tenant": True,
        "Keywords": ["subletting"]
    },
    "Termination Notice Period": {
        "Description": "Specifies the notice period tenants must provide before terminating a lease.",
        "Acts": ["California Civil Code Section 1946", "New York Real Property Law Section 232-a"],
        "Charges": {
            "California": "Tenant must provide at least 30 days' written notice to terminate a month-to-month lease.",
            "New York": "Tenant must provide at least 30 days' written notice to terminate a month-to-month lease."
        },
        "In Favor of Tenant": True,
        "Keywords": ["termination notice", "lease termination"]
    },
    "Landlord Access to Property": {
        "Description": "Regulates when and how landlords can access rental units.",
        "Acts": ["California Civil Code Section 1954", "New York Real Property Law Section 235-e"],
        "Charges": {
            "California": "Landlords must provide at least 24 hours' written notice before entering a rental unit, except in cases of emergency.",
            "New York": "Landlords must provide reasonable notice and may only enter a rental unit for specific reasons, such as repairs or inspections."
        },
        "In Favor of Tenant": True,
        "Keywords": ["landlord access", "property access"]
    },
    "Tenant Screening Fees": {
        "Description": "Regulates fees landlords can charge for tenant screening.",
        "Acts": ["California Civil Code Section 1950.6", "New York Real Property Law Section 238-a"],
        "Charges": {
            "California": "Landlords can only charge actual screening costs, and must provide itemized receipts upon request.",
            "New York": "Landlords can only charge actual screening costs, and must provide itemized receipts upon request."
        },
        "In Favor of Tenant": True,
        "Keywords": ["screening fees"]
    },
    "Late Rent Fees": {
        "Description": "Specifies allowable fees for late rent payments.",
        "Acts": ["California Civil Code Section 1947.12", "New York Real Property Law Section 235-f"],
        "Charges": {
            "California": "Landlords can charge a late fee of up to 6% of the monthly rent, or $75, whichever is less, after a grace period of 3 days.",
            "New York": "Landlords can charge a late fee of up to $50 or 5% of the rent, whichever is less, after a grace period of 5 days."
        },
        "In Favor of Tenant": False,
        "Keywords": ["late rent fees"]
    },
    "No Just Cause Eviction": {
        "Description": "Allows landlords to evict tenants without providing a specific reason.",
        "Acts": ["California Civil Code Section 1946", "New York Real Property Law Section 228"],
        "Charges": {
            "California": "Allows landlords to terminate month-to-month leases with 30 days' notice without providing a reason.",
            "New York": "Allows landlords to terminate month-to-month leases with 30 days' notice without providing a reason."
        },
        "In Favor of Tenant": False,
        "Keywords": ["no just cause eviction"]
    },
    "Rent Control Restrictions": {
        "Description": "Imposes limits on rent increases and provides eviction protections for tenants.",
        "Acts": ["California Assembly Bill 1482", "New York Rent Stabilization Law"],
        "Charges": {
            "California": "Limits annual rent increases to a certain percentage and provides eviction protections for eligible rental units.",
            "New York": "Regulates rent increases and provides stabilization for eligible rental units in specified areas."
        },
        "In Favor of Tenant": True,
        "Keywords": ["rent control", "eviction protections"]
    },
    "Tenant Remedies": {
        "Description": "Provides tenants with legal remedies for addressing housing issues.",
        "Acts": ["California Civil Code Section 1942", "New York Real Property Law Section 235-bb"],
        "Charges": {
            "California": "Allows tenants to withhold rent for repairs, terminate the lease for certain violations, or pursue legal action against landlords.",
            "New York": "Allows tenants to withhold rent for repairs, terminate the lease for certain violations, or pursue legal action against landlords."
        },
        "In Favor of Tenant": True,
        "Keywords": ["tenant remedies", "legal action"]
    },
    "Short Notice Periods for Eviction": {
        "Description": "Allows landlords to terminate leases with relatively short notice periods.",
        "Acts": ["California Civil Code Section 1946.1", "New York Real Property Actions and Proceedings Law Section 232-a"],
        "Charges": {
            "California": "Allows landlords to terminate leases with 3 days' notice for non-payment of rent or other lease violations.",
            "New York": "Allows landlords to terminate leases with 3 days' notice for non-payment of rent or other lease violations."
        },
        "In Favor of Tenant": False,
        "Keywords": ["short notice eviction"]
    },
    "High Burden of Proof": {
        "Description": "Imposes a high burden of proof on tenants in legal disputes with landlords.",
        "Acts": ["California Evidence Code", "New York Civil Practice Law and Rules"],
        "Charges": {
            "California": "Requires tenants to provide clear and convincing evidence to prevail in certain types of housing cases.",
            "New York": "Requires tenants to provide clear and convincing evidence to prevail in certain types of housing cases."
        },
        "In Favor of Tenant": False,
        "Keywords": ["burden of proof", "legal disputes"]
    },
    "Costa-Hawkins Rental Housing Act": {
        "Description": "Limits local governments' authority to enact rent control ordinances.",
        "Acts": ["California Civil Code Section 1954.50", "Costa-Hawkins Rental Housing Act"],
        "Charges": {
            "California": "Limits rent control ordinances to pre-existing structures and exempts single-family homes and condos.",
            "New York": "N/A"
        },
        "In Favor of Tenant": False,
        "Keywords": ["costa-hawkins act", "rent control"]
    },
    "Ellis Act": {
        "Description": "Allows landlords to withdraw rental properties from the market.",
        "Acts": ["California Government Code Section 7060", "Ellis Act"],
        "Charges": {
            "California": "Allows landlords to evict tenants and exit the rental market if they intend to demolish or convert the property.",
            "New York": "N/A"
        },
        "In Favor of Tenant": False,
        "Keywords": ["ellis act", "property withdrawal"]
    },
    "Rent Increase After Repairs": {
        "Description": "Allows landlords to increase rent after making substantial repairs or improvements to the rental property.",
        "Acts": ["California Civil Code Section 1941.1", "New York Real Property Law Section 235-f"],
        "Charges": {
            "California": "Allows landlords to increase rent by up to 10% within the first 12 months following substantial rehabilitation or repair.",
            "New York": "Allows landlords to increase rent by up to 10% within the first 12 months following substantial rehabilitation or repair."
        },
        "In Favor of Tenant": False,
        "Keywords": ["rent increase", "property repairs"]
    },
    "Rent Registry Requirements": {
        "Description": "Requires landlords to register rental properties with local authorities.",
        "Acts": ["California Civil Code Section 1954.25", "New York Real Property Law Section 235-c"],
        "Charges": {
            "California": "Landlords must register rental properties with the local rent control board.",
            "New York": "Landlords must register rental properties with the New York State Division of Housing and Community Renewal."
        },
        "In Favor of Tenant": True,
        "Keywords": ["rent registry", "property registration"]
    },
    "Tenant Harassment Protections": {
        "Description": "Protects tenants from harassment by landlords or their agents.",
        "Acts": ["California Civil Code Section 1940.2", "New York Real Property Law Section 235-f"],
        "Charges": {
            "California": "Prohibits landlords from harassing tenants through actions such as threats, interruptions of essential services, or unauthorized entry.",
            "New York": "Prohibits landlords from harassing tenants through actions such as threats, interruptions of essential services, or unauthorized entry."
        },
        "In Favor of Tenant": True,
        "Keywords": ["tenant harassment", "harassment protections"]
    },
    "Habitability Standards": {
        "Description": "Specifies minimum standards for rental property habitability.",
        "Acts": ["California Civil Code Section 1941.1", "New York Real Property Law Section 235-b"],
        "Charges": {
            "California": "Requires landlords to maintain rental units in a habitable condition.",
            "New York": "Requires landlords to maintain rental units in a habitable condition."
        },
        "In Favor of Tenant": True,
        "Keywords": ["habitability standards", "property conditions"]
    },
    "Security Deposit Return Requirements": {
        "Description": "Specifies requirements for returning security deposits to tenants.",
        "Acts": ["California Civil Code Section 1950.5", "New York Real Property Law Section 7-103"],
        "Charges": {
            "California": "Landlords must return security deposits within 21 days of the tenant's move-out date, along with an itemized statement of deductions.",
            "New York": "Landlords must return security deposits within a reasonable time after the tenant's move-out date, along with an itemized statement of deductions."
        },
        "In Favor of Tenant": True,
        "Keywords": ["security deposit return", "deposit refund"]
    },
    "Fair Housing Laws": {
        "Description": "Prohibits discrimination in housing based on certain protected characteristics.",
        "Acts": ["California Fair Employment and Housing Act", "New York State Human Rights Law"],
        "Charges": {
            "California": "Prohibits discrimination based on race, color, religion, sex, gender identity, sexual orientation, marital status, national origin, ancestry, familial status, disability, or source of income.",
            "New York": "Prohibits discrimination based on race, color, religion, sex, sexual orientation, gender identity or expression, national origin, marital status, age, disability, or source of income."
        },
        "In Favor of Tenant": True,
        "Keywords": ["fair housing laws", "discrimination protections"]
    }
}
coll_ref = db.collection('laws')
for law_name,law_data in rental_laws.items():
    doc = coll_ref.document(law_name)
    doc.set(law_data)
print("Data insertion complete.")