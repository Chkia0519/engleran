# Copilot instructions for this repository ✅

## Quick summary
- Tiny single-file Flask app: `app.py` is the entire application. No packages, blueprints, or templates present.
- Purpose: minimal HTTP service; the root route (`@app.route('/')`) returns the string `Hi`.

## How to run locally (Windows)
- Direct run (works as-is):
  - `python app.py`  # starts Flask development server at 127.0.0.1:5000
  - Visit: `http://127.0.0.1:5000/` → returns `Hi`
- Flask CLI (note important caveat — see "Caveats"):
  - `set FLASK_APP=app` then `set FLASK_ENV=development` then `flask run`

## Key discoveries & project-specific notes 🔎
- app.py contains an unguarded `app.run()` at module top-level. This means importing `app` (as `FLASK_APP`) will execute the server immediately on import. Agents should NOT assume `flask run` always works without modification.
- Minimal code style: inline Chinese comments and small English identifiers (e.g., `index`, `app`). Keep comments in Traditional Chinese when adding edits to match existing style.
- No dependency manifest found (no `requirements.txt` / `pyproject.toml`). The only dependency required to run is `Flask`.

## Recommended agent behaviors (explicit, actionable) ⚠️
- When adding CLI-friendly behavior, prefer changing:

```py
# current bottom of file
app.run()

# recommended pattern (example) — only modify if you intend to support `flask run` safely
if __name__ == "__main__":
    app.run(debug=True)
```

- If you add the above change, `flask run` will import the module without starting a second server and `python app.py` will still work.
- If you must use `flask run` without modifying `app.py`, run in a subprocess or avoid importing `app` directly to prevent double-run.

## Tasks agents may perform safely (and how to test them) ✅
- Add routes: follow the existing pattern `@app.route('/path')` and return plain strings for simple responses.
- Add dependency tracking: add a `requirements.txt` containing `Flask` (pin versions only when necessary).
- Local verification: run `python app.py` and check root URL returns `Hi`.

## What is NOT present / be cautious about 🚫
- No tests, CI, or packaging files to infer test or release workflow.
- No database integrations or external services; if you add one, document and add local dev instructions.

## Where to look for examples in this repo
- `app.py` — single source of truth. The root route, return type, and server start logic are all here.

---

If anything is unclear or you want the file to include more details (e.g., preferred linters, test framework, or convention rules), tell me which areas to expand and I will update this file.