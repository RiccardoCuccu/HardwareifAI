# Industry

Holds dated quarterly market-analysis snapshots, produced per [`methodology/industry_analysis.md`](../../methodology/industry_analysis.md) using [`templates/industry_analysis_template.md`](../../templates/industry_analysis_template.md).

## Contents

- `<quarter>/<quarter>.md` - the filled snapshot for that quarter (e.g. `2026-Q3/2026-Q3.md`): companies scanned and the observed skills cluster.
- `<quarter>/job_posts/` - the underlying job postings behind that quarter's snapshot, one filled record per selected posting plus an `html/` snapshot subfolder.

No particular reading order; a new quarter folder is added each time the refresh cadence runs.
