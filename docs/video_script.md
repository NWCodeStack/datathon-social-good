# Video run of show: 4:55 of the 5:00 limit

**Rule (event guide):** the video overview is **at most 5 minutes**. Aim to finish by 4:55; anything over 5:00 risks a penalty.

**Deck (Google Slides, editable by the whole team):**
https://docs.google.com/presentation/d/12MdTCOWkenq3uDpkiO4kSkeeBE1t4VgpGzaq6gvbblI/edit
Every slide's speaker notes hold its time slot and script. The last slide is hidden and holds this same table.

## Schedule

| Time | Sec | Slide | Segment | Speaker |
|---|---|---|---|---|
| 0:00–0:10 | 10 | 1 | Title and hook | Nash |
| 0:10–0:30 | 20 | 2 | The problem, in three numbers | Nash |
| 0:30–0:40 | 10 | 3 | Who did what | Nash |
| 0:40–1:10 | 30 | 4 | Essential services access | Anna |
| 1:10–1:40 | 30 | 5 | Housing costs | Albert |
| 1:40–2:05 | 25 | 6 | [Tim's part] | Tim |
| 2:05–2:20 | 15 | 7 | One reproducible pipeline | Nash |
| 2:20–3:05 | 45 | 8 | Interactive map (live screen recording) | Jason |
| 3:05–3:35 | 30 | 9 | Model 1: rent-spike predictor, setup | Jason |
| 3:35–3:55 | 20 | 10 | Model 1: results vs baseline, subgroups, failures | Jason |
| 3:55–4:10 | 15 | 11 | Redlining overlay | Albert |
| 4:10–4:35 | 25 | 12 | Model 2: where to rent next (demo) | [Model 2 owner] |
| 4:35–4:50 | 15 | 13 | Ethics: who could this hurt? | Nash |
| 4:50–4:55 | 5 | 14 | Close and repo link | Nash |

**Why this split:** each person's own analysis gets 25–30 s. The map and the two models get the most time (2:15 together), because judges check the Advanced Track list first: model, baseline, held-out test, ≥3 subgroups with failure examples. Those all have to be visible in slides 9–11. Ethics gets its own 15 s, because the rules require it to be discussed explicitly.

**Pace:** about 2.5 spoken words per second, so 30 s is roughly 75 words. If a segment runs long, cut words, not time from the model segments.

## What each person owes before recording

| Who | Send to Nash | Slide |
|---|---|---|
| Anna | Confirm the "affordable but cut off" count (50 in your write-up; a recount from your CSV gives 51) | 4 |
| Albert | Redlining overlay map + share of high-risk zips per HOLC grade | 11 |
| Tim | Your role, dataset(s), one chart (PNG), one headline finding with its number | 3, 6 |
| Jason | 45 s screen recording of the map; confirm the layer list | 8 |
| Jason + Albert | Spike definition, features, model type, baseline, test split; final numbers from `03_model_vs_baseline.csv` and `04_subgroup_performance.csv`; one failure example | 9, 10 |
| Model 2 owner | Who presents; inputs; one demo profile and its top 3 zips; how it's evaluated | 12 |
| Everyone | Confirm the project title (working title: "Priced Out") | 1 |

Every number on a slide must come from a table or write-up in this repo (CLAUDE.md §7). Bracketed text like `[__]` on a slide is a placeholder, not a result.

## Script (also in each slide's speaker notes)

1. **Title (Nash, 10 s).** We're [team name]. Our project asks whether we can see Bay Area rent spikes coming, and help low-income renters find places they can afford to stay.
2. **Problem (Nash, 20 s).** In the median Bay Area zip code, typical rent is about $3,400 a month. Keeping that under 30% of income takes almost $137,000 a year, and rents are up more than a quarter since 2019. So we asked: can we predict rent spikes, and point renters somewhere safer?
3. **Team (Nash, 10 s).** Anna measured access to essential services, Albert housing costs and redlining, Tim [Tim's part], I tied it into one reproducible pipeline, and Jason built the map and the rent-spike model.
4. **Anna (30 s).** Food banks are the hardest essential to reach: the typical home is over a mile away. About 50 zip codes are cheap but cut off, like Vallejo, Oakley and Cloverdale. In the Mission, Fruitvale and East San Jose, check-cashing shops outnumber banks.
5. **Albert (30 s).** Typical rent runs from about $2,550 in Solano to $4,750 in San Francisco, where rent is up 43% since 2019. Buying the typical home costs 29 years of rent. Zillow's index agrees with the datathon's listings (correlation 0.81).
6. **Tim (25 s).** [Data used, one headline finding with its number, how it feeds the map or model.]
7. **Integration (Nash, 15 s).** Each dataset is checked against an agreed format, every join is logged, the test set stays locked until the final run, and models are scored next to baselines. One command rebuilds every number in this video.
8. **Map (Jason, 45 s, screen recording).** Pan to one zip (e.g. Vallejo 94589), click it, show its rent trend, jobs and access, then switch on one more layer. These layers are Model 1's inputs.
9. **Model 1 setup (Jason, 30 s).** What counts as a spike, what the model learns from, the baseline, and the held-out test set it never saw.
10. **Model 1 results (Jason, 20 s).** Model vs baseline on the test set; the worst subgroup; one zip it got badly wrong, and why.
11. **Redlining (Albert, 15 s).** 1930s HOLC grades overlaid on spike risk. Association, not proof of cause.
12. **Model 2 (25 s, screen recording).** One renter profile in, a ranked list of zip codes with reasons out.
13. **Ethics (Nash, 15 s).** Landlords could misuse spike predictions, so results are zip-level only. Recommendations can steer people, so renters set every preference. Thin-data areas show "no data", not guesses.
14. **Close (Nash, 5 s).** Everything is reproducible from our public repo. Thanks for watching.

## Recording checklist
- [ ] Record each segment separately, then trim and join (easier to stay on time)
- [ ] Screen + voice at 1080p; turn off notifications; enlarge the map's text before recording
- [ ] Total runtime ≤ 5:00 after export (check the final file, not the timeline)
- [ ] Upload unlisted (YouTube or Drive), open the link in an incognito window to confirm it plays
- [ ] Put the video and deck links in the README and the Google Form
