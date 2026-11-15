# Wages and Housing Affordability: Tim 

**Datathon for Social Good 2026 · Bay Area Affordability Project**

This part of the project estimates what common Bay Area jobs pay, measures historical wage growth, and compares annual pay with the cost of renting or buying a typical home.

**Main outputs for the team:** `outputs/wages_by_job_city.csv` and `outputs/burden_by_job_zip.csv`.

---

## Key findings

1. **Typical rent can exceed a worker’s entire gross salary.** The Belmont cashier estimate implies spending **114.8% of annual pay** renting a typical home. This estimate has fewer than 10 usable salaries and is illustrative rather than a headline finding.
2. **Higher pay does not necessarily make buying affordable.** In Burlingame, the software-engineer estimate puts rent at **22.6% of gross pay**, but buying requires approximately **3.43 times that salary** under the mortgage assumptions.
3. **Historical wage growth varies by occupation and metro.** Average annual software-developer wage growth was approximately **4.35% in the San Francisco metro** and **6.76% in the San Jose metro**, using the retained annual comparisons.
4. **Some local estimates have limited support.** Posting counts and usable-salary counts distinguish stronger estimates from thin data.
5. **Missing information remains missing.** Unavailable salaries, rents, home values, and growth estimates are not replaced with zero.

These results compare advertised pay with typical housing costs. They do not measure what individual households actually earn or spend.

---

## What I did

| Step | What it does |
|---|---|
| 1. Inspect the sample | Loaded the 1,000-posting Indeed sample and examined salary formats, locations, and missing values. |
| 2. Process the full dataset | Read the approximately 2 GB Indeed file in 100,000-row chunks, retaining featured jobs. |
| 3. Remove duplicates | Removed duplicate combinations of job title, company name, and location. |
| 4. Identify cities | Extracted California cities from location strings, including full street addresses. |
| 5. Filter geography | Matched extracted cities and communities to the nine Bay Area counties. |
| 6. Group jobs | Used documented title keyword rules to assign postings to 12 featured jobs. |
| 7. Hand-check | Reviewed 20 sampled titles per job and excluded incorrect matches. |
| 8. Clean salaries | Converted supported salary formats to annual equivalents and tracked missing pay. |
| 9. Summarize wages | Calculated median annual pay, posting counts, usable-pay counts, and missing-pay share by job and city. |
| 10. Add BLS history | Extracted occupation wages from five metro areas for May 2021–2025. |
| 11. Project pay | Applied historical average wage growth to current Indeed median pay. |
| 12. Join housing | Joined ZIP-level housing estimates to city-level wages using normalized city names. |
| 13. Calculate affordability | Calculated rent burden and ownership gap for available job/ZIP combinations. |
| 14. Create a figure | Plotted high rent-burden examples meeting salary and housing data-quality thresholds. |

The full-file job filter produced **15,223 postings after deduplication**. The initial Bay Area filter retained **6,162**. Manual-review exclusion rules reduced this to **6,019**, before narrowing the teacher category to K–12.

### Featured jobs

| Job group | Examples or scope |
|---|---|
| Cashier | Cashier and related front-end roles |
| Retail sales | Retail sales associate roles |
| Food service worker | Food service workers, baristas, restaurant servers, and hosts |
| Home health aide | Home health and personal care aides |
| Childcare worker | Childcare and nanny roles; pet daycare excluded |
| Warehouse worker | Warehouse and material-handling roles; management excluded |
| Medical assistant | Medical assistant roles |
| K–12 teacher | Explicitly identified K–12 classroom roles |
| Registered nurse | RN roles; identified management and advanced-practice roles excluded |
| Electrician | Electrician roles |
| Accountant | Accountant roles across experience levels |
| Software engineer | Software engineer and developer roles; internships excluded |

### How annual pay works

Salary ranges use their midpoint.

| Pay unit | Annual conversion |
|---|---|
| Hourly | Pay × 2,080 |
| Weekly | Pay × 52 |
| Monthly | Pay × 12 |
| Annual | Use directly |

English and Spanish pay-unit labels are supported. One-sided offers such as “From $19 an hour” are excluded from pay medians because they provide a bound rather than a complete estimate.

### How wage growth works

1. Compare BLS annual median wages within each metro and occupation.
2. Calculate each valid consecutive-year percentage change.
3. Average the available changes, requiring at least two.
4. Apply that growth rate to the Indeed median pay.

**Projected pay = median annual pay × (1 + average annual wage growth).**

Food service, warehouse work, and K–12 teaching span multiple BLS occupations. Their growth estimates use equal weights across the mapped occupations. If a required occupation lacks usable growth, the combined estimate remains blank.

### How rent burden works

**Rent burden = 12 × typical monthly rent ÷ median annual pay.**

A value of **0.40** means rent consumes **40% of gross annual pay**. Values above 1.0 are retained.

### How ownership gap works

1. Finance 80% of the typical home value, assuming 20% down.
2. Calculate principal-and-interest payments for a 30-year fixed mortgage.
3. Divide annual payments by 0.30 to estimate required gross income.
4. Divide required income by the job’s median annual pay.

**Ownership gap = required annual income ÷ median annual pay.**

A value of **2.0** means buying requires twice the estimated job salary.

The calculation uses a **7.11% annual interest rate**, reported by the participant as Freddie Mac’s November 12, 2026 rate. Independent verification remains pending.

---

## Data decisions

- **Annualization is a full-time equivalent.** Hourly wages assume 2,080 hours annually; weekly wages assume 52 weeks.
- **Implausible salaries are excluded.** Annualized values below $15,000 or above $1,000,000 are not used.
- **Suspicious units are not guessed.** Incorrect-looking salary amounts or units remain missing.
- **Daily pay is excluded.** Annual working days are unknown.
- **Tips are excluded.**
- **Missing and unusable pay are different.** `share_missing_pay` measures absent salary text, not every unsuccessful conversion.
- **Postings without usable pay remain in posting counts.**
- **Thin data is flagged.** `thin_data` means fewer than 10 postings; `thin_pay_data` means fewer than 10 usable salaries.
- **K–12 teachers require explicit school-level evidence.** Preschool, assistants, substitutes, tutoring, after-school, and identified special-education roles are excluded.
- **ZIP codes are stored as five-character text.**
- **Housing estimates retain their original meaning.** `typical_rent` and `typical_home_value` are not described as listing medians.
- **Seven housing rows were excluded** because of out-of-area or unverified ZIP mappings, leaving 286 housing ZIP rows.
- **Growth projections are scenarios**, not validated forecasting-model predictions.

---

## Potential biases

- **Advertised pay is not actual earnings.** The sample reflects available postings rather than all employed workers.
- **Annualization assumes consistent work.** It can overstate earnings for part-time, seasonal, travel, or school-year work.
- **Seniority varies.** Job groups can mix entry-level and experienced workers.
- **City wages are applied across ZIPs.** The method does not measure ZIP-specific wages or commuting patterns.
- **Missing pay may be selective.** Employers disclosing salaries may differ from those that do not.
- **Housing costs are not household-specific.** Roommates, multiple earners, household size, and housing size affect affordability.
- **Ownership costs are incomplete.** Taxes, insurance, HOA fees, maintenance, closing costs, and the ability to save a down payment are excluded.
- **BLS changes are not individual raises.** They may reflect workforce composition and estimation changes.
- **Keyword matching is approximate.** Reviewing matches identifies false positives but does not measure missed jobs.
- **ZIP geography is imperfect.** ZIP reference checks do not replace address-level boundary validation.

---

## Files in this contribution

| File | What it is |
|---|---|
| `outputs/wages_by_job_city.csv` | Current pay, posting counts, missing-pay share, growth, projections, and quality flags |
| `outputs/burden_by_job_zip.csv` | Required rent-burden and ownership-gap measures by job and ZIP |
| `outputs/burden_by_job_zip_details.csv` | Supporting housing, salary, mortgage calculations, and quality flags |
| `outputs/figures/wages_rent_burden.png` | Rent-burden figure using estimates meeting data-quality thresholds |
| `notebooks/wages_and_affordability.ipynb` | Cleaning, wage-growth, housing-affordability, and export workflow |

Additional audit files are generated in the notebook’s configured Drive output folder. These include cleaned postings, BLS history, title-review samples, housing exclusions, and unmatched cities.

### Wage and burden columns

| Column | Meaning |
|---|---|
| `job` | Featured occupation group |
| `city` | City associated with the postings |
| `median_pay` | Median usable annualized advertised pay, USD |
| `n_postings` | Number of retained postings |
| `n_usable_pay` | Number contributing to the pay median |
| `share_missing_pay` | Fraction without salary text |
| `wage_growth` | Historical average annual growth as a decimal |
| `projected_pay` | One-year pay scenario, USD |
| `zipcode` | Five-digit ZIP. Read as text. |
| `rent_burden` | Annual typical rent divided by annual pay |
| `ownership_gap` | Required buying income divided by annual pay |
| `thin_data` | Fewer than 10 postings |
| `thin_pay_data` | Fewer than 10 usable salaries |

### Rent burden figure

![Rent burden by job and city](../outputs/figures/wages_rent_burden.png)

The figure shows the **10 highest rent-burden examples** among job/city estimates with at least **10 usable salaries** and housing not flagged as low data. Each job/city appears once, using its highest-burden ZIP.

| Element | How to read it |
|---|---|
| Horizontal bars | Typical annual rent as a percentage of one worker’s gross annual pay |
| Dashed line | 30% reference |
| Values above 100% | Typical annual rent exceeds the estimated annual salary |

The figure compares typical whole-home rent with one worker’s salary. It does not measure actual household spending or account for roommates, multiple earners, taxes, or differences in housing size.

The figure selects high-burden examples; it does not show the full distribution of Bay Area affordability.

---

## Notes for Person 4

- **Join on job and ZIP.** The burden table contains multiple jobs per ZIP.
- **Preserve missing values and quality flags.** Missing does not mean zero.
- **Use at least 10 usable salaries** and exclude housing `low_data` rows for headline findings.
- **Some cities lack matching wages.** Do not invent a zero-pay or regional fallback.
- **Solano K–12 growth remains unavailable.**
- **Metro-boundary verification is pending.** Name changes in 2024 triggered temporary exclusions of the corresponding annual comparisons for San Francisco, Santa Rosa, and Vallejo. A changed name alone does not prove a boundary change.
- **Independently verify the mortgage rate** before submission.
- **Confirm joins and rerun the cleaned notebook** from top to bottom before freezing deliverables.
- **Show results at ZIP level**, not individual addresses.

---

## Sources

- Indeed job-listings dataset supplied for the datathon.
- [BLS OEWS tables](https://www.bls.gov/oes/tables.htm), May 2021–2025 metropolitan releases.
- Person 1’s `albert_housing_by_zip.csv`.
- [Freddie Mac PMMS](https://www.freddiemac.com/pmms), rate supplied by the participant and pending independent verification.
- [GeoNames postal data](https://download.geonames.org/export/zip/) and [free ZIP reference data](https://github.com/midwire/free_zipcode_data) for housing geography checks.
