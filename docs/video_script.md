# Video run of show: 4:55 of the 5:00 limit

**Rule (event guide):** the video overview is **at most 5 minutes**. Aim to finish by 4:55; anything over 5:00 risks a penalty.

**Deck (Google Slides, editable by the whole team):**
https://docs.google.com/presentation/d/12MdTCOWkenq3uDpkiO4kSkeeBE1t4VgpGzaq6gvbblI/edit
Every slide's speaker notes hold its time slot and script.

## Schedule

| Time | Sec | Slide | Segment | Speaker |
|---|---|---|---|---|
| 0:00–0:10 | 10 | 1 | Title and hook | Nash |
| 0:10–0:30 | 20 | 2 | The problem, in three numbers | Nash |
| 0:30–0:40 | 10 | 3 | Who did what | Nash |
| 0:40–1:10 | 30 | 4 | Essential services access | Anna |
| 1:10–1:40 | 30 | 5 | Housing costs | Albert |
| 1:40–2:05 | 25 | 6 | Wages and housing affordability | Tim |
| 2:05–2:20 | 15 | 7 | One reproducible pipeline | Nash |
| 2:20–3:05 | 45 | 8 | Interactive map (live screen recording) | Jason |
| 3:05–3:35 | 30 | 9 | Model 1: rent-spike predictor, setup | Jason |
| 3:35–4:00 | 25 | 10 | Model 1: results vs baseline, subgroups, failures | Jason |
| 4:00–4:35 | 35 | 11 | Model 2: better places to rent, from the client's needs + Model 1 (demo) | Jason |
| 4:35–4:50 | 15 | 12 | Ethics: who could this hurt? | Nash |
| 4:50–4:55 | 5 | 13 | Close and repo link | Nash |

**Why this split:** each person's own analysis gets 25–30 s. Jason's map and his two models are the main focus and get 2:15 together: Model 1 flags areas likely to see a rent spike, and Model 2 uses the client's needs plus Model 1's output to suggest better places to rent. Judges check the Advanced Track list first (model, baseline, held-out test, ≥3 subgroups with failure examples), and those all have to be visible in slides 9–10. Ethics gets its own 15 s, because the rules require it to be discussed explicitly.

The redlining analysis was dropped; the 15 s it had went to the model segments.

**Pace:** about 2.5 spoken words per second, so 30 s is roughly 75 words. If a segment runs long, cut words, not time from the model segments.

## What each person owes before recording

| Who | Send to Nash | Slide |
|---|---|---|
| Anna | Confirm the "affordable but cut off" count (50 in your write-up; a recount from your CSV gives 51) | 4 |
| Tim | Finish slide 6 (headline finding with its number, chart) | 6 |
| Jason | 45 s screen recording of the map; confirm the layer list | 8 |
| Jason | Model 1: spike definition, features, model type, baseline, test split; final numbers from `03_model_vs_baseline.csv` and `04_subgroup_performance.csv`; one failure example | 9, 10 |
| Jason | Model 2: the client inputs it takes, how it uses Model 1's output, one demo client and the alternative zips it suggests, how it's evaluated | 11 |
| Everyone | Confirm the project title (working title: "Priced Out") | 1 |

Every number on a slide must come from a table or write-up in this repo (CLAUDE.md §7). Bracketed text like `[__]` on a slide is a placeholder, not a result.

## Script (also in each slide's speaker notes)

1. **Title (Nash, 10 s).** We're [team name]. Our project asks whether we can see Bay Area rent spikes coming, and help low-income renters find places they can afford to stay.
2. **Problem (Nash, 20 s).** In the median Bay Area zip code, typical rent is about $3,400 a month. Keeping that under 30% of income takes almost $137,000 a year, and rents are up more than a quarter since 2019. So we asked: can we predict rent spikes, and point renters somewhere safer?
3. **Team (Nash, 10 s).** Anna measured access to essential services, Albert housing costs, Tim wages and job affordability, I tied it into one reproducible pipeline, and Jason built the map and both models.
4. **Anna (30 s).** Food banks are the hardest essential to reach: the typical home is over a mile away. About 50 zip codes are cheap but cut off, like Vallejo, Oakley and Cloverdale. In the Mission, Fruitvale and East San Jose, check-cashing shops outnumber banks.
5. **Albert (30 s).** Typical rent runs from about $2,550 in Solano to $4,750 in San Francisco, where rent is up 43% since 2019. Buying the typical home costs 29 years of rent. Zillow's index agrees with the datathon's listings (correlation 0.81).
6. **Tim (25 s).** Wages and housing affordability, from Indeed postings, BLS wage data and Zillow estimates: [one headline finding with its number].
7. **Integration (Nash, 15 s).** Each dataset is checked against an agreed format, every join is logged, the test set stays locked until the final run, and models are scored next to baselines. One command rebuilds every number in this video.
8. **Map (Jason, 45 s, screen recording).** Pan to one zip (e.g. Vallejo 94589), click it, show its rent trend, jobs and access, then switch on one more layer. These layers are Model 1's inputs.
9. **Model 1 setup (Jason, 30 s).** What counts as a spike, what the model learns from, the baseline, and the held-out test set it never saw.
10. **Model 1 results (Jason, 25 s).** Model vs baseline on the test set; the worst subgroup; one zip it got badly wrong, and why.
11. **Model 2 (Jason, 35 s, screen recording).** A client enters their budget, workplace and needs; Model 2 combines those with Model 1's spike risk and suggests alternative zip codes, with the reason for each.
12. **Ethics (Nash, 15 s).** Landlords could misuse spike predictions, so results are zip-level only. Recommendations can steer people, so renters set every preference. Thin-data areas show "no data", not guesses.
13. **Close (Nash, 5 s).** Everything is reproducible from our public repo. Thanks for watching.

## Recording checklist
- [ ] Record each segment separately, then trim and join (easier to stay on time)
- [ ] Screen + voice at 1080p; turn off notifications; enlarge the map's text before recording
- [ ] Total runtime ≤ 5:00 after export (check the final file, not the timeline)
- [ ] Upload unlisted (YouTube or Drive), open the link in an incognito window to confirm it plays
- [ ] Put the video and deck links in the README and the Google Form
