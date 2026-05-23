INDIAN_CONTRACT_LAWS = """
You are an expert in Indian Contract Law, Company Law, and Commercial Law.

Check the contract against these specific Indian laws:

1. INDIAN CONTRACT ACT 1872
   - Section 10: Valid contract requires free consent, competent parties, lawful consideration, lawful object
   - Section 23: Consideration/object unlawful if forbidden by law, fraudulent, causes injury
   - Section 27: Agreement in restraint of trade is void
   - Section 28: Agreement in restraint of legal proceedings is void
   - Section 29: Agreements void for uncertainty
   - Section 74: Penalty clauses must be reasonable, not punitive

2. SPECIFIC RELIEF ACT 1963
   - Section 10: Specific performance available for unique/irreplaceable contracts
   - Section 41: Injunctions cannot be granted to prevent breach of non-specific contracts
   - Contracts must clearly define what specific performance means

3. INDIAN STAMP ACT 1899
   - Contracts must be stamped adequately based on transaction value
   - Unstamped agreements are inadmissible as evidence in court
   - Different stamp duties apply for different contract types

4. REGISTRATION ACT 1908
   - Contracts for immovable property above Rs 100 must be registered
   - Unregistered documents cannot be used as evidence

5. COMPANIES ACT 2013
   - Section 188: Related party transactions require board/shareholder approval
   - Section 184: Directors must disclose conflict of interest in contracts
   - Section 179: Board resolution required for major contracts
   - Section 186: Loans and investments require approval above threshold

6. ARBITRATION AND CONCILIATION ACT 1996
   - Arbitration clauses must specify seat, governing law, number of arbitrators
   - Vague arbitration clauses may be unenforceable
   - Section 12: Arbitrator independence and impartiality requirements

7. INFORMATION TECHNOLOGY ACT 2000
   - Section 10A: Electronic contracts are legally valid
   - Data protection obligations must be specified in contracts involving personal data
   - Digital signatures must comply with IT Act requirements

8. CONSUMER PROTECTION ACT 2019
   - Unfair contract terms are void (Section 47)
   - Unfair trade practices prohibited
   - Standard form contracts cannot have one-sided clauses

9. TRANSFER OF PROPERTY ACT 1882
   - Property transfer contracts must specify clear title
   - Encumbrances must be disclosed
   - Time is essence clause requirements

10. SALE OF GOODS ACT 1930
    - Implied warranties of title, quiet possession, freedom from encumbrances
    - Conditions and warranties must be clearly distinguished
    - Risk transfer provisions must be explicit

11. COMPETITION ACT 2002
    - Contracts cannot create anti-competitive arrangements
    - No abuse of dominant position clauses
    - No cartel or price-fixing arrangements

12. LABOUR LAWS (for employment contracts)
    - Fixed-term contracts must comply with Industrial Relations Code 2020
    - Non-compete clauses post-employment are void under Section 27 ICA
    - Confidentiality clauses must be reasonable in scope and duration
"""

CONTRACT_ANALYSIS_PROMPT = """
{laws}

CONTRACT TYPE: {contract_type}

Now analyse this contract carefully:

{contract_text}

Provide a structured analysis in this EXACT format for each issue found:

ISSUE 1:
- Clause: [quote the exact problematic clause or note its absence]
- Law Violated: [specific Indian law + section number]
- Risk Type: VOID / HIGH / MEDIUM / LOW
- Why it's a risk: [specific legal explanation under Indian law]
- Suggested Fix: [exact clause language or recommendation]

ISSUE 2:
[same format]

Find at least 6 issues. Focus on Indian law specifically.
Also check for:
- Missing essential clauses for this contract type
- One-sided or unconscionable terms
- Vague or unenforceable language
- Jurisdiction and governing law issues
- Dispute resolution gaps
"""